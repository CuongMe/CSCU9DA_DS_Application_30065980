from pathlib import Path

import geopandas as gpd


script_dir = Path(__file__).resolve().parent
project_dir = script_dir.parent
source = project_dir / "shared_data/study_data/files/training_area/siatka100_python.shp"
output = script_dir / "training_data.xlsx"

training = gpd.read_file(source, ignore_geometry=True)
training.to_excel(output, index=False, sheet_name="Training data")

print(f"Saved {len(training):,} training rows to {output}")
