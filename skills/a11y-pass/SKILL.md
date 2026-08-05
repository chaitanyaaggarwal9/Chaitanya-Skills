---
name: a11y-pass
description: Use when building or reviewing a web UI for accessibility — keyboard navigation, screen reader semantics, focus management, or an explicit "accessibility pass"/"a11y review" request. Complements frontend-taste's craft-floor contrast check with the parts a purely visual review misses.
license: MIT
---

# Accessibility Pass

Most accessibility failures are invisible to a sighted reviewer clicking through with a mouse — that's exactly why they need a dedicated pass instead of getting folded into a general visual review.

## 1. Keyboard first

Everything a mouse can do, a keyboard must be able to do too:

- Tab order follows visual/logical reading order, not DOM-insertion accident.
- No keyboard traps — a user can always tab both into and back out of any component.
- Focus is always visible. Never `outline: none` without an explicit, visible replacement (`:focus-visible` styling).

## 2. Reach for native semantics before ARIA

A `<button>` is keyboard-operable, focusable, and announced correctly for free. A `<div onClick>` styled to look like one gets none of that without hand-rolling `role`, `tabindex`, and key handlers to match. Prefer native `button`/`a`/`label`/`nav`/`h1–h6` first; add ARIA only for what native elements genuinely can't express. No ARIA beats bad ARIA.

## 3. Focus management on state change

- Opening a modal/drawer moves focus into it and traps it there while open; closing returns focus to what opened it.
- A route change or major content swap moves focus somewhere sensible — not silently left on a now-gone element or reset to the document root with no indication anything happened.

## 4. Forms

- Every input has a programmatically associated label (`<label for>` or `aria-label`) — placeholder text is not a label; it disappears on input and isn't reliably announced.
- Errors are tied to their field via `aria-describedby`, not conveyed by color or position alone.
- Required fields are marked in a way a screen reader announces, not just a visual asterisk.

## 5. Images, icons, and motion

- Meaningful images get real `alt` text describing their content/purpose; purely decorative images get `alt=""` so screen readers skip them.
- Icon-only buttons get an accessible name (`aria-label`), not just a visual glyph.
- Respect `prefers-reduced-motion` — non-essential animation should reduce or disable under it.

## 6. Contrast and target size

Body/placeholder text ≥ 4.5:1 contrast, large text ≥ 3:1 (same bar as `frontend-taste`'s craft-floor pass). Interactive targets (buttons, links, form controls) at least ~44×44px on touch surfaces — a visually "clean" small tap target is still a failure if it can't reliably be hit.

## 7. Refuse by default

- A `div`/`span` with `onClick` standing in for a button.
- Color as the *only* signal for state, error, or required-ness.
- `outline: none` with no focus-visible replacement.
- Autoplaying audio or video.
- `user-scalable=no` or a fixed viewport that disables pinch-zoom.

## 8. Verify

- Tab through the entire flow with no mouse — can you reach and operate everything?
- Run a screen reader once through the critical path (VoiceOver/NVDA), not just the automated audit.
- An automated tool (axe, Lighthouse) is a floor, not a ceiling — it catches roughly a third of real issues. Passing it is the minimum bar, not proof of done.
