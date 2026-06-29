#!/usr/bin/env python3
"""Add unique brand/car description for carbrands.world AdSense compliance"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, "build.py"), "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add brand description section in build_brand_page after the detail-hero
old_hero = '''<div class="detail-hero"><div class="brand-name-lg">{html.escape(b["name"])}</div><div class="brand-sub">{loc} · {ui["founded"]} {b["founded"]} · {len(b_cars)} {ui["models"]}</div></div>
<div class="model-grid">'''

new_hero = '''<div class="detail-hero"><div class="brand-name-lg">{html.escape(b["name"])}</div><div class="brand-sub">{loc} · {ui["founded"]} {b["founded"]} · {len(b_cars)} {ui["models"]}</div></div>
<div class="seo-extra" style="max-width:800px;margin:16px auto;padding:18px 24px;background:var(--surface2);border-radius:var(--radius);border-left:3px solid var(--accent);font-size:0.9rem;color:var(--text2);line-height:1.7">
<p>{b["description"]} Explore the full lineup of {html.escape(b["name"])} models including {", ".join(c["model"] for c in b_cars[:3])} and more. Each model features detailed specs on horsepower, fuel economy, seating capacity, pricing, and body type to help you compare and choose.</p>
</div>
<div class="model-grid">'''

code = code.replace(old_hero, new_hero, 1)

# 2. Add car description section in build_car_page after the car-specs-card
old_specs = '''<div class="car-specs-card"><div class="car-specs-grid"><div class="car-spec"><div class="sv">{c["horsepower"]}</div><div class="sl">{ui["horsepower"]}</div></div><div class="car-spec"><div class="sv">{c["fuel"]}</div><div class="sl">{ui["fuel"]}</div></div><div class="car-spec"><div class="sv">{c["seats"]}</div><div class="sl">{ui["seats"]}</div></div><div class="car-spec"><div class="sv">{c["price"]}</div><div class="sl">{ui["price"]}</div></div><div class="car-spec"><div class="sv">{c["year"]}</div><div class="sl">{ui["year"]}</div></div><div class="car-spec"><div class="sv">{c["body"]}</div><div class="sl">{ui["body"]}</div></div></div></div>
<footer>'''

new_specs = '''<div class="car-specs-card"><div class="car-specs-grid"><div class="car-spec"><div class="sv">{c["horsepower"]}</div><div class="sl">{ui["horsepower"]}</div></div><div class="car-spec"><div class="sv">{c["fuel"]}</div><div class="sl">{ui["fuel"]}</div></div><div class="car-spec"><div class="sv">{c["seats"]}</div><div class="sl">{ui["seats"]}</div></div><div class="car-spec"><div class="sv">{c["price"]}</div><div class="sl">{ui["price"]}</div></div><div class="car-spec"><div class="sv">{c["year"]}</div><div class="sl">{ui["year"]}</div></div><div class="car-spec"><div class="sv">{c["body"]}</div><div class="sl">{ui["body"]}</div></div></div></div>
<div class="seo-extra" style="max-width:800px;margin:16px auto;padding:18px 24px;background:var(--surface2);border-radius:var(--radius);border-left:3px solid var(--accent);font-size:0.9rem;color:var(--text2);line-height:1.7">
<p>The <strong>{c["model"]}</strong> by <strong>{c["brand"]}</strong> is a {c["body"]} with {c["horsepower"]} HP, {c["fuel"]} fuel type, {c["seats"]} seats, and a price of {c["price"]}. Produced in {c["year"]}, this vehicle offers a compelling combination of performance, practicality, and value. Check detailed specifications including engine power, fuel economy, dimensions, and features to see how this model compares to others in its class.</p>
</div>
<footer>'''

code = code.replace(old_specs, new_specs, 1)

with open(os.path.join(BASE, "build.py"), "w", encoding="utf-8") as f:
    f.write(code)

print("Done: carbrands build.py updated")
