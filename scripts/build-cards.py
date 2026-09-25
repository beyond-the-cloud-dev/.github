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
    ("soql-lib", "SOQL Lib", "Query builder, selectors", None),
    ("dml-lib", "DML Lib", "Unit of work you can mock", None),
    ("async-lib", "Async Lib", "Queueable, batch, schedule", None),
    ("http-mock-lib", "HTTP Mock Lib", "Callout mocks in one line", None),
    ("apex-consts", "Apex Consts", "No more magic strings", None),
    ("cache-manager", "Cache Manager", "One API for Platform Cache", None),
    ("test-lib", "Test Lib", "Test data builders", "Beta"),
    ("trigger-lib", "Trigger Lib", "Trigger framework", "WIP"),
    ("veles", "Veles", "Sandbox and scratch org setup", None),
    ("release-notifier", "Release Notifier", "In-app release notes", None),
    ("isv-analytics", "ISV Analytics", "Usage analytics for ISVs", None),
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
        "pill_text": "#0b6fa0",
        "pill_fill": 0.10,
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
        "pill_text": "#6cc6f0",
        "pill_fill": 0.14,
    },
}

BLUE = "#2AABE2"
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
PAD = 6
W, H = 188, 132
ICON_W, ICON_H = 60, 44


def pill(label, t):
    text = label.upper()
    width = round(len(text) * 6.4 + 16)
    x = PAD + W - width - 10
    y = PAD + 10
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="18" rx="9" fill="{BLUE}" '
        f'fill-opacity="{t["pill_fill"]}" stroke="{BLUE}" stroke-opacity=".35"/>'
        f'<text x="{x + width / 2}" y="{y + 12.5}" text-anchor="middle" font-size="9.5" '
        f'font-weight="600" letter-spacing=".6" fill="{t["pill_text"]}">{escape(text)}</text>'
    )


def card(slug, name, desc, status, t):
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
<text x="{cx}" y="{PAD + 88}" text-anchor="middle" font-size="15" font-weight="600" fill="{t["name"]}">{escape(name)}</text>
<text x="{cx}" y="{PAD + 108}" text-anchor="middle" font-size="11.5" fill="{t["desc"]}">{escape(desc)}</text>
{pill(status, t) if status else ""}
</svg>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, name, desc, status in CARDS:
        for theme, t in THEMES.items():
            (OUT / f"{slug}-{theme}.svg").write_text(card(slug, name, desc, status, t))
    print(f"Wrote {len(CARDS) * len(THEMES)} cards to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
