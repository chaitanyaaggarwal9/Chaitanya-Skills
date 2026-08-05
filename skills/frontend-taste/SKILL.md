---
# Must match the folder name exactly
name: frontend-taste
# Matched against the live request — the highest-leverage line in the file
description: Use when designing, building, redesigning, or reviewing frontend visual work — landing pages, portfolios, marketing sites, dashboards, product UI, components, or animations. Covers reading a design brief correctly, picking a real design system vs. building a custom aesthetic, avoiding generic "AI-slop" defaults, animation decision-making, and a pre-ship quality pass. Trigger this even when the user just asks for "a landing page" or "make this look better" without naming design taste explicitly.
# License this skill's own text is released under — the adapted sources
# in ## Credits below each carry their own original license
license: MIT
---

# Frontend Taste

A workflow for shipping frontend work that reads as considered rather than templated: read the brief correctly, commit to a direction, build against real constraints, then run one disciplined quality pass before calling it done.

## 1. Read the brief before touching code

Most generic-looking output happens because the brief never got read carefully — the model jumped straight to a default aesthetic. Before writing anything, work out:

- **What kind of surface is this?** Landing page (SaaS / consumer / agency), portfolio, product dashboard, docs, redesign. The kind of surface determines what "good" even means here — a dashboard is judged on scanability, a portfolio on point of view.
- **Who is looking at it, and why?** A procurement panel, a design-conscious consumer, a recruiter skimming in ten seconds. The audience picks the aesthetic — not your personal preference.
- **What vibe words, references, or existing brand assets did the user give you?** URLs, screenshots, named competitors, an existing logo/palette/type system. Treat existing brand material as required starting material, not optional flavor — especially on a redesign.
- **Are there constraints that override aesthetics?** Accessibility-critical audiences, regulated industries, public-sector, trust-first commerce. These beat vibe every time.

State your read in one line before generating anything: *"Reading this as: [surface] for [audience], with a [vibe] direction."* If the brief genuinely could go two very different ways, ask exactly one clarifying question — never a list of them. If you can confidently infer it, don't ask, just state the read and move.

**Watch for the default-aesthetic trap.** Left alone, generic output converges on the same handful of moves: purple gradient hero over a dark mesh background, three identical feature cards, glassmorphism applied for no reason, Inter set on slate-900, a kicker/eyebrow label above every heading, infinite looping micro-animations. None of these are wrong in principle — they're wrong as a *default*, reached for out of habit instead of decided on. If the brief doesn't specifically earn one of these, don't reach for it.

## 2. Set your direction, deliberately

Once you have the read, pick where this sits on three axes. These aren't a formula — they're a way to keep decisions consistent as you build instead of re-deciding taste on every section.

| Axis | Low end | High end |
|---|---|---|
| **Boldness** | Perfectly symmetric, restrained, quiet | Deliberately unconventional, expressive |
| **Motion** | Static, or near-static | Cinematic, physics-driven |
| **Density** | Airy, gallery-like spacing | Packed, cockpit-like information density |

Rough starting points by surface type — nudge from here based on the brief, don't treat these as fixed:

- SaaS landing, mainstream: moderate boldness, moderate motion, low-moderate density.
- Creative/agency landing or portfolio: high boldness, high motion, low density.
- Developer portfolio: moderate on all three — craft should show in restraint, not flash.
- Editorial/blog: low-moderate boldness and motion, low density, type does the work.
- Public-sector or trust-first: low boldness and motion, moderate-high density (people are scanning for facts, not being sold a vibe).
- Redesign that should preserve identity: match the existing levels, allow a small motion bump.
- Redesign that should overhaul: push boldness and motion up, keep density where it was — a redesign that also becomes harder to scan solved the wrong problem.

## 3. Choose a real design system honestly, don't fake one

Before writing custom CSS for something, check whether an official system already owns this territory. If it does, use the real package instead of hand-rolling an approximation of it — a Material-flavored product that isn't actually running Material tokens reads as almost-right, which is worse than clearly different.

- Enterprise/Microsoft-flavored → Fluent UI (`@fluentui/*`)
- Material/Google-flavored product → Material Web (`@material/web`) + Material 3 tokens
- Enterprise B2B/analytics, IBM-flavored → Carbon (`@carbon/react`)
- Government/public-sector → `govuk-frontend` (UK) or `uswds` (US) — often not optional, regulatorily expected
- Modern accessible React foundation, no strong brand pull → Radix Themes or shadcn/ui (own the code, easy to restyle)
- Fast, boring, ships today → Tailwind utilities, or Bootstrap for a quick local-business MVP

One system per project — don't blend Fluent components into a Material app, or shadcn into a Carbon one.

For aesthetics rather than systems (glassmorphism, bento grids, brutalism, editorial, dark-tech/hacker, kinetic type) — there usually isn't an official package. Build it with native CSS/Tailwind honestly, and say in comments what's borrowed inspiration versus vendor-official (e.g. Apple's "Liquid Glass" is Apple-platform-only; any web version is an approximation of the look, not the real thing — label it as such).

See `reference/stack-defaults.md` for a fuller system-selection table and default technical stack choices (framework, state management, icons, fonts, breakpoints) once you know which lane you're in.

## 4. Design the animation, don't just add it

Animation is judged on purpose and frequency, not on whether it exists. Before animating anything, check how often a person will see it:

| How often seen | What to do |
|---|---|
| Very frequent (keyboard shortcuts, palette toggles, tens+ times/day) | Don't animate it. Speed beats delight here. |
| Frequent (hovers, list navigation) | Keep it minimal or cut it |
| Occasional (modals, drawers, toasts) | Standard, purposeful animation is fine |
| Rare / first-time (onboarding, empty states, celebrations) | This is where delight earns its keep |

Every animation should have an answer to "why does this move": it shows a state change, indicates direction/continuity (a toast should exit the way it entered), gives feedback that input was received (a button compressing slightly on press), or explains a mechanism. An animation with no purpose beyond "it looked cool" is a good candidate to cut.

When reviewing existing animation code, present findings as a single markdown table, not prose or a before/after list:

| Before | After | Why |
|---|---|---|
| `transition: all 300ms` | `transition: transform 200ms ease-out` | Naming the exact property avoids animating things that shouldn't move |
| `transform: scale(0)` on entrance | `scale(0.95)` + fade | Nothing in the physical world appears out of zero size |
| `ease-in` on an opening panel | `ease-out` | `ease-in` reads as sluggish; `ease-out` gives immediate feedback |

## 5. Craft-floor pass before calling it done

Run this once, as a batched check across desktop and mobile together — not as an open-ended loop of "let me check one more thing." Fix everything it surfaces in one pass, confirm with at most one more look, then stop.

**Verify:**
- Contrast: body/placeholder text ≥ 4.5:1, large text ≥ 3:1. Tint secondary text from the surface's own hue rather than defaulting to gray.
- Depth: shadows have an offset and soft blur — a flat colored halo at zero offset is decoration, not depth.
- Spacing: tight within a group, generous between groups; more space above a heading than below it.
- Type: body measure around 65–75 characters per line, headings show a clear scale/weight step, nothing overflows at any breakpoint with the *real* copy (not lorem ipsum).
- Motion: one authored, purposeful moment — not the same entrance animation copy-pasted onto every section, and not motion scattered without a plan.
- States: hover, disabled, loading, empty, and error states all exist and use the product's own language — an error names the problem and the way out, a control names its own action.
- Coverage: every requirement in the brief is present and findable within seconds of looking.

**Refuse by default (unless the brief specifically earns it):**
- Same-size icon+heading+text cards as the whole page structure — the laziest possible layout, and nested cards are always a mistake.
- A kicker/eyebrow label above a heading — delete it and let the heading carry its own weight.
- Gradient text as emphasis — use weight or size instead.
- A colored border-left accent above 1px on cards/alerts as a decoration reflex.
- Sparklines, progress rings, or soft-shadowed rounded rectangles standing in for actual content.
- Emoji or unicode glyphs used as an icon system — use a real icon library or authored SVG, one consistent stroke weight throughout.
- Picking light/dark mode by category habit rather than by the actual use scene — who's using this, where, under what light.

## 6. Why the invisible details matter

The details in sections 4–5 mostly aren't things a user will consciously notice — that's the point. When an interface behaves exactly the way someone assumed it would, they don't think about it at all; they just keep going. That compounding of small, correct decisions is what separates software that feels considered from software that merely functions. In a landscape where most software works fine, this is often the actual differentiator, not the feature list.

---

## Credits

This skill synthesizes ideas and structure from three open-source Claude skill projects, each used under its own license:

- **taste-skill** (Leonxlnx) — brief-inference, the three-axis direction system, and the design-system-vs-aesthetic honesty rule. MIT License.
- **impeccable** (Paul Bakaus) — the craft-floor verify/refuse checklist structure and mode-based framing. Apache License 2.0.
- **Emil Kowalski's design-eng skills** — the animation decision framework, before/after review table format, and the "unseen details compound" philosophy. MIT License. See [animations.dev](https://animations.dev/) for the full course this draws from.

If you redistribute this skill further, keep this credits section intact.
