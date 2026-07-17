from pathlib import Path

import geopandas as gpd

GRID_FILE = Path("data/grids/finland_grid.geojson")


def load_grid() -> gpd.GeoDataFrame:
    return gpd.read_file(GRID_FILE)