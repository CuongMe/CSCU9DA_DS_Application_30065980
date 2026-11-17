from pathlib import Path

import geopandas as gpd


script_dir = Path(__file__).resolve().parent
project_dir = script_dir.parent
source = project_dir / "shared_data/study_data/files/apply_area/rz_siatka100_dla_ann_python.shp"
output = script_dir / "apply_data.xlsx"

apply_data = gpd.read_file(source, ignore_geometry=True)
apply_data.to_excel(output, index=False, sheet_name="Apply data")

print(f"Saved {len(apply_data):,} apply rows to {output}")
