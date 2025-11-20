

# Plugin Preset

This folder contains a ready‑to‑install preset version of the theme for the Steam Deck.

Inside you will find a complete CSS Loader plugin-style structure under:

`Steam Deck Keyboard Template/`

It includes:
- `theme.json` — the manifest describing how the theme should be loaded.
- `keyboard.css` — the actual keyboard styling.

You can copy the entire `Steam Deck Keyboard Template` folder directly into:
`~/homebrew/themes/`

After that, the theme will appear in Decky’s CSS Loader and can be enabled like any other community theme.
# Steam Deck Customizable Keyboard — Plugin Package

This folder contains the **ready‑to‑install plugin version** of the theme for Steam Deck’s CSS Loader.

Everything here is already structured exactly the way Decky expects.  
Just drop this folder into your themes directory and it will appear in CSS Loader automatically.

---

## 📦 What’s inside

- **theme.json** — plugin manifest that registers this keyboard theme in CSS Loader, including color pickers and rounding presets.
- **keyboard.css** — the full customizable keyboard stylesheet.

---

## 🧩 How to install

Copy this entire folder:
```
Steam Deck Keyboard Template/
```
into:
```
~/homebrew/themes/
```

After copying:
1. Open Decky Loader → **CSS Loader**
2. Go to **Manage Themes**
3. Enable **Steam Deck Customizable Keyboard**
4. Press **Refresh Themes** if needed

That’s it — the keyboard theme becomes available system‑wide.

---

## 🔧 Customization

This plugin supports:
- live color editing via color pickers
- multiple rounding presets (Square / Soft / Pill)
- direct variable control in CSS for advanced users

Edit values in **CSS Loader UI** or modify the CSS directly.

---

## 📁 Notes
- This folder is not the root of the project — it’s the ready‑to‑deploy plugin.
- For source files, presets, and documentation, refer to the main repository.