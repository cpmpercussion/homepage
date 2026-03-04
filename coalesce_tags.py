#!/usr/bin/env python3
"""Phase 3: Coalesce near-duplicate and related tags.

Applies a remapping table: old_tag -> canonical_tag.
If a post gains a canonical tag it already has, the old one is just removed (no duplicate).

Usage:
  python3 coalesce_tags.py           # dry run
  python3 coalesce_tags.py --apply   # apply changes
"""

import re
import sys
from pathlib import Path

POSTS_DIR = Path("_posts")

# Maps old_tag -> canonical_tag (all lowercase)
REMAP = {
    # Format duplicates
    "computer-music":       "computer music",
    "strikeonstage":        "strike on stage",
    "pure-data":            "pure data",
    "tutorials":            "tutorial",
    # Abbreviations
    "lmtd":                 "last man to die",
    "lmtd2010":             "last man to die",
    "pd":                   "pure data",
    # Semantic consolidation
    "concert":              "performance",
    "show":                 "performance",
    "gig":                  "performance",
    "vital lmtd":           "last man to die",
    "ai":                   "machine-learning",
    "artificial-intelligence": "machine-learning",
}


def get_tags_block_bounds(fm_lines):
    """Find (start_idx, end_idx) of the tags section in front-matter lines."""
    for i, line in enumerate(fm_lines):
        if re.match(r"^tags\s*:", line):
            j = i + 1
            while j < len(fm_lines) and re.match(r"^[ \t]*-[ \t]", fm_lines[j]):
                j += 1
            return i, j - 1
    return None, None


def process_file(filepath, apply=False):
    content = filepath.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return False, "no front matter"
    close = content.find("\n---", 3)
    if close == -1:
        return False, "no closing ---"

    fm_text = content[4:close]
    body = content[close:]
    fm_lines = fm_text.split("\n")

    start, end = get_tags_block_bounds(fm_lines)
    if start is None:
        return False, "no tags field"

    # Parse current tags
    old_tags = []
    for line in fm_lines[start + 1 : end + 1]:
        m = re.match(r"^[ \t]*-[ \t]+(.*)", line)
        if m:
            old_tags.append(m.group(1).strip())

    # Apply remapping, preserving order, deduplicating
    seen = set()
    new_tags = []
    for tag in old_tags:
        canonical = REMAP.get(tag, tag)
        if canonical not in seen:
            seen.add(canonical)
            new_tags.append(canonical)

    if new_tags == old_tags:
        return False, "no change"

    # Rebuild front matter
    new_tag_lines = ["tags:"] + [f"- {t}" for t in new_tags]
    new_fm_lines = fm_lines[:start] + new_tag_lines + fm_lines[end + 1 :]
    new_content = "---\n" + "\n".join(new_fm_lines) + body

    if apply:
        filepath.write_text(new_content, encoding="utf-8")

    return True, (old_tags, new_tags)


def main():
    apply = "--apply" in sys.argv
    mode = "APPLYING" if apply else "DRY RUN (pass --apply to write changes)"
    print(f"=== Tag coalescing – {mode} ===\n")

    changed_files = []

    for md_file in sorted(POSTS_DIR.glob("*.md")):
        ok, result = process_file(md_file, apply=apply)
        if ok:
            old_tags, new_tags = result
            changed_files.append(md_file.name)
            removed = [t for t in old_tags if t not in new_tags]
            added   = [t for t in new_tags if t not in old_tags]
            print(f"  {md_file.name}")
            for r in removed:
                canon = REMAP.get(r, r)
                print(f"    {r!r} -> {canon!r}")

    print(f"\n{'Changed' if apply else 'Would change'} {len(changed_files)} file(s).")
    if not apply and changed_files:
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
