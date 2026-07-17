from backend.weather.service import WeatherService


def main():
    service = WeatherService()

    weather = service.get_weather(65.0121, 25.4651)

    print(weather)


if __name__ == "__main__":
    main()
