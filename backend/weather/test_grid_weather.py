from backend.weather.grid import load_grid
from backend.weather.service import WeatherService


def main():
    service = WeatherService()
    grid = load_grid()

    for index, row in grid.head(5).iterrows():
        point = row.geometry

        weather = service.get_weather(
            latitude=point.y,
            longitude=point.x,
        )

        print(f"Point {index}")
        print(weather)
        print("-" * 50)


if __name__ == "__main__":
    main()
