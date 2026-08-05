#!/usr/bin/env python3
"""
Validate every skills/*/SKILL.md in this repo.


Checks, per skill:
  - SKILL.md exists and is valid UTF-8
  - Frontmatter is present and parses as YAML
  - Required keys (name, description, license) exist and are non-empty
  - `name` matches the containing folder name
  - No mojibake artifacts (the encoding corruption this repo hit once already)
  - Every `reference/...md` path referenced in the body actually exists on disk

Exit code is non-zero if any skill fails. Run locally with:
    python3 scripts/validate_skills.py
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: run `pip install pyyaml` first.")

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
REQUIRED_KEYS = ("name", "description", "license")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
REFERENCE_LINK_RE = re.compile(r"`(reference/[\w./-]+\.md)`")
MOJIBAKE_CHARS = ("â", "Ã¢", "â€", "Â")


def check_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    try:
        text = skill_md.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        return [f"{skill_dir.name}/SKILL.md: not valid UTF-8 ({e})"]

    for bad_char in MOJIBAKE_CHARS:
        if bad_char in text:
            errors.append(
                f"{skill_dir.name}/SKILL.md: found '{bad_char}' — looks like "
                f"mojibake/encoding corruption, not an intentional character"
            )

    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"{skill_dir.name}/SKILL.md: no --- frontmatter block found")
        return errors

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{skill_dir.name}/SKILL.md: frontmatter is not valid YAML ({e})")
        return errors

    if not isinstance(frontmatter, dict):
        errors.append(f"{skill_dir.name}/SKILL.md: frontmatter did not parse to a mapping")
        return errors

    for key in REQUIRED_KEYS:
        if not frontmatter.get(key):
            errors.append(f"{skill_dir.name}/SKILL.md: missing or empty required key '{key}'")

    if frontmatter.get("name") and frontmatter["name"] != skill_dir.name:
        errors.append(
            f"{skill_dir.name}/SKILL.md: frontmatter name '{frontmatter['name']}' "
            f"does not match folder name '{skill_dir.name}'"
        )

    for ref in REFERENCE_LINK_RE.findall(text):
        if not (skill_dir / ref).exists():
            errors.append(f"{skill_dir.name}/SKILL.md: references '{ref}' but that file does not exist")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        sys.exit(f"No skills/ directory found at {SKILLS_DIR}")

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        sys.exit("No skills found under skills/")

    all_errors = []
    for skill_dir in skill_dirs:
        errors = check_skill(skill_dir)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"OK   {skill_dir.name}")

    for err in all_errors:
        print(f"FAIL {err}")

    print(f"\n{len(skill_dirs)} skill(s) checked, {len(all_errors)} error(s).")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
