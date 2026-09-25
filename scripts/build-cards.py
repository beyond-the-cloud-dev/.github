#!/usr/bin/env python3
"""Build the light and dark SVG cards used in profile/README.md.

Icons live in assets/icons/<slug>.png and are embedded as base64, because
GitHub renders README SVGs as <img>, which cannot load external files.

Usage: python3 scripts/build-cards.py
"""

import base64
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "assets" / "icons"
OUT = ROOT / "assets" / "cards"

CARDS = [
    ("soql-lib", "SOQL Lib", "Query builder, selectors"),
    ("dml-lib", "DML Lib", "Unit of work you can mock"),
    ("async-lib", "Async Lib", "Queueable, batch, schedule"),
    ("callout-lib", "Callout Lib", "Fluent HTTP callouts"),
    ("http-mock-lib", "HTTP Mock Lib", "Callout mocks in one line"),
    ("trigger-lib", "Trigger Lib", "Trigger framework"),
    ("test-lib", "Test Lib", "Test data builders"),
    ("apex-consts", "Apex Consts", "No more magic strings"),
    ("cache-manager", "Cache Manager", "One API for Platform Cache"),
    ("veles", "Veles", "Secure config across every org"),
    ("release-notifier", "Release Notifier", "Turn releases into adoption"),
    ("isv-analytics", "ISV Analytics", "AppExchange usage monitoring"),
]

THEMES = {
    "light": {
        "card": "#ffffff",
        "name": "#1f2328",
        "desc": "#59636e",
        "edge": "#d1d9e0",
        "edge_accent": 0.75,
        "glow": 0.10,
        "shadow": "#1f2328",
        "shadow_opacity": 0.10,
    },
    "dark": {
        "card": "#151b23",
        "name": "#f0f6fc",
        "desc": "#9198a1",
        "edge": "#3d444d",
        "edge_accent": 0.9,
        "glow": 0.18,
        "shadow": "#2AABE2",
        "shadow_opacity": 0.16,
    },
}

BLUE = "#2AABE2"
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
PAD = 6
W, H = 228, 136
ICON_W, ICON_H = 64, 48



def card(slug, name, desc, t):
    icon = base64.b64encode((ICONS / f"{slug}.png").read_bytes()).decode()
    cx = PAD + W / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W + 2 * PAD}" height="{H + 2 * PAD}" viewBox="0 0 {W + 2 * PAD} {H + 2 * PAD}" font-family="{FONT}">
<defs>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{BLUE}" stop-opacity="{t["edge_accent"]}"/>
<stop offset=".45" stop-color="{t["edge"]}"/>
<stop offset="1" stop-color="{t["edge"]}"/>
</linearGradient>
<radialGradient id="glow" cx=".5" cy="0" r=".85">
<stop offset="0" stop-color="{BLUE}" stop-opacity="{t["glow"]}"/>
<stop offset="1" stop-color="{BLUE}" stop-opacity="0"/>
</radialGradient>
<filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
<feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="{t["shadow"]}" flood-opacity="{t["shadow_opacity"]}"/>
</filter>
</defs>
<rect x="{PAD}" y="{PAD}" width="{W}" height="{H}" rx="14" fill="{t["card"]}" filter="url(#shadow)"/>
<rect x="{PAD}" y="{PAD}" width="{W}" height="{H}" rx="14" fill="url(#glow)"/>
<rect x="{PAD + 0.5}" y="{PAD + 0.5}" width="{W - 1}" height="{H - 1}" rx="13.5" fill="none" stroke="url(#edge)"/>
<image href="data:image/png;base64,{icon}" x="{cx - ICON_W / 2}" y="{PAD + 20}" width="{ICON_W}" height="{ICON_H}"/>
<text x="{cx}" y="{PAD + 92}" text-anchor="middle" font-size="15" font-weight="600" fill="{t["name"]}">{escape(name)}</text>
<text x="{cx}" y="{PAD + 112}" text-anchor="middle" font-size="11.5" fill="{t["desc"]}">{escape(desc)}</text>
</svg>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, name, desc in CARDS:
        for theme, t in THEMES.items():
            (OUT / f"{slug}-{theme}.svg").write_text(card(slug, name, desc, t))
    print(f"Wrote {len(CARDS) * len(THEMES)} cards to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
