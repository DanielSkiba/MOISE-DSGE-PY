"""Parse MOISE agent-edition Markdown into math blocks.

A block is a metadata comment line followed (after an optional bold title line and blank
lines) by exactly one $$ ... $$ display:

    <!-- kind: eq; id: 229; section: D.4; page: 114; pdf_page: 120 -->
    **(229) Title**

    $$
    ... latex ...
    \\tag{229}
    $$
"""
import re

META_RE = re.compile(r"^<!--\s*kind:\s*(?P<body>.*?)\s*-->\s*$")


def parse_meta(line):
    m = META_RE.match(line.strip())
    if not m:
        return None
    meta = {}
    for part in ("kind: " + m.group("body")).split(";"):
        if ":" not in part:
            continue
        k, v = part.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta


def parse_blocks(text):
    """Return (blocks, problems). Each block: dict(meta..., title, latex, line)."""
    lines = text.split("\n")
    blocks, problems = [], []
    i, n = 0, len(lines)
    pending = None
    while i < n:
        line = lines[i]
        s = line.strip()
        meta = parse_meta(s) if s.startswith("<!--") else None
        if s.startswith("<!--") and "kind:" in s and meta is None:
            problems.append(f"line {i+1}: malformed metadata comment: {s[:80]}")
        if meta is not None:
            if pending is not None:
                problems.append(f"line {pending['line']}: metadata without a $$ block (id {pending.get('id')})")
            pending = dict(meta)
            pending["line"] = i + 1
            pending["title"] = ""
            i += 1
            continue
        if s == "$$":
            j = i + 1
            while j < n and lines[j].strip() != "$$":
                j += 1
            if j >= n:
                problems.append(f"line {i+1}: unclosed $$ block")
                break
            latex = "\n".join(lines[i + 1:j]).strip()
            if pending is None:
                problems.append(f"line {i+1}: $$ block without a metadata line")
            else:
                pending["latex"] = latex
                blocks.append(pending)
                pending = None
            i = j + 1
            continue
        if s.startswith("$$") and s != "$$":
            problems.append(f"line {i+1}: put $$ on its own line (found: {s[:60]})")
        if pending is not None and s.startswith("**") and not pending["title"]:
            pending["title"] = s.strip("*").strip()
        i += 1
    if pending is not None:
        problems.append(f"line {pending['line']}: metadata without a $$ block (id {pending.get('id')})")
    return blocks, problems


def eq_number(block):
    """Numeric part of an eq id ('229' -> 229, '32a' -> 32)."""
    m = re.match(r"(\d+)", block.get("id", ""))
    return int(m.group(1)) if m else None
