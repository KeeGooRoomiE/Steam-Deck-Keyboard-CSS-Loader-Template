# Presets

This folder contains ready‑to‑use visual presets for the Steam Deck keyboard theme.
Each preset is a standalone `:root { ... }` block that overrides the variables in the main `keyboard.css`.

You can copy any preset directly into your theme to instantly switch styles.

---

## Available Presets

**• ios-light.css**  – soft bright design inspired by iOS.

**• steam-white.css** – clean white/gray look similar to a "white edition" Steam Deck.

**• neon-cyan.css** – dark cyberpunk palette with neon accents.

**• hacker-green.css** – retro terminal / CRT‑inspired green theme.

---

## How to Use a Preset

1. Open any `.css` file in this folder.
2. Copy the entire `:root { ... }` block.
3. Paste it at the top of your `keyboard.css` (or overwrite your existing variables).
4. Reload your CSS Loader theme on the Deck.

Presets do **not** add new selectors — they only change colors, rounding, shadows, and other variables.

---

## Creating Your Own Preset

To add a custom preset:

1. Create a new file inside this folder.
2. Add a `:root` block with your colors and radius values.
3. (Optional) Add a screenshot to the main `screenshots/` directory.
4. Update this README if you'd like your preset to appear in the list.

This folder acts as a small theme library — easy to explore, easy to fork.
