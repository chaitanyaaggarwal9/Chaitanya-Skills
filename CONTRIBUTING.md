# Contributing a skill

## The bar

A skill earns a place in this repo if it's:

- **Small** — a focused workflow or checklist, not a general-purpose prompt.
- **Checkable** — someone can look at the output and tell whether the skill was actually followed.
- **Honest about trade-offs** — it says what it refuses to do by default and why, not just what it does.
- **Specific about when it triggers** — the `description` field should read like the request that should invoke it, not a vague category label.

If you're unsure whether something belongs, that uncertainty is usually the answer: keep it out until it's been used for real and proven itself.

## Structure

```
skills/<skill-name>/
├── SKILL.md              # required
└── reference/             # optional — only if SKILL.md would otherwise get long
    └── *.md
```

```markdown
---
# Must match the folder name exactly
name: skill-name
# Matched against the live request — the highest-leverage line in the file
description: When Claude should reach for this — written the way a user would phrase the request.
# License this skill's content is released under
license: MIT
---

# Skill Name

Instructions.
```

Keep `SKILL.md` itself short. If a section would only be needed once the skill has already decided which path it's on (e.g. a big reference table used only after a certain branch), move it to `reference/*.md` and link to it with a backtick-quoted path like `` `reference/stack-defaults.md` `` — the validator checks that path actually resolves.

## Steps

1. Create `skills/<skill-name>/SKILL.md` following the structure above.
2. Run the validator locally:
   ```bash
   pip install pyyaml
   python3 scripts/validate_skills.py
   ```
   It checks: frontmatter parses as YAML, `name`/`description`/`license` are all present, `name` matches the folder, no mojibake/encoding corruption in the file, and every `reference/*.md` path mentioned actually exists.
3. If the skill is adapted from someone else's published work, add a `## Credits` section at the bottom of `SKILL.md` naming the source and its license (see `frontend-taste/SKILL.md` for the pattern), and set your own `license` field accordingly.
4. Add a row for it to the table in [README.md](README.md).
5. Before opening a PR, actually run the skill against a real task in Claude Code. These are workflows and checklists — the fastest way to check one is broken is to use it once.

CI runs the same validator on every push and PR that touches `skills/**`.
