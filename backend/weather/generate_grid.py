from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point

from backend.weather.boundaries import load_finland_boundary

OUTPUT_FILE = Path("data/grids/finland_grid.geojson")


def main():
    polygon = load_finland_boundary()

    points = []

    step = 0.5

    lat = 59.5
    while lat <= 70.5:
        lon = 20.0
        while lon <= 32.0:
            point = Point(lon, lat)

            if polygon.contains(point):
                points.append(point)

            lon += step

        lat += step

    grid = gpd.GeoDataFrame(
        geometry=points,
        crs="EPSG:4326",
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    grid.to_file(OUTPUT_FILE, driver="GeoJSON")

    print(f"Analysis points: {len(points)}")
    print(f"Saved grid to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()