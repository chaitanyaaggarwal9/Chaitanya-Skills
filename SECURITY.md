# Security Policy

## Scope

This repository contains [Claude Code](https://claude.com/claude-code) skills — Markdown instruction files (`SKILL.md`) that Claude reads and follows, not executable software. There are no versioned releases to track and no traditional runtime to patch, but a skill's instructions still run with whatever permissions the invoking Claude Code session has, so a bad instruction is a real risk, not just a documentation error.

Treat as a security issue anything where following a skill as written would:

- Cause Claude to take a destructive or hard-to-reverse action without asking (deleting data, force-pushing, exposing secrets, running unreviewed shell commands).
- Contain instructions designed to override the user's intent, exfiltrate data, or be triggered by content the user didn't write (a prompt-injection vector embedded in a skill).
- Contain obfuscated, hidden, or misleading instructions — anything a reviewer skimming the rendered Markdown wouldn't actually see.

A skill that's simply low-quality, out of date, or badly written is a normal bug — open a regular [issue](../../issues) for that instead.

## Supported Versions

There are no version branches. Only the latest commit on `main` is supported; fixes land there directly.

## Reporting a Vulnerability

Please **do not** open a public issue for a security concern. Use GitHub's private reporting instead:

1. Go to the [Security tab](../../security) of this repository.
2. Click **Report a vulnerability** to open a private advisory.

Include which skill file is affected, the exact instruction text you're concerned about, and the scenario where following it would cause harm.

You should get an initial response within a few days. If the issue is confirmed, the fix will be a direct edit to the affected `SKILL.md` — there's no embargo/release process to coordinate, so a fix ships as soon as it's ready and merged.
