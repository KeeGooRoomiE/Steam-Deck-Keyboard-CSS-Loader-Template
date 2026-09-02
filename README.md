# 🎮 Steam Deck Customizable Keyboard

[![DeckThemes downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.deckthemes.com%2Fthemes%2F0c5d6c86-ef3e-4af7-a041-34731a51fe7f&query=%24.download.downloadCount&label=downloads&color=1a9fff&style=for-the-badge&logo=steamdeck)](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)
[![DeckThemes stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.deckthemes.com%2Fthemes%2F0c5d6c86-ef3e-4af7-a041-34731a51fe7f&query=%24.starCount&label=stars&color=ffb300&style=for-the-badge)](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)
[![Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.deckthemes.com%2Fthemes%2F0c5d6c86-ef3e-4af7-a041-34731a51fe7f&query=%24.version&label=DeckThemes&color=8b5cf6&style=for-the-badge)](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)

A clean, modern, fully‑customizable keyboard theme for the Steam Deck.

> Your Steam Deck keyboard. But actually yours.

A CSS Loader theme that restyles the Steam Deck on-screen keyboard — colors, key rounding, accents.
Built as a template: fork it, change variables, ship your own theme in minutes.

See it on [DeckThemes](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)

![Preview](small_preview.png)

---

## ✨ Features

- 🎨 **13 hand-tuned presets** — colours, corner radius, glow, and function-key style are baked into
  each one individually:
  - Inspired by Steam Points Shop keyboards: **Steam Green · Spectrum · Cerulean · Digital · Seafoam ·
    Candy Coded · Grape · Ruby · Pumpkin · OLED · Limited Edition White**
  - Plus **One Dark Style** and **OLED Black**
- 🌈 Real per-key effects, not just flat recolours — Spectrum's rainbow gradient (with an authentic
  per-row offset), Candy Coded's glossy gradient keycaps, OLED's inner glow, Steam Green's raised
  bevel with an inverted pressed state — all from the same small set of CSS variables
- 🎛️ Two global controls in the CSS Loader UI: **Press animation** (on/off) and **Function keys**
  (accent / neutral)
- 🖌️ Full **Custom** mode — 9 colour pickers for every part of the keyboard, no code
- 🧱 CSS-variable architecture, verified live against the real Steam keyboard DOM
  (see [`docs/keyboard-anatomy.md`](docs/keyboard-anatomy.md))
- 📦 Drop-in install via Decky

> The Points Shop–inspired presets are colour recreations tuned by hand against the official art —
> not the original gradient/glow themes pixel-for-pixel.

---

## 📦 Installation

**Option A — CSS Loader store (recommended)**
Decky → **CSS Loader** → **Browse Themes** → search **Customizable Keyboard** → download.
Then enable it under **Manage Themes** and pick a preset.

**Option B — Git**
```bash
cd ~/homebrew/themes
git clone https://github.com/KeeGooRoomiE/Steam-Deck-Keyboard-CSS-Loader-Template.git "Customizable Keyboard"
```

**Option C — Manual**
Download → drag `Customizable Keyboard/` into `~/homebrew/themes/`

For B and C: **Decky → CSS Loader → Manage Themes → Enable "Customizable Keyboard"**

---

## 🍴 Make your own theme

1. Fork this repo
2. Edit CSS variables at the top of `keyboard.css`
3. Update name in `theme.json`
4. Drop in `~/homebrew/themes/` — done

---

## 🖼️ Preset gallery

<sub>Captured on-device. The <kbd>h</kbd> key is shown pressed in every shot.</sub>

| | |
|---|---|
| **Steam Green**<br><img src="docs/presets/steam-green.png" width="430"> | **Spectrum**<br><img src="docs/presets/spectrum.png" width="430"> |
| **Cerulean**<br><img src="docs/presets/cerulean.png" width="430"> | **Digital**<br><img src="docs/presets/digital.png" width="430"> |
| **Seafoam**<br><img src="docs/presets/seafoam.png" width="430"> | **Candy Coded**<br><img src="docs/presets/candy-coded.png" width="430"> |
| **Grape**<br><img src="docs/presets/grape.png" width="430"> | **Ruby**<br><img src="docs/presets/ruby.png" width="430"> |
| **Pumpkin**<br><img src="docs/presets/pumpkin.png" width="430"> | **OLED**<br><img src="docs/presets/oled.png" width="430"> |
| **Limited Edition White**<br><img src="docs/presets/limited-edition-white.png" width="430"> | **Marshmallow**<br><img src="docs/presets/marshmallow.png" width="430"> |
| **One Dark Style**<br><img src="docs/presets/one-dark-style.png" width="430"> | **OLED Black**<br><img src="docs/presets/oled-black.png" width="430"> |

---

## 📄 License

MIT — fork it, remix it, ship it.
