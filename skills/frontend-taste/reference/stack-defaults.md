# Stack Defaults & Full Design-System Map

Load this once you know whether the brief calls for a real design system or a custom aesthetic build (see SKILL.md section 3).

## Design-system map

| Brief reads as… | Reach for | Why |
|---|---|---|
| Enterprise SaaS / dashboards, Microsoft-flavored | `@fluentui/react-components` | Official Fluent UI tokens + accessibility built in |
| Material-flavored consumer product | `@material/web` + Material 3 tokens | Official, themeable via Material Theming |
| B2B enterprise analytics, IBM-flavored | `@carbon/react` + `@carbon/styles` | Mature data-density patterns, official |
| Shopify admin surfaces | Polaris (React or web components) | Required for Shopify app UI |
| Atlassian/Jira-style product | `@atlaskit/*` + `@atlaskit/tokens` | Official Atlassian design system |
| GitHub-style dev tool or community page | `@primer/css` / `@primer/react-brand` | Official Primer; Brand variant for marketing pages |
| UK public-sector service | `govuk-frontend` | Often a regulatory expectation, not a style choice |
| US public-sector / trust-first | `uswds` | Same reasoning |
| Fast local-business MVP | Bootstrap 5.3 | Boring on purpose, ships fast |
| Modern accessible foundation, no brand pull yet | `@radix-ui/themes` | Solid primitives with a themeable layer |
| Modern SaaS, want to own the components | shadcn/ui (`npx shadcn@latest add ...`) | You own the code; never ship it unstyled/default |
| Tailwind-based modern SaaS or AI product marketing | Tailwind v4 utilities + `dark:` variant | Default lane for indie/small-team builds |

**Rules of thumb:** if a brief clearly matches a row above, install and use the *official* package rather than recreating its look by hand, and don't import a system's tokens only to override most of them. Stick to one system per project — mixing component libraries from two different design systems in one tree reads as inconsistent even when each piece looks fine alone.

## When it's an aesthetic, not a system

There's no official package for these — build with native CSS/Tailwind and be explicit in comments about what's borrowed inspiration versus vendor-official material:

| Aesthetic | Honest implementation |
|---|---|
| Glassmorphism | `backdrop-filter` + layered borders/highlights; provide a solid-fill fallback for `prefers-reduced-transparency` |
| Bento-style tile grids | CSS Grid with mixed cell sizes — no library owns this |
| Brutalism | Native CSS, monospace, raw borders, no library |
| Editorial/magazine | Serif type, asymmetric grid, generous whitespace |
| Dark tech / terminal | Monospace + accent color, terminal motifs |
| Aurora/mesh gradients | Layered SVG or radial gradients |
| Kinetic typography | Native CSS animation, scroll-driven animation, or GSAP for hijack-scroll sequences |
| "Liquid glass" web approximations | Apple's real Liquid Glass is Apple-platform-only. A web version is an approximation via `backdrop-filter` + layered highlights — label it as an approximation, not the real material |

## Default technical stack (when no system dictates otherwise)

- **Framework:** React/Next.js, defaulting to Server Components. Anything using animation libraries, scroll listeners, or pointer-driven physics must be an isolated client-component leaf (`'use client'`) — server components stay static.
- **Styling:** Tailwind v4 by default (v3 only if an existing project already depends on it).
- **Animation library:** Motion (formerly Framer Motion), imported as `motion/react`.
- **State:** local `useState`/`useReducer` for isolated UI; a global store (Zustand/Jotai/context) only to avoid deep prop drilling. Never track continuous, high-frequency values (scroll position, pointer coordinates, drag physics) in `useState` — it re-renders the tree on every tick. Use the animation library's motion-value primitives instead.
- **Icons:** pick one icon family for the whole project (Phosphor, Hugeicons, Radix Icons, Tabler are all reasonable defaults) and never hand-draw SVG icon paths from scratch — install a second library if one glyph is missing rather than drawing it.
- **Fonts:** self-host via `next/font` or `@font-face` with `font-display: swap`. Don't link Google Fonts directly in production.
- **Breakpoints:** standard Tailwind scale (`sm 640 / md 768 / lg 1024 / xl 1280 / 2xl 1536`).
- **Full-height sections:** use `min-h-[100dvh]`, never `h-screen` — avoids mobile browser chrome causing layout jumps.
- **Multi-column layout:** prefer CSS Grid over flexbox percentage math for anything beyond a simple row.
- **Before importing any third-party package:** check it's actually in `package.json` first; never assume a library is already installed.
