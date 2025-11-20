# Steam Deck Customizable Keyboard
A clean, fork‑friendly, fully customizable keyboard theme for the Steam Deck.

Shape it, recolor it, tweak it — this project gives you a structured, modern way to style the on‑screen keyboard using CSS Loader. No hunting through messy CSS, no guessing selectors. Everything is exposed, everything is clear.

---

## ✨ What this project is

This repo contains **three** main parts:

### **1. The actual CSS theme**
Located in:
```
Steam Deck Keyboard Template/
```
This is the complete CSS Loader‑ready theme:
- `keyboard.css` — all keyboard styling
- `theme.json` — manifest with UI controls (color pickers, rounding presets)
- `README.md` — info for the plugin folder

This folder can be copied **directly to the Steam Deck** and will appear as a full theme in CSS Loader.

---

### **2. Presets (optional theme variants)**
Located in:
```
presets/
```
Each file contains a `:root { ... }` block with alternative color/rounding palettes:
- iOS‑style
- Neon
- White Deck
- Hacker Green

You can manually replace your variables in `keyboard.css` with any preset.

---

### **3. Repo screenshots (optional)**
```
repo-screens/
```
Used only for GitHub visuals. These files are **not loaded** on the Deck.

---

## 🧩 How the theme works

All appearance parameters are exposed as CSS variables inside `keyboard.css`:

```css
:root {
  --sdkb-bg-color: #101015;
  --sdkb-key-bg: #1a1b22;
  --sdkb-key-bg-hover: #242633;
  --sdkb-key-bg-pressed: #2f3242;
  --sdkb-key-border-color: #2b2d3a;
  --sdkb-key-border-color-active: #3c3f52;
  --sdkb-key-text-color: #f5f5f7;
  --sdkb-key-text-secondary: #a0a3b5;
  --sdkb-accent: #00bfa5;
  --sdkb-accent-text: #0b1015;
  --sdkb-key-radius: 10px;
  --sdkb-key-radius-special: 14px;
}
```

These variables control **all** important visual elements:
- background
- key colors
- text colors
- accent keys
- rounding
- spacing & shadows

You can edit these manually **or use the built‑in CSS Loader controls** (see below).

---

## 📦 Installing the theme on Steam Deck

### **Option A — simplest (copy the plugin folder)**

1. Download or clone this repo on your Steam Deck:
   ```bash
   cd ~/homebrew
   git clone https://github.com/KeeGooRoomiE/Steam-Deck-Keyboard-CSS-Loader-Template.git
   ```

2. Copy the theme folder:
   ```bash
   cp -r "~/homebrew/Steam-Deck-Keyboard-CSS-Loader-Template/Steam Deck Keyboard Template" \
         "~/homebrew/themes/"
   ```

3. Open **Decky Loader → CSS Loader → Manage Themes**.
4. Enable **Steam Deck Customizable Keyboard**.
5. Hit **Refresh Themes** if needed.

Done — your keyboard now uses the theme.

---

### **Option B — manual file copy (FileZilla, SFTP, Decky File Server)**

1. Open your Deck’s filesystem.
2. Navigate to:
   ```
   /home/deck/homebrew/themes/
   ```
3. Drop the entire folder:
   ```
   Steam Deck Keyboard Template/
   ```
4. Enable it in CSS Loader.

---

## 🎛️ Built‑in Customization via CSS Loader UI

This theme supports **live customization** thanks to the `patches` section in `theme.json`.

You get:

### **Color pickers for:**
- background
- key background
- hover
- pressed
- border
- active border
- text
- secondary text
- accent
- accent text

### **Dropdown presets for key rounding:**
- Square
- Soft
- Pill

No need to edit CSS manually unless you want to.

---

## 🧪 Using presets manually

If you prefer to load a preset instead of tweaking controls:
1. Open any file in `presets/`.
2. Copy the entire `:root { ... }` block.
3. Replace the one in `keyboard.css`.
4. Save & Refresh in CSS Loader.

Presets are just color/rounding presets — nothing more.

---

## 🤓 For developers / modders

### DOM mapping
The theme uses `.sdkb-*` classes internally (for clarity).  
If your Deck environment uses different selectors, simply map styles from:
- `.sdkb-key`
- `.sdkb-key--special`
- `.sdkb-key--accent`
- `.sdkb-key__hint`

…to the real keyboard DOM.

Steam’s keyboard layout may update in future UI revisions — keeping the theme modular makes it easy to maintain.

---

## 📄 License
This project is released under the **MIT License**.
Use it, fork it, remix it, build your own themes on top — it’s yours.