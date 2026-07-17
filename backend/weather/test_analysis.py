from backend.weather.analysis import analyze


def main():
    results = analyze(limit=5)

    for weather in results:
        print(weather)


if __name__ == "__main__":
    main()