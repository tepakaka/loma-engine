from backend.data.locations import load_locations
from backend.scoring.engine import calculate_scores
from backend.weather.models import AnalysisResult
from backend.weather.service import WeatherService


def analyze(limit: int = 5):
    service = WeatherService()
    locations = load_locations()

    results = []

    for location in locations[:limit]:
        weather = service.get_weather(
            latitude=location.latitude,
            longitude=location.longitude,
        )

        scores = calculate_scores(weather)

        results.append(
            AnalysisResult(
                name=location.name,
                region=location.region,
                latitude=weather.latitude,
                longitude=weather.longitude,
                temperature=weather.temperature,
                wind_speed=weather.wind_speed,
                cloud_cover=weather.cloud_cover,
                precipitation=weather.precipitation,
                precipitation_probability=weather.precipitation_probability,
                relative_humidity=weather.relative_humidity,
                timestamp=weather.timestamp,
                scores=scores,
            )
        )

    return results
