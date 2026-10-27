#!/usr/bin/env python3
"""Budapest Health Atlas: reproduce secondary, descriptive district contrasts.
Reads data/district_environment.csv. Standard library only. No clinical outcomes.
"""
from pathlib import Path
import csv
from statistics import mean

PATH = Path(__file__).resolve().parents[1] / "data" / "district_environment.csv"
with PATH.open(encoding="utf-8-sig", newline="") as f:
    data = list(csv.DictReader(f))
assert len(data) == 23, f"Expected 23 Budapest districts, got {len(data)}"
assert len({int(r["district_number"]) for r in data}) == 23

for row in data:
    for key in ("green_cover_pct", "rcp45_2041_2070", "rcp85_2041_2070"):
        row[key] = float(row[key])
ranked = sorted(data, key=lambda row: row["green_cover_pct"])
least_green, most_green = ranked[:6], ranked[-6:]

print("Budapest Health Atlas: unweighted six-district group means")
for metric in ("rcp45_2041_2070", "rcp85_2041_2070"):
    lo, hi = mean(r[metric] for r in least_green), mean(r[metric] for r in most_green)
    print(f"{metric}: least-green={lo:.2f}, greenest={hi:.2f}, difference={lo-hi:.2f}")
print("Least-green districts:", [int(r["district_number"]) for r in least_green])
print("Greenest districts:", [int(r["district_number"]) for r in most_green])
print("\nCaution: modeled threshold-frequency outputs, not observed hot days.")
print("Descriptive analysis only. The model already incorporates land-cover inputs.")
