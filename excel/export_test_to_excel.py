from pathlib import Path

import geopandas as gpd


script_dir = Path(__file__).resolve().parent
project_dir = script_dir.parent
source = project_dir / "shared_data/study_data/files/test_area/ldz_siatka100_dla_ann_python.shp"
output = script_dir / "test_data.xlsx"

test_data = gpd.read_file(source, ignore_geometry=True)
test_data.to_excel(output, index=False, sheet_name="Test data")

print(f"Saved {len(test_data):,} test rows to {output}")
