import geopandas as gpd

URL = "https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip"


def main():
    world = gpd.read_file(URL)

    finland = world[world["ADMIN"] == "Finland"]

    print(finland[["ADMIN", "CONTINENT"]])
    print()
    print(finland.geometry.iloc[0].geom_type)


if __name__ == "__main__":
    main()