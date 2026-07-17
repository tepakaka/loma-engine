from backend.weather.grid import load_grid
from backend.weather.service import WeatherService
from backend.scoring.camping import camping_score
from backend.weather.models import AnalysisResult


def analyze(limit: int = 5):
    service = WeatherService()
    grid = load_grid()

    results = []

    for _, row in grid.head(limit).iterrows():
        point = row.geometry

        weather = service.get_weather(
            latitude=point.y,
            longitude=point.x,
        )

        results.append(
    AnalysisResult(
        latitude=weather.latitude,
        longitude=weather.longitude,
        temperature=weather.temperature,
        wind_speed=weather.wind_speed,
        cloud_cover=weather.cloud_cover,
        timestamp=weather.timestamp,
        camping_score=camping_score(weather),
    )
)

    return results