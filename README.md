# 🎮 Steam Deck Customizable Keyboard

[![DeckThemes downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.deckthemes.com%2Fthemes%2F0c5d6c86-ef3e-4af7-a041-34731a51fe7f&query=%24.download.downloadCount&label=downloads&color=1a9fff&style=for-the-badge&logo=steamdeck)](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)
[![DeckThemes stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.deckthemes.com%2Fthemes%2F0c5d6c86-ef3e-4af7-a041-34731a51fe7f&query=%24.starCount&label=stars&color=ffb300&style=for-the-badge)](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)
[![Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.deckthemes.com%2Fthemes%2F0c5d6c86-ef3e-4af7-a041-34731a51fe7f&query=%24.version&label=DeckThemes&color=8b5cf6&style=for-the-badge)](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)

A clean, modern, fully‑customizable keyboard theme for the Steam Deck.

> Your Steam Deck keyboard. But actually yours.

A CSS Loader plugin for restyle the Steam Deck on-screen keyboard — colors, key rounding, accents.
Built as a template: fork it, change variables, ship your own theme in minutes.

See it on [DeckThemes](https://deckthemes.com/themes/view?themeId=0c5d6c86-ef3e-4af7-a041-34731a51fe7f)**

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

**Option A — Git**
```bash
cd ~/homebrew/themes
git clone https://github.com/KeeGooRoomiE/Steam-Deck-Keyboard-CSS-Loader-Template.git "Customizable Keyboard"
```

**Option B — Manual**  
Download → drag `Customizable Keyboard/` into `~/homebrew/themes/`

Then: **Decky → CSS Loader → Manage Themes → Enable "Customizable Keyboard"**

---

## 🍴 Make your own theme

1. Fork this repo
2. Edit CSS variables at the top of `keyboard.css`
3. Update name in `theme.json`
4. Drop in `~/homebrew/themes/` — done

---

## 🖼️ Preset gallery

<table>
<tr>
<td><img src="docs/presets/limited-edition-white.png" width="380" alt="Limited Edition White preset"><br><sub>Limited Edition White</sub></td>
<td><img src="docs/presets/spectrum.png" width="380" alt="Spectrum preset"><br><sub>Spectrum</sub></td>
</tr>
<tr>
<td><img src="docs/presets/oled.png" width="380" alt="OLED preset"><br><sub>OLED</sub></td>
<td><img src="docs/presets/one-dark-style.png" width="380" alt="One Dark Style preset"><br><sub>One Dark Style</sub></td>
</tr>
</table>

<sub>The <kbd>h</kbd> key is shown pressed in each shot.</sub>

---

## 📄 License

MIT — fork it, remix it, ship it.
