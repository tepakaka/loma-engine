from backend.scoring.beach import beach_score
from backend.weather.models import WeatherData


def test_beach_score_perfect_weather():
    weather = WeatherData(
        latitude=60,
        longitude=25,
        temperature=27,
        wind_speed=4,
        cloud_cover=5,
        precipitation=0,
        precipitation_probability=0,
        relative_humidity=50,
        timestamp="2026-07-17T12:00",
    )

    assert beach_score(weather) == 100
