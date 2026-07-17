from pathlib import Path

import geopandas as gpd

URL = "https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip"

OUTPUT = Path("data/boundaries/finland.geojson")


def main():
    world = gpd.read_file(URL)
    finland = world[world["ADMIN"] == "Finland"]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    finland.to_file(OUTPUT, driver="GeoJSON")

    print(f"Saved Finland boundary to {OUTPUT}")


if __name__ == "__main__":
    main()
