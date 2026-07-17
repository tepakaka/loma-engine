from backend.weather.models import WeatherData
from backend.weather.providers.openmeteo import get_weather


class WeatherService:
    def get_weather(self, latitude: float, longitude: float) -> WeatherData:
        return get_weather(latitude, longitude)