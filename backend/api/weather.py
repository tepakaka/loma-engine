from fastapi import APIRouter

from backend.weather.service import WeatherService

router = APIRouter(prefix="/weather", tags=["Weather"])

service = WeatherService()


@router.get("")
def get_weather(lat: float, lon: float):
    return service.get_weather(lat, lon)