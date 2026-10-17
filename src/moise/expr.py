"""A small, safe parser and evaluator for model expressions.

Grammar (the "code form" used in docs/paper and model/*.yaml):

    equation := expr ['=' expr]
    expr     := term (('+' | '-') term)*
    term     := unary (('*' | '/') unary)*
    unary    := ('+' | '-') unary | power
    power    := atom ['^' unary]              # right-associative; -x^2 == -(x^2)
    atom     := NUMBER
              | NAME                          # variable at t, or a parameter
              | NAME '(' ['+' | '-'] INT ')'  # variable lead/lag: x(+1), x(-1)
              | FUNC '(' expr ')'             # exp, log, ln, sqrt
              | '(' expr ')'

Any identifier is allowed as a NAME, including Python keywords such as ``lambda``.
Nothing is evaluated with ``eval``: expressions are parsed into a small tree.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Callable, Iterator, Union

FUNCS = {"exp": math.exp, "log": math.log, "ln": math.log, "sqrt": math.sqrt}

_TOKEN = re.compile(
    r"\s*(?:(?P<num>\d+\.\d*(?:[eE][+-]?\d+)?|\.\d+(?:[eE][+-]?\d+)?|\d+(?:[eE][+-]?\d+)?)"
    r"|(?P<name>[A-Za-z_][A-Za-z0-9_]*)|(?P<op>[-+*/^(),=]))"
)


class ExprError(ValueError):
    """Raised for syntax errors and unknown names."""


# ----------------------------------------------------------------------------- AST
@dataclass(frozen=True)
class Num:
    value: float


@dataclass(frozen=True)
class Var:
    name: str
    lag: int = 0          # 0 = time t, +1 = t+1, -1 = t-1


@dataclass(frozen=True)
class Neg:
    arg: "Node"


@dataclass(frozen=True)
class Bin:
    op: str
    left: "Node"
    right: "Node"


@dataclass(frozen=True)
class Func:
    name: str
    arg: "Node"


Node = Union[Num, Var, Neg, Bin, Func]


# ----------------------------------------------------------------------------- tokenizer
def _tokens(src: str) -> list[tuple[str, str]]:
    out, pos = [], 0
    src = src.rstrip()
    while pos < len(src):
        m = _TOKEN.match(src, pos)
        if not m or m.end() == pos:
            raise ExprError(f"cannot read {src[pos:pos + 15]!r} in {src!r}")
        pos = m.end()
        for kind in ("num", "name", "op"):
            if m.group(kind) is not None:
                out.append((kind, m.group(kind)))
                break
    return out


class _Parser:
    def __init__(self, src: str):
        self.src = src
        self.t = _tokens(src)
        self.i = 0

    def peek(self, k: int = 0):
        j = self.i + k
        return self.t[j] if j < len(self.t) else ("eof", "")

    def eat(self, value: str | None = None):
        tok = self.peek()
        if value is not None and tok[1] != value:
            raise ExprError(f"expected {value!r}, found {tok[1]!r} in {self.src!r}")
        self.i += 1
        return tok

    def expr(self) -> Node:
        node = self.term()
        while self.peek()[1] in ("+", "-"):
            op = self.eat()[1]
            node = Bin(op, node, self.term())
        return node

    def term(self) -> Node:
        node = self.unary()
        while self.peek()[1] in ("*", "/"):
            op = self.eat()[1]
            node = Bin(op, node, self.unary())
        return node

    def unary(self) -> Node:
        if self.peek()[1] == "-":
            self.eat()
            return Neg(self.unary())
        if self.peek()[1] == "+":
            self.eat()
            return self.unary()
        return self.power()

    def power(self) -> Node:
        base = self.atom()
        if self.peek()[1] == "^":
            self.eat()
            return Bin("^", base, self.unary())
        return base

    def atom(self) -> Node:
        kind, val = self.peek()
        if kind == "num":
            self.eat()
            return Num(float(val))
        if kind == "name":
            self.eat()
            if self.peek()[1] != "(":
                return Var(val, 0)
            if val in FUNCS:
                self.eat("(")
                arg = self.expr()
                self.eat(")")
                return Func(val, arg)
            # lead/lag
            self.eat("(")
            sign = 1
            if self.peek()[1] in ("+", "-"):
                sign = -1 if self.eat()[1] == "-" else 1
            k, num = self.eat()
            if k != "num" or not re.fullmatch(r"\d+", num):
                raise ExprError(f"{val}(...) must be a lead/lag like {val}(+1) in {self.src!r}")
            self.eat(")")
            return Var(val, sign * int(num))
        if val == "(":
            self.eat()
            node = self.expr()
            self.eat(")")
            return node
        raise ExprError(f"unexpected {val!r} in {self.src!r}")


def parse(src: str) -> Node:
    """Parse one expression."""
    p = _Parser(src)
    node = p.expr()
    if p.peek()[0] != "eof":
        raise ExprError(f"unexpected {p.peek()[1]!r} in {src!r}")
    return node


def parse_equation(src: str) -> Node:
    """Parse 'lhs = rhs' (or a bare expression meaning expr = 0) into the residual lhs - rhs."""
    parts = src.split("=")
    if len(parts) == 1:
        return parse(src)
    if len(parts) != 2:
        raise ExprError(f"an equation needs exactly one '=': {src!r}")
    return Bin("-", parse(parts[0]), parse(parts[1]))


# ----------------------------------------------------------------------------- utilities
def walk(node: Node) -> Iterator[Node]:
    yield node
    if isinstance(node, (Neg, Func)):
        yield from walk(node.arg)
    elif isinstance(node, Bin):
        yield from walk(node.left)
        yield from walk(node.right)


def names(node: Node) -> set[tuple[str, int]]:
    """All (name, lag) pairs in an expression."""
    return {(n.name, n.lag) for n in walk(node) if isinstance(n, Var)}


def evaluate(node: Node, lookup: Callable[[str, int], float]) -> float:
    """Evaluate with lookup(name, lag) -> value."""
    if isinstance(node, Num):
        return node.value
    if isinstance(node, Var):
        return lookup(node.name, node.lag)
    if isinstance(node, Neg):
        return -evaluate(node.arg, lookup)
    if isinstance(node, Func):
        return FUNCS[node.name](evaluate(node.arg, lookup))
    a, b = evaluate(node.left, lookup), evaluate(node.right, lookup)
    if node.op == "+":
        return a + b
    if node.op == "-":
        return a - b
    if node.op == "*":
        return a * b
    if node.op == "/":
        return a / b
    if a < 0 and b != int(b):
        raise ValueError(f"negative number {a:g} raised to the non-integer power {b:g}")
    return a ** b


def to_str(node: Node) -> str:
    """Fully parenthesized text form (for messages and tests)."""
    if isinstance(node, Num):
        v = node.value
        return str(int(v)) if v == int(v) else repr(v)
    if isinstance(node, Var):
        return node.name if node.lag == 0 else f"{node.name}({node.lag:+d})"
    if isinstance(node, Neg):
        return f"(-{to_str(node.arg)})"
    if isinstance(node, Func):
        return f"{node.name}({to_str(node.arg)})"
    return f"({to_str(node.left)} {node.op} {to_str(node.right)})"
