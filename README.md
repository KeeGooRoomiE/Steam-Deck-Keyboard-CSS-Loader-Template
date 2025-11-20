# Steam-Deck-Keyboard-CSS-Loader-Template
Your Steam Deck keyboard, but actually customizable. Fork it, recolor it, reshape it.

# Steam Deck Keyboard CSS Loader Template

Your Steam Deck keyboard, but actually customizable. Fork it, recolor it, reshape it.

Minimal CSS template for styling the Steam Deck on-screen keyboard via CSS Loader (or similar tools).
The layout stays close to default – you only tweak colors, rounding and a few spacing/shadow settings.

---

## What this is

- A small, readable CSS file (`keyboard.css`).
- All important settings are exposed as CSS variables in the `:root` block.
- Designed to be forked and turned into your own theme in a couple of minutes.

You don’t have to dig through a huge stylesheet – just change the variables and, if needed, map the styles to your own keyboard selectors.

---

## Files

- `keyboard.css` – base theme for the Steam Deck keyboard.
- `LICENSE` – MIT license.
- `README.md` – this file.

You can also add a `screenshots/` folder with previews of your theme.

---

## Usage

1. Open `keyboard.css` in this repo.
2. Copy its contents into your Steam Deck CSS loader (for example, CSS Loader plugin).
3. Apply or reload the style.
4. If your keyboard uses different selectors, map the styles from the `.sdkb-*` classes to your real DOM classes.

> **Note:** The `.sdkb-*` classes are just clean, human-readable placeholders. You can either keep them (if your setup allows) or copy the styles into the real Steam keyboard selectors.

---

## Customization

All the core values are defined at the top of `keyboard.css`:

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

Change these to get a different look:

- **Background & keys** – main keyboard background and key colors.
- **Text & secondary text** – primary labels and small hints.
- **Accent** – color for special keys (e.g. Enter, active layout).
- **Radius** – how round your keys look.

### Quick styling ideas

- **iOS-like**
  - Light background.
  - Dark text.
  - Higher radius (12–16px) for a softer look.

- **White Steam Deck vibe**
  - Neutral light background.
  - Keys slightly darker than the background.
  - Strong accent color for active keys.

---

## Mapping to real selectors

If you want to bind the styles directly to the real Steam Deck keyboard elements, you can:

- Inspect the keyboard in a browser / devtools (through CSS Loader tools).
- Find the actual class names used for keys and rows.
- Copy styles from `.sdkb-key`, `.sdkb-key--special`, `.sdkb-key--accent`, etc., into those selectors.

This template doesn’t force a specific DOM structure – it just gives you a clean base.

---

## Forking / creating your own theme

1. Click **Fork** on GitHub.
2. Edit the `:root` block in `keyboard.css` to set your colors, radius and spacing.
3. Optionally, update selectors to match your exact keyboard.
4. Add screenshots and rename the project to match your theme.

That’s it – you now have your own Steam Deck keyboard theme repo.

---

## License

This project is released under the [MIT License](./LICENSE).

You’re free to use it in personal projects, share it, fork it, and ship your own themes based on it.