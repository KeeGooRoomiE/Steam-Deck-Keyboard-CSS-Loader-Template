# Steam Deck Customizable Keyboard
A clean, modern, fully‑customizable keyboard theme for the Steam Deck.

This project gives you a simple, structured way to restyle the on‑screen keyboard using CSS Loader. Rounded keys, new palettes, accent colors — everything is controlled through variables and built‑in UI controls.

---

## ✨ What’s included

### **Customizable Keyboard Theme**
Located in the folder:
```
Customizable Keyboard/
```
Inside is the complete plugin:
- `keyboard.css` — the stylesheet
- `theme.json` — manifest with color pickers and rounding presets

Copy this folder to your Deck and the theme appears in CSS Loader immediately.

### **Presets**
```
presets/
```
Optional ready‑to‑use color/rounding profiles.
You can paste these directly into `:root { ... }` if you prefer manual editing.

---

## 🧩 How it works
All style logic is built on CSS variables, for example:
```css
:root {
  --sdkb-bg-color: #101015;
  --sdkb-key-bg: #1a1b22;
  --sdkb-key-text-color: #f5f5f7;
  --sdkb-accent: #00bfa5;
  --sdkb-key-radius: 10px;
}
```
These control everything from colors to rounding.
You can edit them directly **or** adjust them visually through CSS Loader.

---

## 📦 Installing on Steam Deck

### **Quick install**
1. Clone or download the repo on your Deck:
   ```bash
   cd ~/homebrew
   git clone https://github.com/KeeGooRoomiE/Steam-Deck-Keyboard-CSS-Loader-Template.git
   ```
2. Copy the theme:
   ```bash
   cp -r "~/homebrew/Steam-Deck-Keyboard-CSS-Loader-Template/Customizable Keyboard" \
         "~/homebrew/themes/"
   ```
3. Open **Decky → CSS Loader → Manage Themes**
4. Enable **Customizable Keyboard**
5. Press **Refresh Themes** if needed

Done.

---

## 🎛️ Customization
The theme exposes full live controls via CSS Loader:
- background
- key colors
- text colors
- accent colors
- hover/pressed states
- key rounding (Square / Soft / Pill)

No manual editing required.

---

## 📄 License
MIT — do whatever you want with it.