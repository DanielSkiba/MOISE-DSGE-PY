#!/usr/bin/env python3
"""Check (and optionally refresh) the MOISE agent edition in docs/paper/.

Usage (from the repo root):
    python tools/paper/check_paper.py              # structural checks + code-form sync check
    python tools/paper/check_paper.py --compile    # also compile every math block with pdflatex
    python tools/paper/check_paper.py --fix-code   # rewrite the embedded code forms from the LaTeX
    python tools/paper/check_paper.py --write-json # regenerate docs/paper/equations.json
    python tools/paper/check_paper.py --write-combined  # regenerate docs/paper/MOISE_agent_edition.md

Checks:
  * every math block has valid metadata (kind, id, section, page, pdf_page = page + 6)
  * block ids are unique; numbered equations (1)-(331) each appear exactly once, in order
  * each numbered block's \\tag matches its id
  * in 10-log-linear-model.md, the "Code form" under each equation equals what
    latex2code.py produces from the LaTeX with the names in data/notation_codes.csv
    (so an edit to an equation cannot silently leave a stale code form)
Exit status 1 if anything fails.
"""
import csv, json, os, re, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks import parse_blocks                     # noqa: E402
from latex2code import to_code, ConvertError        # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(ROOT, "docs", "paper")
N_EQUATIONS = 331
CODE_FILE = "10-log-linear-model.md"
CODE_HEADER = "Code form (derived from the LaTeX above; LaTeX is authoritative):"


def section_files():
    return sorted(f for f in os.listdir(DOCS) if re.match(r"\d\d-.*\.md$", f))


def load_names():
    path = os.path.join(DOCS, "data", "notation_codes.csv")
    names = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names[row["latex_key"]] = row["code_name"]
    return names


def embedded_codeforms(text):
    """id -> (code, line index of the code line) for blocks followed by a code form."""
    lines = text.split("\n")
    out, cur = {}, None
    for i, line in enumerate(lines):
        m = re.match(r"^<!--\s*kind:\s*\w+;\s*id:\s*([^;]+);", line.strip())
        if m:
            cur = m.group(1).strip()
        if line.strip() == CODE_HEADER and cur is not None and i + 2 < len(lines) and lines[i + 1].startswith("```"):
            out[cur] = (lines[i + 2], i + 2)
    return out


def compile_block(latex):
    if not shutil.which("pdflatex"):
        return True, "pdflatex not installed (skipped)"
    d = tempfile.mkdtemp()
    try:
        with open(os.path.join(d, "x.tex"), "w") as f:
            f.write("\\documentclass[12pt]{article}\\usepackage{amsmath,amssymb}\\begin{document}\n"
                    "\\begin{equation*}\n" + latex + "\n\\end{equation*}\n\\end{document}\n")
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "x.tex"],
                           cwd=d, capture_output=True, text=True, timeout=120)
        return r.returncode == 0, "" if r.returncode == 0 else r.stdout[-400:]
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main():
    args = set(sys.argv[1:])
    errors, all_blocks = [], []
    for fname in section_files():
        text = open(os.path.join(DOCS, fname), encoding="utf-8").read()
        blocks, problems = parse_blocks(text)
        errors += [f"{fname}: {p}" for p in problems]
        for b in blocks:
            b["file"] = fname
            all_blocks.append(b)

    seen, numbered = {}, []
    for b in all_blocks:
        tag = f"{b['file']}:{b['line']} id {b.get('id')}"
        for field in ("kind", "id", "section", "page", "pdf_page"):
            if not b.get(field):
                errors.append(f"{tag}: missing '{field}'")
        try:
            if int(b["pdf_page"]) != int(b["page"]) + 6:
                errors.append(f"{tag}: pdf_page must equal page + 6")
        except (KeyError, ValueError):
            errors.append(f"{tag}: page/pdf_page not integers")
        if b.get("id") in seen:
            errors.append(f"{tag}: duplicate id (also {seen[b['id']]})")
        seen[b.get("id")] = tag
        if b.get("kind") == "eq":
            tags = re.findall(r"\\tag\{([^}]*)\}", b.get("latex", ""))
            if tags != [b.get("id")]:
                errors.append(f"{tag}: \\tag {tags} does not match id")
            m = re.match(r"(\d+)", b.get("id", ""))
            if m:
                numbered.append(int(m.group(1)))
    missing = sorted(set(range(1, N_EQUATIONS + 1)) - set(numbered))
    if missing:
        errors.append(f"numbered equations missing: {missing}")
    if numbered != sorted(numbered):
        errors.append("numbered equations are not in increasing order across files")

    # code forms
    code_path = os.path.join(DOCS, CODE_FILE)
    text = open(code_path, encoding="utf-8").read()
    names = load_names()
    embedded = embedded_codeforms(text)
    lines = text.split("\n")
    n_ok = n_fixed = 0
    for b in [x for x in all_blocks if x["file"] == CODE_FILE]:
        try:
            code, unknown = to_code(b["latex"], names)
        except ConvertError as e:
            if b["id"] in embedded:
                errors.append(f"{CODE_FILE} id {b['id']}: has a code form but the LaTeX no longer converts ({e})")
            continue
        if unknown:
            errors.append(f"{CODE_FILE} id {b['id']}: symbols missing from data/notation_codes.csv: {unknown}")
            continue
        if b["id"] not in embedded:
            if b.get("kind") != "inline":
                errors.append(f"{CODE_FILE} id {b['id']}: no embedded code form")
            continue
        old, idx = embedded[b["id"]]
        if old == code:
            n_ok += 1
        elif "--fix-code" in args:
            lines[idx] = code
            n_fixed += 1
        else:
            errors.append(f"{CODE_FILE} id {b['id']}: embedded code form is stale\n    file:      {old}\n    from LaTeX: {code}")
    if n_fixed:
        open(code_path, "w", encoding="utf-8").write("\n".join(lines))

    if "--compile" in args:
        for b in all_blocks:
            ok, msg = compile_block(b["latex"])
            if not ok:
                errors.append(f"{b['file']} id {b['id']}: LaTeX does not compile: {msg}")

    if "--write-json" in args:
        cf = embedded_codeforms(open(code_path, encoding="utf-8").read())
        eqs = [{k: b.get(k) for k in ("kind", "id", "section", "page", "pdf_page", "title", "latex", "file")}
               | {"code": cf[b["id"]][0] if b["id"] in cf and b["file"] == CODE_FILE else None}
               for b in all_blocks]
        with open(os.path.join(DOCS, "equations.json"), "w", encoding="utf-8") as f:
            json.dump(eqs, f, ensure_ascii=False, indent=1)

    if "--write-combined" in args:
        parts = ["# MOISE — agent edition (all files in one)\n",
                 "Generated by concatenating `00-overview.md` … `10-log-linear-model.md`. Edit those files, not this one.\n"]
        for fname in section_files():
            parts.append(f"\n\n<!-- ===== {fname} ===== -->\n\n")
            parts.append(open(os.path.join(DOCS, fname), encoding="utf-8").read())
        with open(os.path.join(DOCS, "MOISE_agent_edition.md"), "w", encoding="utf-8") as f:
            f.write("".join(parts))

    print(f"{len(all_blocks)} math blocks in {len(section_files())} files; "
          f"{len(set(numbered))} numbered equations; code forms in sync: {n_ok}"
          + (f"; rewritten: {n_fixed}" if n_fixed else ""))
    for e in errors:
        print("ERROR:", e)
    print("RESULT:", "OK" if not errors else f"{len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
