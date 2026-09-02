#!/usr/bin/env python3
"""Generate preview/index.html — a standalone browser preview of the Steam Deck
keyboard using the real DOM class names, reconstructed Steam base layout, the
project's keyboard.css, and every preset from theme.json.

Run:  python3 preview/build.py     (re-run after editing theme.json)
"""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEME = json.load(open(os.path.join(ROOT, "Customizable Keyboard", "theme.json")))
KEYBOARD_CSS = open(os.path.join(ROOT, "Customizable Keyboard", "keyboard.css")).read()
PRESETS = {k: {vk: vv[0] for vk, vv in v.items()}
           for k, v in THEME["patches"]["Preset"]["values"].items()}

def root_block(name):
    p = PRESETS.get(name, {})
    return ":root{" + "".join("%s:%s;" % (k, v) for k, v in p.items()) + "}"

KEY = "_2KhPXikozxMpbIRo_6jPxW"          # base key class (every key)
FOCUS = "_21EoN2ZlmHNY3fjho_HMae"        # focused
TOUCH = "_3UFQq1GinEyksceos-TETi"        # pressed / touched
HINT = "_3FZukK3yuHnaZ_X3yujMNS"         # shifted-hint span
GW = "_3VtXfHDGV1q2LCVruVnHed"           # glyph wrapper

# controller-button glyph as a data-URI SVG. The `#steaminputglyphs/...` fragment
# makes keyboard.css's  img[src*="steaminputglyphs"]  selector match.
def badge(txt):
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 34 20'>"
           "<rect x='0.5' y='0.5' width='33' height='19' rx='4' fill='%23222'/>"
           "<text x='17' y='14' font-family='Arial' font-size='11' font-weight='700'"
           " text-anchor='middle' fill='%23fff'>" + txt + "</text></svg>")
    return "data:image/svg+xml," + svg.replace("#", "%23") + "#steaminputglyphs/" + txt.lower() + ".svg"

SVG = {
 "emoji": "<svg viewBox='0 0 36 36' fill='none'><circle cx='18' cy='18' r='14' stroke='currentColor' stroke-width='2.5'/><circle cx='13' cy='15' r='1.8' fill='currentColor'/><circle cx='23' cy='15' r='1.8' fill='currentColor'/><path d='M12 22c2 2.6 4 3.6 6 3.6s4-1 6-3.6' stroke='currentColor' stroke-width='2.5' stroke-linecap='round'/></svg>",
 "globe": "<svg viewBox='0 0 36 36' fill='none'><circle cx='18' cy='18' r='14' stroke='currentColor' stroke-width='2.2'/><path d='M4 18h28M18 4c4 4 4 24 0 28M18 4c-4 4-4 24 0 28' stroke='currentColor' stroke-width='2.2'/></svg>",
 "up":   "<svg viewBox='0 0 36 36' fill='none'><path d='M10 22l8-9 8 9' stroke='currentColor' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>",
 "down": "<svg viewBox='0 0 36 36' fill='none'><path d='M10 14l8 9 8-9' stroke='currentColor' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>",
 "left": "<svg viewBox='0 0 36 36' fill='none'><path d='M22 10l-9 8 9 8' stroke='currentColor' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>",
 "right":"<svg viewBox='0 0 36 36' fill='none'><path d='M14 10l9 8-9 8' stroke='currentColor' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>",
 "close":"<svg viewBox='0 0 36 36' fill='none'><rect x='3' y='7' width='30' height='16' rx='2' stroke='currentColor' stroke-width='2'/><path d='M8 27l20 0' stroke='currentColor' stroke-width='2' stroke-linecap='round'/></svg>",
}

# rows: list of (label, hint, keytheme, special_hash, flex, glyph_badge, svg_key)
def K(label, hint=None, kt=None, sp=None, flex=1.0, gb=None, svg=None):
    return dict(label=label, hint=hint, kt=kt or ("KeyTheme_" + (label or "")),
                sp=sp, flex=flex, gb=gb, svg=svg)

ROWS = [
  [K("`","~"),K("1","!"),K("2","@"),K("3","#"),K("4","$"),K("5","%"),K("6","^"),
   K("7","&"),K("8","*"),K("9","("),K("0",")"),K("-","_"),K("=","+"),
   K("Backspace",None,"KeyTheme_Backspace","_3LsB3VZBjMjAp0RCa_3MGS",1.9,"X")],
  [K("Tab",None,"KeyTheme_Tab","_3GfcsK1T47BLa5UQ3e4Xh3",1.15),
   K("q"),K("w"),K("e"),K("r"),K("t"),K("y"),K("u"),K("i"),K("o"),K("p"),
   K("[","{"),K("]","}"),K("\\","|")],
  [K("Caps",None,"KeyTheme_CapsLock","NGv5FNsp6c4OnD0_KOiDl",1.45,"L3"),
   K("a"),K("s"),K("d"),K("f"),K("g"),K("h"),K("j"),K("k"),K("l"),
   K(";",":"),K("'","\""),
   K("Enter",None,"KeyTheme_Enter","IunX6VHNYj-i8dv5WJzpM",1.9,"R2")],
  [K("Shift",None,"KeyTheme_Shift","_2ye7YjL-n6ql_6UPyf5ptv",2.15,"L2"),
   K("z"),K("x"),K("c"),K("v"),K("b"),K("n"),K("m"),
   K(",","<"),K(".",">"),K("/","?"),
   K("Shift",None,"KeyTheme_Shift","iMZ3TXDTLXYVzU8Q7A9yP",2.15,"L2")],
  [K("",None,"KeyTheme_SwitchKeys_Emoticons","_1WbIjnypHqw8t8_NFQHPJr",1.3,None,"emoji"),
   K("",None,"KeyTheme_SwitchKeys_Layout","_1WbIjnypHqw8t8_NFQHPJr",1.3,None,"globe"),
   K("",None,"KeyTheme_Space",None,7.5),
   K("",None,"KeyTheme_ArrowUp","_1WbIjnypHqw8t8_NFQHPJr",1.1,None,"up"),
   K("",None,"KeyTheme_ArrowLeft","_1WbIjnypHqw8t8_NFQHPJr",1.1,None,"left"),
   K("",None,"KeyTheme_ArrowRight","_1WbIjnypHqw8t8_NFQHPJr",1.1,None,"right"),
   K("Paste",None,"KeyTheme_VKPaste","_1WbIjnypHqw8t8_NFQHPJr",1.6),
   K("",None,"KeyTheme_VKClose",None,1.3,None,"close")],
]

def esc(s): return html.escape(s or "", quote=True)

def render_key(k, col):
    cls = [KEY, "Col_%d" % col, k["kt"]]
    if k["sp"]: cls.insert(1, k["sp"])
    style = "flex:%s 1 0;" % k["flex"]
    inner = ""
    if k["hint"]:
        inner += "<span class='%s'>%s</span>" % (HINT, esc(k["hint"]))
    if k["gb"]:
        inner += "<div class='%s'><img alt='%s' src=\"%s\"></div>" % (GW, k["gb"], badge(k["gb"]))
    if k["svg"]:
        inner += "<span>%s</span>" % SVG[k["svg"]]
    if k["label"]:
        inner += "<span>%s</span>" % esc(k["label"])
    return "<div class=\"%s\" style=\"%s\">%s</div>" % (" ".join(cls), style, inner)

rows_html = ""
for ri, row in enumerate(ROWS):
    keys = "".join(render_key(k, ci) for ci, k in enumerate(row))
    rows_html += "  <div class=\"d-_DJF8LavBgxrCblp2Kb Row_%d Panel\">%s</div>\n" % (ri, keys)

STEAM_BASE = """
/* --- reconstructed minimal Steam OSK base (approximation) --- */
.kbd-stage { display:inline-block; padding:24px; }
.DefaultTheme.Oel3OSshpNqQ5hIOrC1Z5 { display:inline-block; background: var(--background-color,#1e2127); }
._45rH7-kY4P2uVEb3TxZhm.Layout_qwerty {
  display:flex; flex-direction:column; width:1200px;
  padding:3px 3px 1px 1px; background: var(--background-color,#1e2127);
}
[class*="Row_"] { display:flex; }
._2KhPXikozxMpbIRo_6jPxW {
  height:44px; margin:1px; display:flex; align-items:center; justify-content:center;
  position:relative; box-sizing:border-box; overflow:visible; user-select:none;
  font-family:"Motiva Sans","Arial",sans-serif; font-size:16px; line-height:1;
  background-color: var(--key-background-color,#282c34);
  color: var(--key-color,#abb2bf);
}
._2KhPXikozxMpbIRo_6jPxW > span { position:relative; z-index:1; }
._2KhPXikozxMpbIRo_6jPxW svg { width:20px; height:20px; display:block; }
._3FZukK3yuHnaZ_X3yujMNS {
  position:absolute; top:3px; left:7px; font-size:11px; z-index:1;
  opacity:.45; color: var(--key-shift-label-color, currentColor);
}
._3VtXfHDGV1q2LCVruVnHed { position:absolute; right:8px; bottom:6px; margin:0; line-height:0; }
._3VtXfHDGV1q2LCVruVnHed img { width:24px; height:14px; display:block; }
/* function keys read Steam's per-key vars */
.KeyTheme_Backspace { background-color: var(--key-backspace-background-color); color: var(--key-backspace-color); }
.KeyTheme_Enter     { background-color: var(--key-enter-background-color);     color: var(--key-enter-color); }
.KeyTheme_Tab       { background-color: var(--key-tab-background-color);       color: var(--key-tab-color); }
.KeyTheme_CapsLock  { background-color: var(--key-caps-background-color);      color: var(--key-caps-color); }
.KeyTheme_Shift     { background-color: var(--key-shift-background-color);     color: var(--key-shift-color); }
.KeyTheme_Space     { background-color: var(--key-spacebar-background-color);  color: var(--key-spacebar-color); }
/* focused */
._21EoN2ZlmHNY3fjho_HMae {
  background-color: var(--key-focused-background-color,#3a3f4a);
  color: var(--key-focused-color,inherit);
}
/* touched — Steam hard-codes the blue + a white ripple ::after */
._3UFQq1GinEyksceos-TETi { background-color: #1a9fff; }
._3UFQq1GinEyksceos-TETi::after {
  content:""; position:absolute; inset:0; border-radius:inherit;
  background:#fff; opacity:.55; mix-blend-mode:overlay; z-index:2;
}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Keyboard preview — Customizable Keyboard</title>
<style>
  body { margin:0; font-family:Arial,Helvetica,sans-serif; background:#15171c; color:#cfd2d8; }
  .toolbar { position:sticky; top:0; z-index:10; display:flex; gap:14px; align-items:center;
             flex-wrap:wrap; padding:12px 18px; background:#1d2027; border-bottom:1px solid #2b2f38; }
  .toolbar label { font-size:13px; color:#9aa0aa; }
  select, button { font:inherit; background:#262a33; color:#e6e8ec; border:1px solid #3a3f4a;
                   border-radius:6px; padding:6px 10px; cursor:pointer; }
  button.active { background:#3a6df0; border-color:#3a6df0; color:#fff; }
  .backdrops button { width:26px; height:26px; padding:0; }
  #stageWrap { display:flex; justify-content:flex-start; padding:34px 10px; overflow:auto; }
  .kbd-stage { transform-origin:top left; }
  .bd-deck  { background:#000; }
  .bd-grey  { background:#3a3f4a; }
  .bd-check { background:
     repeating-conic-gradient(#2a2d34 0% 25%, #34383f 0% 50%) 50% / 24px 24px; }
  .hint { font-size:12px; color:#7c828c; padding:6px 18px 14px; }
  .DefaultTheme [class*="KeyTheme_"] { cursor:pointer; }
</style>
</head>
<body>

<div class="toolbar">
  <label>Preset
    <select id="preset">__OPTIONS__</select>
  </label>
  <label>Zoom
    <select id="zoom">
      <option value="1">100%</option>
      <option value="0.75">75%</option>
      <option value="0.6" selected>60%</option>
      <option value="0.5">50%</option>
    </select>
  </label>
  <span class="states">
    <button data-state="rest" class="active">Rest</button>
    <button data-state="focus">Focus&nbsp;h</button>
    <button data-state="press">Press&nbsp;h</button>
  </span>
  <span class="backdrops">
    <button class="bd-deck active" data-bd="bd-deck" title="black"></button>
    <button class="bd-grey" data-bd="bd-grey" title="grey"></button>
    <button class="bd-check" data-bd="bd-check" title="checker"></button>
  </span>
  <span class="hint">click any key to toggle its pressed state</span>
</div>

<div id="stageWrap" class="bd-deck">
  <div class="kbd-stage">
__STAGE__
  </div>
</div>

<p class="hint">Reconstructed layout — key widths, fonts and glyph art are approximations of the
real Steam OSK. Class names, structure, states and the project <code>keyboard.css</code> are the real thing.</p>

<style id="steam-base">__STEAMBASE__</style>
<style id="keyboard-css">__KEYBOARDCSS__</style>
<style id="preset-vars">__DEFAULTVARS__</style>

<script>
const PRESETS = __PRESETS__;
const FOCUS = "__FOCUS__", TOUCH = "__TOUCH__";
const sel = document.getElementById('preset');
const pv  = document.getElementById('preset-vars');

function applyPreset(name){
  const p = PRESETS[name] || {};
  let css = ':root{';
  for (const k in p) css += k + ':' + p[k] + ';';
  css += '}';
  pv.textContent = css;
}
sel.addEventListener('change', () => applyPreset(sel.value));

// state buttons operate on the "h" key
const hKey = [...document.querySelectorAll('[class*="KeyTheme_h"]')][0];
document.querySelectorAll('.states button').forEach(b => {
  b.addEventListener('click', () => {
    document.querySelectorAll('.states button').forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    if (!hKey) return;
    hKey.classList.remove(FOCUS, TOUCH);
    if (b.dataset.state === 'focus') hKey.classList.add(FOCUS);
    if (b.dataset.state === 'press') hKey.classList.add(TOUCH);
  });
});

// click any key -> toggle pressed
document.querySelectorAll('.DefaultTheme [class*="KeyTheme_"]').forEach(k => {
  k.addEventListener('click', () => k.classList.toggle(TOUCH));
});

// backdrop
const wrap = document.getElementById('stageWrap');
document.querySelectorAll('.backdrops button').forEach(b => {
  b.addEventListener('click', () => {
    document.querySelectorAll('.backdrops button').forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    wrap.className = b.dataset.bd;
  });
});

// zoom
const stage = document.querySelector('.kbd-stage');
const zoom = document.getElementById('zoom');
function applyZoom(){ stage.style.transform = 'scale(' + zoom.value + ')'; }
zoom.addEventListener('change', applyZoom);

applyPreset(sel.value);
applyZoom();
</script>
</body>
</html>
"""

default = THEME["patches"]["Preset"].get("default", list(PRESETS)[0])
opts = "".join(
    "<option%s>%s</option>" % (" selected" if n == default else "", esc(n))
    for n in PRESETS if n != "Custom")

out = (PAGE
       .replace("__OPTIONS__", opts)
       .replace("__STAGE__", "<div class=\"DefaultTheme Oel3OSshpNqQ5hIOrC1Z5\">\n"
                "<div class=\"_45rH7-kY4P2uVEb3TxZhm Layout_qwerty _45rH7-kY4P2uVEb3TxZhm DefaultTheme Panel\">\n"
                + rows_html +
                "</div>\n</div>")
       .replace("__STEAMBASE__", STEAM_BASE)
       .replace("__KEYBOARDCSS__", KEYBOARD_CSS)
       .replace("__DEFAULTVARS__", root_block(default))
       .replace("__PRESETS__", json.dumps(PRESETS))
       .replace("__FOCUS__", FOCUS).replace("__TOUCH__", TOUCH))

open(os.path.join(ROOT, "preview", "index.html"), "w").write(out)
print("wrote preview/index.html —", len(PRESETS) - 1, "presets")
