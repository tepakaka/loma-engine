from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point

BOUNDARY_FILE = Path("data/boundaries/finland.geojson")


def main():
    finland = gpd.read_file(BOUNDARY_FILE)

    polygon = finland.geometry.union_all()

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

    print(f"Analysis points: {len(points)}")


if __name__ == "__main__":
    main()