from dataclasses import dataclass


@dataclass
class WeatherData:
    latitude: float
    longitude: float

    temperature: float
    wind_speed: float
    cloud_cover: int
    precipitation: float
    precipitation_probability: int
    relative_humidity: int

    timestamp: str


@dataclass
class AnalysisResult:
    name: str
    region: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    cloud_cover: int
    precipitation: float
    precipitation_probability: int
    relative_humidity: int
    timestamp: str
    scores: dict[str, int]


@dataclass
class Location:
    name: str
    region: str
    latitude: float
    longitude: float
    activities: list[str]
