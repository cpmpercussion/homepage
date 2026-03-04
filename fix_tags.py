#!/usr/bin/env python3
"""Fix Jekyll post tags.

Phase 1: Normalize all tag formats to YAML list (dash format).
         Handles: inline comma-separated, inline space-separated,
                  bracket arrays, empty arrays.
Phase 2: Lowercase all tags.

Usage:
  python3 fix_tags.py           # dry run – shows what would change
  python3 fix_tags.py --apply   # apply changes in place
"""

import re
import sys
from pathlib import Path

POSTS_DIR = Path("_posts")


def split_front_matter(content):
    """Return (fm_lines, body) or (None, content) if no front matter.

    fm_lines: list of strings (one per line, no trailing newline)
    body: everything from the closing '---' onward (starts with '\n---')
    """
    if not content.startswith("---"):
        return None, content
    close = content.find("\n---", 3)
    if close == -1:
        return None, content
    fm_text = content[4:close]   # skip opening '---\n'
    body = content[close:]        # '\n---\nrest...'
    return fm_text.split("\n"), body


def extract_tags(fm_lines):
    """Find and parse the tags section from front-matter lines.

    Returns (tags, start_idx, end_idx) – inclusive line indices.
    Returns (None, None, None) if no 'tags:' field.
    """
    for i, line in enumerate(fm_lines):
        if not re.match(r"^tags\s*:", line):
            continue

        inline = line.split(":", 1)[1].strip()

        if inline:
            # ── Inline formats ────────────────────────────────────────
            if inline.startswith("[") and inline.endswith("]"):
                # Bracket array: [tag1, tag2] or []
                inner = inline[1:-1].strip()
                tags = (
                    [t.strip().strip("'\"") for t in inner.split(",") if t.strip()]
                    if inner
                    else []
                )
            elif "," in inline:
                # Comma-separated: tag1, tag2, multi word tag
                tags = [t.strip().strip("'\"") for t in inline.split(",") if t.strip()]
            elif " " in inline:
                # Space-separated (no commas): each token is its own tag.
                # e.g. "performance installation bela pure-data magic-lantern"
                tags = inline.split()
            else:
                # Single tag, possibly quoted
                tags = [inline.strip("'\"")]
            return tags, i, i

        else:
            # ── Multi-line YAML list ───────────────────────────────────
            tags = []
            j = i + 1
            while j < len(fm_lines):
                m = re.match(r"^[ \t]*-[ \t]+(.*)", fm_lines[j])
                if m:
                    tags.append(m.group(1).strip().strip("'\""))
                    j += 1
                else:
                    break
            return tags, i, j - 1  # end_idx is last consumed line

    return None, None, None


def format_tags(tags):
    """Return YAML list lines for a tag list."""
    if not tags:
        return ["tags:"]
    return ["tags:"] + [f"- {tag}" for tag in tags]


def process_file(filepath, apply=False):
    """Process one file.

    Returns (changed: bool, info: str | tuple).
    info is a human-readable string on no-change, or (old_tags, new_tags) on change.
    """
    content = filepath.read_text(encoding="utf-8")
    fm_lines, body = split_front_matter(content)
    if fm_lines is None:
        return False, "no front matter"

    tags, start, end = extract_tags(fm_lines)
    if tags is None:
        return False, "no tags field"

    # Lowercase + deduplicate (preserving order)
    seen = set()
    normalized = []
    for t in tags:
        lower = t.lower()
        if lower and lower not in seen:
            seen.add(lower)
            normalized.append(lower)
    new_tag_lines = format_tags(normalized)

    new_fm_lines = fm_lines[:start] + new_tag_lines + fm_lines[end + 1 :]
    new_content = "---\n" + "\n".join(new_fm_lines) + body

    if new_content == content:
        return False, "no change"

    if apply:
        filepath.write_text(new_content, encoding="utf-8")

    return True, (tags, normalized)


def main():
    apply = "--apply" in sys.argv
    mode = "APPLYING" if apply else "DRY RUN (pass --apply to write changes)"
    print(f"=== Tag cleanup – {mode} ===\n")

    changed_files = []
    errors = []

    for md_file in sorted(POSTS_DIR.glob("*.md")):
        ok, result = process_file(md_file, apply=apply)
        if ok:
            old_tags, new_tags = result
            changed_files.append(md_file.name)
            print(f"  {md_file.name}")
            if old_tags != new_tags:
                added = set(new_tags) - set(old_tags)
                removed = set(old_tags) - set(new_tags)
                if removed or added:
                    print(f"    - removed: {sorted(removed)}")
                    print(f"    + added:   {sorted(added)}")
            # Show format change even when tag content is identical
            else:
                print(f"    (format fix, tags unchanged: {new_tags})")
        elif result not in ("no change", "no tags field", "no front matter"):
            errors.append((md_file.name, result))

    print(f"\n{'Changed' if apply else 'Would change'} {len(changed_files)} file(s).")
    if not apply and changed_files:
        print("Run with --apply to write changes.")
    for fname, err in errors:
        print(f"ERROR: {fname}: {err}")


if __name__ == "__main__":
    main()
