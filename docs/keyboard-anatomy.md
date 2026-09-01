# Keyboard styling reference

What `keyboard.css` maps, and the key states. Verified live against the
Steam client (Aug 2026).

---

## Theme variables (`--sdkb-*`)

Set by each preset in `theme.json`, or by the Custom colour pickers.

| Variable | Controls |
|---|---|
| `--sdkb-bg-color` | keyboard background |
| `--sdkb-key-bg` | normal key fill (and spacebar) |
| `--sdkb-key-bg-hover` | focused key fill |
| `--sdkb-key-bg-pressed` | legacy pressed fill (see `--sdkb-press-bg`) |
| `--sdkb-key-text-color` | key label |
| `--sdkb-key-text-secondary` | the small "shifted" hint char (`!` over `1`, …) |
| `--sdkb-accent` / `--sdkb-accent-text` | toggle-on keys; fallback for `fn` / `press` / `glyph` |
| `--sdkb-fn-bg` / `--sdkb-fn-text` | function keys (Tab, Caps, Shift, Enter, Backspace) and utility keys (arrows, Paste, emoji/layout switch, hide-keyboard) |
| `--sdkb-glyph-color` | inline `<svg>` icons + function/utility key text labels |
| `--sdkb-glyph-filter` | `<img>` controller glyphs (L2 / X / R2 / L3); filter chain, `none` = native |
| `--sdkb-key-radius` | corner radius — unit-less number |
| `--sdkb-key-border-width` / `--sdkb-key-border-color` | key border — width unit-less, `0` = none |
| `--sdkb-key-gap` | space between keys — unit-less number |
| `--sdkb-label-size` | key label font size (`px`); unset = native |
| `--sdkb-glow` | resting-key inner glow / bevel (`box-shadow` value); `none` = flat |
| `--sdkb-press-bg` / `--sdkb-press-text` | pressed key fill and label |
| `--sdkb-press-glow` | pressed-key halo + expanding ripple colour |
| `--sdkb-press-scale` | pressed-key shrink factor; `1` = no animation |
| `--sdkb-transition` | key colour transition duration |

---

## Steam variables we set (on `.DefaultTheme`)

These are the only colour hooks Steam exposes. All verified to apply.

| Steam variable | Fed from |
|---|---|
| `--background-color` | `--sdkb-bg-color` |
| `--key-background-color` | `--sdkb-key-bg` |
| `--key-focused-background-color` | `--sdkb-key-bg-hover` |
| `--key-touched-background-color` | `--sdkb-key-bg-pressed` * |
| `--key-color`, `--key-focused-color`, `--key-touched-color` | `--sdkb-key-text-color` |
| `--key-meta / tab / caps / shift / enter / backspace -background-color` | `--sdkb-fn-bg` |
| `--key-meta / tab / caps / shift / enter / backspace -color` | `--sdkb-fn-text` |
| `--key-toggleon-background-color` / `--key-toggleon-color` | `--sdkb-accent` / `--sdkb-accent-text` |
| `--key-shift-label-color`, `--key-focused-shift-label-color` | `--sdkb-key-text-secondary` |
| `--key-spacebar-background-color` / `--key-spacebar-color` | `--sdkb-key-bg` / `--sdkb-key-text-color` |
| `--key-extendedkey-*` (long-press popup) | `--sdkb-key-bg-hover` / `--sdkb-accent` |

**Not available in Steam** — done with direct rules instead:

- `--key-border-color`, `--key-radius` — do not exist.
- The **touched** background is hard-coded by Steam (`#1a9fff`); `--key-touched-background-color` (*) is ignored. We override it on the touched-class rule with `--sdkb-press-bg`.

---

## Properties set by direct rule (no Steam variable)

| Target | Property | From |
|---|---|---|
| every key | `border-radius` | `--sdkb-key-radius` |
| every key | `border` | `--sdkb-key-border-width` + `--sdkb-key-border-color` |
| every key | `box-shadow` | `--sdkb-glow` |
| row | `gap` | `--sdkb-key-gap` |
| key label | `font-size` | `--sdkb-label-size` (else native) |
| pressed key | `background`, `color`, `box-shadow`, `z-index` | `--sdkb-press-bg` / `-text` / `-glow` |
| pressed ripple (`::after`) | `background` | `--sdkb-press-glow` |
| pressed key | `transform: scale`, `filter: brightness` | `--sdkb-press-scale` |
| utility keys (arrows / Paste / switch / hide) | `background`, `color` | `--sdkb-fn-bg` / `--sdkb-fn-text` |
| function/utility labels + inline `<svg>` | `color`, `fill` | `--sdkb-glyph-color` |
| `<img>` glyphs | `filter` | `--sdkb-glyph-filter` |

---

## Key states

| State | How Steam marks it | Styling |
|---|---|---|
| **resting** | — | `--key-background-color` / `--key-color`; `--sdkb-glow` |
| **focused** (cursor on key) | class `_21EoN…` | Steam applies `--key-focused-background-color` / `--key-focused-color` (works via variable) |
| **touched / pressed** | class `_3UFQq…` | Steam hard-codes the background → we override on that class: `--sdkb-press-*`, shrink, brightness, and a white ripple `::after` recoloured to `--sdkb-press-glow` |
| **toggle-on** (Caps / Shift latched) | class + `--key-toggleon-*` | `--sdkb-accent` / `--sdkb-accent-text` |

There is no `:hover` state on this keyboard.

`_21EoN` / `_3UFQq` are webpack hash prefixes and can change on a Steam client update.
