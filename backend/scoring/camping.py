from backend.weather.models import WeatherData


def camping_score(weather: WeatherData) -> int:
    score = 100

    # Lämpötila
    if weather.temperature < 15:
        score -= 40
    elif weather.temperature < 20:
        score -= 20
    elif weather.temperature > 30:
        score -= 15

    # Tuuli
    if weather.wind_speed > 12:
        score -= 25
    elif weather.wind_speed > 8:
        score -= 10

    # Pilvisyys
    if weather.cloud_cover > 80:
        score -= 15
    elif weather.cloud_cover > 50:
        score -= 5

    return max(score, 0)