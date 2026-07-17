from pathlib import Path

import geopandas as gpd

BOUNDARY_FILE = Path("data/boundaries/finland.geojson")


def load_finland_boundary():
    finland = gpd.read_file(BOUNDARY_FILE)
    return finland.geometry.union_all()