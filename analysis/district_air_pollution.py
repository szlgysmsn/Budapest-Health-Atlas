#!/usr/bin/env python3
"""Budapest Health Atlas: exact polygon-overlap area means of EEA 1-km PM2.5 / NO2.
No generated concentrations, station proxies, medical outcomes, or unsupported rankings.
"""
import csv
import datetime as dt
import json
import math
from pathlib import Path
import requests
from shapely.geometry import shape
from shapely.ops import transform
from pyproj import Transformer

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://trial.discomap.eea.europa.eu/arcgis/rest/services/EnvHealthAtlas/European_Capitals_2D/MapServer'
LAYERS = {'pm25':(0,'PM_25'), 'no2':(5,'NO_2')}
OUT = ROOT / 'data' / 'air_pollution_by_district.csv'
SUMMARY = ROOT / 'data' / 'air_pollution_analysis_summary.json'
REPORT = ROOT / 'AIR_POLLUTION_REPORT.md'
TX = Transformer.from_crs('EPSG:4326','EPSG:3035',always_xy=True).transform
S = requests.Session()
S.headers.update({'User-Agent':'BudapestHealthAtlas/1.0 educational analysis'})

def get(url, params):
    res=S.get(url, params=params, timeout=100)
    res.raise_for_status()
    obj=res.json()
    if 'error' in obj: raise RuntimeError('EEA ArcGIS service error: '+str(obj['error']))
    return obj

def get_districts():
    out={}
    for sub in ('01_06','07_12','13_18','19_23'):
        file=ROOT/'data'/('district_boundaries_'+sub+'.geojson')
        for feat in json.loads(file.read_text(encoding='utf-8'))['features']:
            id=int(feat['properties']['district_number'])
            poly=shape(feat['geometry'])
            if not poly.is_valid: poly=poly.buffer(0)
            assert poly.is_valid and not poly.is_empty
            out[id]={'name':feat['properties']['name'], 'geom':transform(TX,poly)}
    assert len(out)==23 and set(out)==set(range(1,24))
    return out

def get_cells(layer, field):
    params={'where':'1=1', 'geometry':'18.82,47.31,19.46,47.69',
            'geometryType':'esriGeometryEnvelope', 'inSR':4326,
            'spatialRel':'esriSpatialRelIntersects', 'outSR':4326,
            'outFields':'OBJECTID,'+field+',CNTR_CODE',
            'returnGeometry':'true','f':'geojson',
            'resultRecordCount':1500,'resultOffset':0}
    out=[];seen=set()
    while True:
        data=get(BASE+'/'+str(layer)+'/query',params)
        batch=data.get('features')
        if not isinstance(batch,list): raise RuntimeError('Unexpected EEA format: '+str(data)[:400])
        for feat in batch:
            p=feat.get('properties') or {}
            val=p.get(field)
            if val is None or p.get('CNTR_CODE') not in (None,'HU'): continue
            val=float(val)
            if not math.isfinite(val) or val<0: continue
            id=p.get('OBJECTID') or feat.get('id')
            if id is not None and id in seen: continue
            if id is not None: seen.add(id)
            if not feat.get('geometry'): continue
            g=shape(feat['geometry'])
            if not g.is_valid: g=g.buffer(0)
            if g.is_empty:continue
            out.append((transform(TX,g),val))
        params['resultOffset']+=len(batch)
        if len(batch)<1500:break
        if params['resultOffset']>12000:raise RuntimeError('Unexpected number of grid records')
    if len(out)<100: raise RuntimeError('Only '+str(len(out))+' mapped cells for '+field)
    return out

def compute(districts,cells):
    data={}
    for id,item in districts.items():
        geom=item['geom'];num=0.;area=0.;hits=0
        for poly,val in cells:
            if not geom.intersects(poly): continue
            overlap=geom.intersection(poly).area
            if overlap<1:continue
            hits+=1;area+=overlap;num+=overlap*val
        cover=area/geom.area if geom.area else 0
        usable=.85<=cover<=1.10 and hits>=2
        data[id]={'value':round(num/area,3) if area and usable else None,
                  'coverage':round(cover,4),'grid_cells':hits,
                  'status':'usable' if usable else 'insufficient_coverage'}
    return data

def main():
    districts=get_districts();analysis={};cell_counts={}
    for pollutant,(layer,field) in LAYERS.items():
        print('Retrieving '+pollutant+' from EEA',flush=True)
        cells=get_cells(layer,field)
        print('Fetched '+str(len(cells))+' grid polygons',flush=True)
        cell_counts[pollutant]=len(cells)
        analysis[pollutant]=compute(districts,cells)
    table=[]
    for id in sorted(districts):
        a,b=analysis['pm25'][id],analysis['no2'][id]
        table.append({'district_number':id,'district':districts[id]['name'],
           'pm25_ug_m3':a['value'],'no2_ug_m3':b['value'],
           'pm25_area_coverage':a['coverage'],'no2_area_coverage':b['coverage'],
           'pm25_grid_cells':a['grid_cells'],'no2_grid_cells':b['grid_cells'],
           'pm25_status':a['status'],'no2_status':b['status']})
    OUT.parent.mkdir(exist_ok=True,parents=True)
    with OUT.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=table[0].keys());writer.writeheader();writer.writerows(table)
    summary={'retrieved_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
         'source_map_service':BASE,'layers':LAYERS,
         'reference_year':'Undetermined service-layer vintage; EEA Health Atlas describes 2023 maps. Verify before assigning year.',
         'aggregation':'Intersection-area weighted mean, projected in equal-area EPSG:3035',
         'units':'annual mean micrograms per cubic meter (µg/m3), mapped surface',
         'method_limitations':['Not population-weighted or personal exposures','Does not measure health outcomes',
             'Values are derived from interpolated European-scale surfaces',
             'Districts with <85% geometry overlap are excluded',
             'Data-vintage verification remains outstanding'],
         'cells_retrieved':cell_counts,
         'districts_with_valid_estimate':{p:sum(analysis[p][id]['value'] is not None for id in districts) for p in LAYERS}}
    SUMMARY.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    md=['# Air pollution across Budapest districts — exploratory zonal analysis','',
      'Research method: Overlay EEA Health Atlas air pollution map-cell polygons with real Budapest district boundaries and compute intersection-area weighted means in EPSG:3035. Units: µg/m³.',
      '', '**Important:** Source map service vintage needs independent verification before attributing results to a calendar year. The EEA Health Atlas discusses 2023 maps, but service layer metadata need cross-checking.',
      '', 'These are mapped-model district **area means**, not 23 independent sets of measured station data, patient exposure, personal health risk, actual disease rates, or regulatory compliance.',
      '', '## Coverage and mapped estimates','',
      '| District | PM2.5 (µg/m³) | Coverage | NO₂ (µg/m³) | Coverage |',
      '|---|---:|---:|---:|---:|']
    for r in table:
        pm='—' if r['pm25_ug_m3'] is None else format(r['pm25_ug_m3'],'.2f')
        no='—' if r['no2_ug_m3'] is None else format(r['no2_ug_m3'],'.2f')
        md.append('| '+str(r['district_number'])+' '+r['district']+' | '+pm+' | '+format(r['pm25_area_coverage'],'.1%')+' | '+no+' | '+format(r['no2_area_coverage'],'.1%')+' |')
    md+=['', '## Interpretation and limitations','',
       'Areas with lower street vegetation or higher traffic may have higher mapped concentrations, but this analysis cannot establish cause-and-effect or individual medical consequences.',
       'Each district is a land-area aggregation of 1-km mapped source cells. Population weighting, pedestrian exposure, street canyons, fine-scale traffic, uncertainty bounds and seasonal contrasts are not computed.',
       'Source methodology: EEA Environmental Health Atlas raster/polygon map inputs. Mapped values must not be equated to regulatory monitoring-site exceedances.',
       'Coverage under 85% results in a missing value, not a guessed estimate. Coverage above 110% also fails as a potential overlap issue.',
       '', '## Source URLs', '', BASE, 'https://discomap.eea.europa.eu/atlas/?page=Air-pollution',
       'https://sdi.eea.europa.eu/catalogue/datahub/api/records/57807f24-25dc-4df3-9468-dcff8cee5468',
       'https://github.com/integralvision/geo-data-hungary','']
    REPORT.write_text('\n'.join(md),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__':main()
