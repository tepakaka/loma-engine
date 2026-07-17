from backend.scoring.camping import camping_score
from backend.scoring.beach import beach_score
from backend.weather.models import WeatherData


def calculate_scores(weather: WeatherData) -> dict[str, int]:
    return {
        "camping": camping_score(weather),
        "beach": beach_score(weather),
    }