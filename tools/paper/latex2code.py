#!/usr/bin/env python3
"""Convert the restricted LaTeX of the MOISE agent edition into a plain code form.

Code form conventions (Dynare-like):
  * every model symbol becomes an identifier from the glossary (key = LaTeX symbol without
    its time index), e.g.  \\hat{\\pi}_{IM,t+1}  ->  pi_IM(+1)
  * time index t -> no suffix, t+k -> (+k), t-k -> (-k)
  * E_{t}( ... ) is dropped (expectations are implicit, as in Dynare); any other E_ is an error
  * multiplication is explicit '*', powers '^', fractions '(a)/(b)', all brackets become ( )
  * a run of letters without spaces (EX, tp, CA) is ONE identifier, never a product
  * \\Delta X_{t} (an observed first difference) is the single identifier for key \\Delta{X}
  * (A/B)_{t} with a subscript is the single identifier for key (A/B)
The converter is strict: anything it does not understand raises ConvertError, so a person
looks at it instead of the converter guessing.
"""
import re

GREEK = {
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta", "theta",
    "vartheta", "iota", "kappa", "varkappa", "lambda", "mu", "nu", "xi", "pi", "varpi", "rho",
    "varrho", "sigma", "varsigma", "tau", "upsilon", "phi", "varphi", "chi", "psi", "omega",
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon", "Phi", "Psi", "Omega",
    "imath", "jmath", "ell",
}
ACCENTS = {"hat", "widehat", "bar", "overline", "tilde", "widetilde", "check", "dot", "breve"}
IGNORED = {"left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl", "Bigr",
           "displaystyle", "textstyle", "nonumber", "quad", "qquad"}
TIME_RE = re.compile(r"^t(?:([+-])(\d+))?$")
OPEN = {"(": ")", "[": "]", "\\{": "\\}"}


class ConvertError(Exception):
    pass


# ----------------------------------------------------------------------------- tokenizer
def tokenize(s):
    toks, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c == "\\":
            m = re.match(r"\\([A-Za-z]+)", s[i:])
            if m:
                toks.append(("cmd", m.group(1))); i += len(m.group(0))
            else:
                toks.append(("sym", s[i:i + 2])); i += 2      # \\  \{  \}  \_  \,
        elif c.isdigit() or (c == "." and i + 1 < len(s) and s[i + 1].isdigit()):
            m = re.match(r"\d*\.?\d+", s[i:])
            toks.append(("num", m.group(0))); i += len(m.group(0))
        elif c.isalpha():
            m = re.match(r"[A-Za-z]+", s[i:])
            toks.append(("let", m.group(0))); i += len(m.group(0))
        else:
            toks.append(("sym", c)); i += 1
    return toks


def read_group_raw(toks, i):
    """toks[i] must be '{'; return (inner_tokens, index_after)."""
    if i >= len(toks) or toks[i] != ("sym", "{"):
        raise ConvertError("expected '{'")
    depth, j, out = 0, i, []
    while j < len(toks):
        t = toks[j]
        if t == ("sym", "{"):
            depth += 1
            if depth > 1:
                out.append(t)
        elif t == ("sym", "}"):
            depth -= 1
            if depth == 0:
                return out, j + 1
            out.append(t)
        else:
            out.append(t)
        j += 1
    raise ConvertError("unclosed '{'")


def detok(toks):
    out = []
    for k, (kind, v) in enumerate(toks):
        if kind == "cmd":
            out.append("\\" + v)
            nxt = toks[k + 1] if k + 1 < len(toks) else None
            if nxt and nxt[0] in ("let", "cmd", "num"):
                out.append(" ")
        else:
            out.append(v)
            nxt = toks[k + 1] if k + 1 < len(toks) else None
            if kind in ("let", "num") and nxt and nxt[0] in ("let", "num"):
                out.append(" ")
    return "".join(out).strip()


class Atom:
    """A model symbol occurrence: accents + base + subscript labels + superscript + time."""
    def __init__(self):
        self.accents = []      # outer -> inner, e.g. ['hat', 'bar']
        self.base = ""
        self.sub = []          # label parts (without time)
        self.sup = None        # superscript label string or None
        self.prime = False
        self.lag = 0
        self.has_time = False
        self.delta = False     # \Delta prefix (observed first difference)

    def key(self):
        k = self.base
        for a in reversed(self.accents):
            k = "\\" + a + "{" + k + "}"
        if self.prime:
            k += "'"
        if self.sub:
            k += "_{" + ",".join(self.sub) + "}"
        if self.sup is not None:
            k += "^{" + self.sup + "}"
        if self.delta:
            k = "\\Delta{" + k + "}"
        return k


def split_sub(raw):
    parts, depth, cur = [], 0, []
    for t in raw:                      # split on top-level commas only
        if t == ("sym", "{"):
            depth += 1
        elif t == ("sym", "}"):
            depth -= 1
        if t == ("sym", ",") and depth == 0:
            parts.append(cur); cur = []
        else:
            cur.append(t)
    parts.append(cur)
    parts = [detok(p) for p in parts]
    lag, has_time = 0, False
    if parts:
        m_nest = re.match(r"^(.*?)_\{(t(?:[+-]\d+)?)\}(\^\{.*\})?$", parts[-1].replace(" ", ""))
        if m_nest and m_nest.group(1):
            mt = TIME_RE.match(m_nest.group(2))
            has_time = True
            if mt.group(1):
                lag = int(mt.group(2)) * (1 if mt.group(1) == "+" else -1)
            parts[-1] = m_nest.group(1) + (m_nest.group(3) or "")
            return [p for p in parts if p != ""], lag, has_time
    if parts and TIME_RE.match(parts[-1].replace(" ", "")):
        m = TIME_RE.match(parts[-1].replace(" ", ""))
        has_time = True
        if m.group(1):
            lag = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
        parts = parts[:-1]
    return [p for p in parts if p != ""], lag, has_time


def is_label_sup(raw):
    """A superscript is a label (part of the name) unless it looks like an exponent."""
    if not raw:
        return False
    if raw in ([("sym", "+")], [("sym", "-")]):
        return True
    if any(t in (("sym", "+"), ("sym", "-"), ("sym", "/")) for t in raw):
        return False
    if any(t[0] == "cmd" and t[1] in ("frac", "ln", "exp", "log") for t in raw):
        return False
    if any(t[0] == "cmd" and t[1] in ACCENTS for t in raw):
        return True           # an accented symbol is a label, e.g. eta^{bar{Pi}}
    if all(t[0] == "num" for t in raw):
        return False
    if any(t[0] == "cmd" and t[1] in GREEK for t in raw) and not any(t[0] == "let" or t == ("sym", "*") for t in raw):
        return False          # pure Greek superscript: treat as exponent unless known in glossary
    return True


# ----------------------------------------------------------------------------- parser
class Parser:
    def __init__(self, toks, glossary):
        self.t = toks
        self.i = 0
        self.g = glossary          # dict latex_key -> code name
        self.unknown = []
        self.uses = []             # (key, has_time) for every symbol occurrence

    def peek(self, k=0):
        j = self.i + k
        return self.t[j] if j < len(self.t) else ("eof", None)

    def eat(self, tok=None):
        cur = self.peek()
        if tok is not None and cur != tok:
            raise ConvertError(f"expected {tok[1]!r}, found {cur[1]!r} at token {self.i}")
        self.i += 1
        return cur

    def skip_ignored(self):
        while self.peek()[0] == "cmd" and self.peek()[1] in IGNORED:
            self.i += 1

    def sub_parser(self, toks):
        p = Parser(toks, self.g)
        return p

    def equation(self):
        sides = [self.expr()]
        while self.peek() == ("sym", "="):
            self.eat(); sides.append(self.expr())
        self.skip_ignored()
        if self.peek()[0] != "eof":
            raise ConvertError(f"unexpected token {self.peek()[1]!r} at {self.i}")
        return " = ".join(sides)

    def expr(self):
        self.skip_ignored()
        out = ""
        if self.peek() in (("sym", "+"), ("sym", "-")):
            out += self.eat()[1]
        out += self.term()
        while True:
            self.skip_ignored()
            if self.peek() in (("sym", "+"), ("sym", "-")):
                op = self.eat()[1]
                out += f" {op} " + self.term()
            else:
                break
        return out

    def starts_factor(self):
        k, v = self.peek()
        if k in ("num", "let"):
            return True
        if k == "cmd":
            return v in GREEK or v in ACCENTS or v in ("frac", "dfrac", "tfrac", "ln", "exp", "log", "left")
        if k == "sym":
            return v in ("(", "[", "\\{", "{")
        return False

    def term(self):
        out = self.factor()
        while True:
            self.skip_ignored()
            k, v = self.peek()
            if (k, v) in (("cmd", "cdot"), ("cmd", "times")):
                self.eat(); out += "*" + self.factor()
            elif (k, v) == ("sym", "/"):
                self.eat(); out = f"{out}/" + self.factor()
            elif self.starts_factor():
                out += "*" + self.factor()
            else:
                break
        return out

    def factor(self):
        self.skip_ignored()
        if self.peek() in (("sym", "-"), ("sym", "+")):
            op = self.eat()[1]
            return ("-" if op == "-" else "") + self.factor()
        base = self.primary()
        self.skip_ignored()
        if self.peek() == ("sym", "^"):
            self.eat()
            raw, self.i = read_group_raw(self.t, self.i)
            sub = self.sub_parser(raw)
            e = sub.expr()
            if sub.peek()[0] != "eof":
                raise ConvertError("could not parse exponent")
            self.unknown += sub.unknown; self.uses += sub.uses
            e_txt = e if _wrapped(e) else f"({e})"
            base = f"({base})^{e_txt}" if not re.fullmatch(r"[\w]+(\([+-]\d+\))?", base) else f"{base}^{e_txt}"
        return base

    def primary(self):
        self.skip_ignored()
        k, v = self.peek()
        if k == "cmd" and v in ("ldots", "cdots", "dots", "dotsb"):
            raise ConvertError("the printed equation contains an ellipsis (...); no code form - expand the terms by hand")
        if k == "num":
            self.eat(); return v
        if k == "sym" and v in OPEN:
            start = self.i
            self.eat()
            inner = self.expr()
            self.skip_ignored()
            if self.peek() != ("sym", OPEN[v]):
                raise ConvertError(f"expected closing {OPEN[v]!r}, found {self.peek()[1]!r} at {self.i}")
            self.eat()
            if v == "(" and self.peek() == ("sym", "_"):
                # named ratio such as (CA/Y)_{t}
                inner_raw = [t for t in self.t[start + 1:self.i - 1] if not (t[0] == "cmd" and t[1] in IGNORED)]
                a = Atom(); a.base = "(" + detok(inner_raw) + ")"
                self.eat()
                raw, self.i = read_group_raw(self.t, self.i)
                a.sub, a.lag, a.has_time = split_sub(raw)
                return self.lookup(a)
            return "(" + inner + ")"
        if (k, v) == ("sym", "{"):
            # braced group used as an atom base, e.g. {Y^{*}}_{t}
            return self.atom()
        if k == "cmd" and v in ("frac", "dfrac", "tfrac"):
            self.eat()
            num_raw, self.i = read_group_raw(self.t, self.i)
            den_raw, self.i = read_group_raw(self.t, self.i)
            a, b = self.sub_parser(num_raw), self.sub_parser(den_raw)
            na, nb = a.expr(), b.expr()
            if a.peek()[0] != "eof" or b.peek()[0] != "eof":
                raise ConvertError("could not parse fraction")
            self.unknown += a.unknown + b.unknown; self.uses += a.uses + b.uses
            return f"({na})/({nb})"
        if k == "cmd" and v in ("ln", "exp", "log"):
            self.eat()
            arg = self.factor()
            return f"{v}({arg})" if not arg.startswith("(") else f"{v}{arg}"
        if k == "let" and v == "E" and self.peek(1) == ("sym", "_"):
            # E_{t}: expectation operator if something to take the expectation of follows
            save = self.i
            self.eat(); self.eat(("sym", "_"))
            raw, j = read_group_raw(self.t, self.i)
            after = self.t[j] if j < len(self.t) else ("eof", None)
            is_op = after in (("sym", "("), ("sym", "["), ("sym", "\\{")) or after == ("cmd", "left") \
                or after[0] == "let" or (after[0] == "cmd" and (after[1] in GREEK or after[1] in ACCENTS or after[1] == "frac"))
            if is_op:
                if detok(raw).replace(" ", "") != "t":
                    raise ConvertError(f"expectation with subscript {detok(raw)!r} not supported")
                self.i = j
                self.skip_ignored()
                if self.peek()[0] == "sym" and self.peek()[1] in OPEN:
                    return self.primary()
                return self.factor()
            self.i = save
            return self.atom()
        if k == "cmd" and v == "Delta":
            nxt = self.peek(1)
            if nxt[0] == "let" or nxt == ("sym", "{") or (nxt[0] == "cmd" and (nxt[1] in ACCENTS or (nxt[1] in GREEK and nxt[1] != "Delta"))):
                self.eat()
                name = self.atom(delta=True)
                return name
            raise ConvertError("\\Delta not followed by a symbol")
        if k == "let" or (k == "cmd" and (v in GREEK or v in ACCENTS)):
            return self.atom()
        raise ConvertError(f"cannot parse token {v!r} at {self.i}")

    def lookup(self, a):
        key = a.key()
        self.uses.append((key, a.has_time))
        name = None
        if a.has_time and not a.accents and (key + "@t") in self.g:
            # an unhatted symbol with a time index (an observed level) can have its own name,
            # distinct from the same letters without a time index (a steady-state value)
            name = self.g[key + "@t"]
        if name is None:
            name = self.g.get(key)
        if name is None:
            self.unknown.append(key)
            name = "<" + key + ">"
        if a.lag:
            name += f"({a.lag:+d})"
        return name

    def atom(self, delta=False):
        a = self.atom_struct()
        if delta:
            a.delta = True
        return self.lookup(a)

    def atom_struct(self):
        """Parse one symbol occurrence and return the Atom (no glossary lookup)."""
        a = Atom()
        k, v = self.peek()
        if k == "cmd" and v in ACCENTS:
            acc = self.eat()[1]
            raw, self.i = read_group_raw(self.t, self.i)
            a.accents.append(acc)
            inner_toks = raw
            while inner_toks and inner_toks[0][0] == "cmd" and inner_toks[0][1] in ACCENTS:
                acc2 = inner_toks[0][1]
                raw2, j = read_group_raw(inner_toks, 1)
                if j != len(inner_toks):
                    raise ConvertError("unexpected tokens after nested accent")
                a.accents.append(acc2)
                inner_toks = raw2
            a.base = detok(inner_toks)
        elif (k, v) == ("sym", "{"):
            raw, self.i = read_group_raw(self.t, self.i)
            inner = Parser(raw, self.g)
            a = inner.atom_struct()
            if inner.peek()[0] != "eof":
                raise ConvertError("braced group is not a single symbol")
        elif k == "let" or (k == "cmd" and v in GREEK):
            self.eat()
            a.base = "\\" + v if k == "cmd" else v
        else:
            raise ConvertError(f"expected a symbol, found {v!r} at {self.i}")
        # prime, star, subscript, superscript
        while True:
            if self.peek() == ("sym", "'"):
                self.eat(); a.prime = True
            elif self.peek() == ("sym", "*") and a.sup is None:
                self.eat(); a.sup = "*"
            elif self.peek() == ("sym", "_"):
                self.eat()
                raw, self.i = read_group_raw(self.t, self.i)
                labels, lag, has_time = split_sub(raw)
                a.sub = a.sub + labels
                if has_time:
                    a.lag, a.has_time = lag, True
            elif self.peek() == ("sym", "^"):
                save = self.i
                self.eat()
                raw, j = read_group_raw(self.t, self.i)
                trial = Atom(); trial.__dict__.update(a.__dict__); trial.sup = detok(raw)
                if trial.key() in self.g or is_label_sup(raw):
                    a.sup = detok(raw) if a.sup is None else a.sup + detok(raw)
                    self.i = j
                else:
                    self.i = save
                    break
            else:
                break
        return a


def _wrapped(e):
    """True if e is one parenthesized group, e.g. '(a+b)' but not '(a)+(b)'."""
    if not (e.startswith("(") and e.endswith(")")):
        return False
    depth = 0
    for i, ch in enumerate(e):
        depth += ch == "("
        depth -= ch == ")"
        if depth == 0 and i < len(e) - 1:
            return False
    return True


def clean_latex(latex):
    s = re.sub(r"\\tag\{[^}]*\}", "", latex)
    s = s.replace("\\begin{aligned}", "").replace("\\end{aligned}", "")
    s = re.sub(r"\\begin\{array\}\{[^}]*\}", " ", s).replace("\\end{array}", " ")
    s = s.replace("&", " ").replace("\\\\", " ")
    s = s.replace("={}", "=")
    s = re.sub(r"\\(left|right)\s*\.", " ", s)          # \left. \right.
    s = re.sub(r"\\(left|right)\s*(?=[(\[)\]|])", " ", s)
    s = re.sub(r"\\(left|right)\s*\\\{", r" \\{", s)
    s = re.sub(r"\\(left|right)\s*\\\}", r" \\}", s)
    s = re.sub(r"\\(big|Big|bigg|Bigg)[lr]?\s*", " ", s)
    s = s.replace("\\,", " ").replace("\\;", " ").replace("\\!", "").replace("\\quad", " ")
    return s


def to_code(latex, glossary, with_uses=False):
    """Return (code_string, unknown_symbol_keys[, uses]). Raises ConvertError on syntax it can't handle."""
    p = Parser(tokenize(clean_latex(latex)), glossary)
    code = p.equation()
    code = re.sub(r"\s+", " ", code).strip()
    if with_uses:
        return code, sorted(set(p.unknown)), p.uses
    return code, sorted(set(p.unknown))


if __name__ == "__main__":
    import sys
    print(to_code(sys.argv[1], {}))
