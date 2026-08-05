---
name: skill-authoring
description: Use when writing a new Claude Code skill (a SKILL.md file), turning a repeated prompt or workflow into one, or reviewing/improving an existing skill's frontmatter, description, or structure. Triggers on requests like "write a skill for X", "turn this into a skill", "create a SKILL.md", or "why isn't my skill triggering".
license: MIT
---

# Skill Authoring

A skill is only as good as whether it triggers at the right time and whether someone can tell it was followed. Most bad skills fail before a single line of instruction is written — at the "should this exist" and "will this description ever match a real request" stages.

## 1. Decide it should be a skill before writing one

Not every repeated task deserves a skill. A skill earns its place when it's a **recurring, recognizable request** with a **repeatable process or judgment call** behind it — not a one-off task, and not pure reference information with no decisions in it.

- One-off task → just do it, don't package it.
- Static reference info with no judgment involved (a list of API keys, a glossary) → a doc, not a skill.
- A recognizable request pattern where the *process* matters more than the output ("make this look better", "review this diff", "fix this bug") → a skill.

Before writing anything, check whether an existing skill already covers this ground — including built-in ones the harness ships. Two skills with overlapping triggers don't add coverage, they add ambiguity about which one fires.

## 2. The frontmatter is the product

```markdown
---
name: skill-name
description: When to use this — written so it matches how a user would actually phrase the request.
license: MIT
---
```

- `name` — kebab-case, must match the containing folder exactly.
- `description` — this is what gets matched against a live request. It is the single highest-leverage sentence in the file.
- `license` — state one. If the skill adapts someone else's published skill or write-up, credit the source and its license in a `## Credits` section at the bottom, and set `license` to reflect what you're actually allowed to redistribute.

## 3. Write the description like the request, not like a label

| Weak (label-shaped) | Strong (request-shaped) |
|---|---|
| "Helps with code review" | "Use when reviewing a diff or PR for correctness, style, or missed edge cases before merging." |
| "Frontend skill" | "Use when designing, building, or redesigning a landing page, dashboard, or component — even if the user just says 'make this look better'." |
| "Debugging helper" | "Use when a bug report, stack trace, or failing test needs root-causing before a fix is attempted." |

A label describes the *topic*. A request-shaped description describes the *trigger* — include the phrasing a user would actually type, including the vague/implicit ways they'd ask without naming the skill. Too narrow and it never fires; too broad ("use for any coding task") and it fires on everything, which is functionally the same as not triggering at all.

## 4. Keep SKILL.md short; push overflow to reference files

The body should read in under a couple of minutes. If a section is only needed after a specific branch has already been decided (a big lookup table, a stack-specific reference), move it out:

```
skills/skill-name/
├── SKILL.md
└── reference/
    └── <topic>.md   # linked from SKILL.md, loaded only when that branch is reached
```

Link it with a literal path a validator can check (see `frontend-taste/reference/stack-defaults.md` for a real example of the pattern). Never leave a reference to a file that doesn't exist, and never create a reference file nothing links to.

## 5. Write instructions as checklists and tables, not prose

The two things that make a skill *checkable* — someone can tell whether it was followed:

- **Checklists** for anything that should be verified before calling something done.
- **Before/after tables** for anything that's a judgment call rather than a binary rule (see the table in section 3, or `frontend-taste`'s animation review table).
- **A refuse list** — name the defaults the skill should *not* reach for, and why. A skill that only says what to do, never what to avoid, tends to get followed selectively.

## 6. Hygiene pass before shipping

- Real UTF-8 punctuation (em dash `—`, arrows `→`), typed or pasted cleanly — not the single mangled Latin-1 character that em dashes and arrows both corrupt into after a lossy copy-paste. If this repo has `scripts/validate_skills.py`, run it.
- `name` matches the folder name exactly.
- Every `reference/*.md` path mentioned actually resolves.
- No overlap with an existing skill's trigger — if two skills could plausibly both fire on the same request, either merge them or narrow both descriptions.
- Test it: invoke the skill against a real request and check the output actually reflects the instructions, not just that the file parses.

## 7. Why this matters more for skills than for most code

A skill's only interface to the world is its `description` and its instructions — there's no compiler to catch a description that will never match, no test suite to catch instructions too vague to change behavior. The authoring discipline *is* the quality bar; nothing downstream checks it for you.
