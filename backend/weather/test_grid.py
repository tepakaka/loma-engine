from backend.weather.grid import load_grid


def main():
    grid = load_grid()

    print(grid.head())
    print()
    print(f"Points: {len(grid)}")


if __name__ == "__main__":
    main()
