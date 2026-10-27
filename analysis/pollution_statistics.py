#!/usr/bin/env python3
"""Descriptive, noncausal ecological comparisons across Budapest's 23 districts.
Run from repository root: python analysis/pollution_statistics.py
Uses only Python standard library and files committed to this repository.
"""
import csv, json
from pathlib import Path
from statistics import mean
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    with (ROOT/path).open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))
p=load("data/air_pollution_by_district.csv")
v=load("data/district_environment.csv")
byv={int(x["district_number"]):x for x in v}
assert len(p)==len(v)==23
rows=[]
for r in p:
    n=int(r["district_number"])
    assert n in byv and r["pm25_status"]=="usable" and r["no2_status"]=="usable"
    rows.append(dict(district=n,pm25=float(r["pm25_ug_m3"]),no2=float(r["no2_ug_m3"]),green=float(byv[n]["green_cover_pct"])))
assert {r["district"] for r in rows}==set(range(1,24))
def correl(a,b):
    ma,mb=mean(a),mean(b)
    numerator=sum((x-ma)*(y-mb) for x,y in zip(a,b))
    denominator=(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))**0.5
    return numerator/denominator
def ranks(arr):
    return [1+sum(y<x for y in arr)+(sum(y==x for y in arr)-1)/2 for x in arr]
def stats(metric):
    a=[r["green"] for r in rows]
    b=[r[metric] for r in rows]
    return dict(pearson_r=round(correl(a,b),4),spearman_rho=round(correl(ranks(a),ranks(b)),4),
                district_unweighted_mean=round(mean(b),3),min=round(min(b),3),max=round(max(b),3))
lo=sorted(rows,key=lambda r:r["green"])[:6]
hi=sorted(rows,key=lambda r:r["green"])[-6:]
out=dict(n=23,units="µg/m³",year_status="EEA Environmental Health Atlas labels layers as 2023; service-layer-specific metadata not independently audited",
         aggregation="area-weighted mapped concentration within district; then equal-weight district comparison",
         vegetation_year_note="Vegetation input predates the pollution maps (around 2015–2017 versus EEA-labeled 2023).",
         pm25=stats("pm25"),no2=stats("no2"),
         pm25_no2_pearson_r=round(correl([r["pm25"] for r in rows],[r["no2"] for r in rows]),4),
         low_vegetation_six=sorted(r["district"] for r in lo),high_vegetation_six=sorted(r["district"] for r in hi),
         groups={k:{"least_green_mean":round(mean(r[k] for r in lo),4),
                    "most_green_mean":round(mean(r[k] for r in hi),4),
                    "difference":round(mean(r[k] for r in lo)-mean(r[k] for r in hi),4)} for k in ("pm25","no2")},
         caveats=["Descriptive ecological associations, not causal effects","District observations spatially autocorrelated",
                  "No population weighting, individual exposure, patient outcome data, or socioeconomic adjustment",
                  "PM2.5/NO2 are modeled gridded estimates; NOT 23 measured station averages",
                  "Vegetation layer is from an earlier reference period"])
print(json.dumps(out,ensure_ascii=False,indent=2))
