#!/usr/bin/env python3
"""Check that every relative link/href/src in .html and .md files resolves to a real file."""
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git"}

HTML_LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')
MD_LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')


def is_external(link):
    return link.startswith(("http://", "https://", "mailto:", "//", "#"))


def check_file(path, pattern):
    problems = []
    text = path.read_text(errors="ignore")
    for match in pattern.finditer(text):
        link = match.group(1)
        if is_external(link):
            continue
        target = link.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        target = urllib.parse.unquote(target)
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            problems.append(f"{path.relative_to(ROOT)} -> {link}")
    return problems


def main():
    problems = []
    for path in sorted(ROOT.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix == ".html":
            problems += check_file(path, HTML_LINK_RE)
        elif path.suffix == ".md":
            problems += check_file(path, MD_LINK_RE)

    if problems:
        print("Broken relative links found:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    print("OK: all relative links in .html and .md files resolve.")


if __name__ == "__main__":
    main()
