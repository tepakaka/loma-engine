from dataclasses import dataclass


@dataclass
class GridPoint:
    latitude: float
    longitude: float


def generate_finland_grid(
    min_lat=59.5,
    max_lat=70.5,
    min_lon=20.0,
    max_lon=32.0,
    step=1.0,
):
    """
    Luo säännöllisen ruudukon annetulle alueelle.
    """

    points = []

    lat = min_lat
    while lat <= max_lat:
        lon = min_lon
        while lon <= max_lon:
            points.append(GridPoint(round(lat, 4), round(lon, 4)))
            lon += step
        lat += step

    return points


if __name__ == "__main__":
    grid = generate_finland_grid()

    print(f"Grid contains {len(grid)} points:\n")

    for point in grid:
        print(point)