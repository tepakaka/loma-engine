from dataclasses import dataclass


@dataclass
class WeatherData:
    latitude: float
    longitude: float

    temperature: float
    wind_speed: float
    cloud_cover: int

    timestamp: str