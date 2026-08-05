# Chaitanya-Skills

[![Validate skills](https://github.com/chaitanyaaggarwal9/Chaitanya-Skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/chaitanyaaggarwal9/Chaitanya-Skills/actions/workflows/validate-skills.yml)

A collection of [Claude Code](https://claude.com/claude-code) Skills — packaged instructions that give Claude a repeatable workflow for a specific kind of task, instead of relying on it to reinvent an approach every time.

## What's in here

| Skill | What it does |
|---|---|
| [`coding-discipline`](skills/coding-discipline/SKILL.md) | Behavioral guardrails for writing, reviewing, or refactoring code — surface assumptions instead of guessing, default to the smallest working solution, make surgical edits, define "done" before starting. |
| [`frontend-taste`](skills/frontend-taste/SKILL.md) | A workflow for frontend visual work — landing pages, dashboards, portfolios, components — covering how to read a design brief, when to reach for a real design system vs. a custom aesthetic, how to make animation decisions, and a pre-ship quality checklist. |
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | Guidance for writing a new Claude Code skill well — deciding whether something should be a skill at all, writing a description that actually triggers, keeping `SKILL.md` short with reference files for overflow, and a pre-ship hygiene pass. |

## What a skill is

Each skill is a folder containing a `SKILL.md` file with YAML frontmatter and a Markdown body:

```markdown
---
name: skill-name
description: When Claude should reach for this skill, written so it matches how a user would phrase the request.
license: MIT
---

# Skill Name

The actual instructions Claude follows once this skill is triggered.
```

- `name` — the skill's identifier, matches the folder name.
- `description` — read by Claude to decide relevance; the more specific this is about *when* to trigger, the better.
- `license` — the license this particular skill's content is released under (can differ per skill — see [License](#license)).

A skill can also ship extra reference material it only loads when needed, so the main `SKILL.md` stays short. `frontend-taste` does this:

```
skills/frontend-taste/
├── SKILL.md
└── reference/
    └── stack-defaults.md   # loaded on demand, not part of every trigger
```

## How to use these skills

Claude Code looks for skills in two places:

- **Per-project**: `.claude/skills/<skill-name>/` inside a specific project — only active in that project.
- **Global**: `~/.claude/skills/<skill-name>/` — active in every project for your user.

To install a skill from this repo, copy or symlink its folder into one of those locations.

**Global install (recommended for these two — they're general-purpose, not project-specific):**

```bash
mkdir -p ~/.claude/skills
ln -s /path/to/Chaitanya-Skills/skills/coding-discipline ~/.claude/skills/coding-discipline
ln -s /path/to/Chaitanya-Skills/skills/frontend-taste ~/.claude/skills/frontend-taste
```

**Per-project install:**

```bash
mkdir -p /path/to/your-project/.claude/skills
cp -r /path/to/Chaitanya-Skills/skills/coding-discipline /path/to/your-project/.claude/skills/
cp -r /path/to/Chaitanya-Skills/skills/frontend-taste /path/to/your-project/.claude/skills/
```

Symlinking (rather than copying) means `git pull` in this repo updates the skill everywhere it's linked, without reinstalling.

Once installed, restart Claude Code (or start a new session). The skill then activates one of two ways:

- **Automatically** — Claude reads the `description` field and triggers the skill when a request matches, with no explicit invocation needed.
- **Explicitly** — type `/<skill-name>` (e.g. `/coding-discipline`) to invoke it directly.

## Validating a skill

Every `SKILL.md` in this repo is checked by [`scripts/validate_skills.py`](scripts/validate_skills.py) — it confirms the frontmatter parses, `name`/`description`/`license` are all present, `name` matches the folder, there's no mojibake/encoding corruption, and every `reference/*.md` path a skill links to actually exists. CI runs it on every push and PR that touches `skills/**`; run it locally with:

```bash
pip install pyyaml
python3 scripts/validate_skills.py
```

## Contributing a new skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar, the expected folder structure, and the steps to add one.

## License

[MIT](LICENSE) for the repository and all skills currently in it. A future skill could in principle declare a different license in its own `SKILL.md` frontmatter — that field always takes precedence over this file for that skill's content — but as of now every skill here is MIT. Where a skill adapts someone else's published work, the source and its original license are credited in that skill's `## Credits` section (see `frontend-taste/SKILL.md`).
