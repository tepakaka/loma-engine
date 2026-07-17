import requests

from backend.weather.models import WeatherData

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(latitude: float, longitude: float) -> WeatherData:
    response = requests.get(
        BASE_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "wind_speed_10m,"
                "cloud_cover,"
                "precipitation,"
                "precipitation_probability,"
                "relative_humidity_2m"
            ),
        },
        timeout=30,
    )

    response.raise_for_status()

    current = response.json()["current"]

    return WeatherData(
        latitude=latitude,
        longitude=longitude,
        temperature=current["temperature_2m"],
        wind_speed=current["wind_speed_10m"],
        cloud_cover=current["cloud_cover"],
        precipitation=current["precipitation"],
        precipitation_probability=current["precipitation_probability"],
        relative_humidity=current["relative_humidity_2m"],
        timestamp=current["time"],
    )