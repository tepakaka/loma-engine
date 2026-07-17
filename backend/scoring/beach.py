from backend.weather.models import WeatherData


def beach_score(weather: WeatherData) -> int:
    score = 100

    # Lämpötila
    if weather.temperature < 20:
        score -= 40
    elif weather.temperature < 24:
        score -= 15

    # Tuuli
    if weather.wind_speed > 10:
        score -= 10
    if weather.wind_speed > 15:
        score -= 15

    # Pilvisyys
    if weather.cloud_cover > 50:
        score -= 15
    if weather.cloud_cover > 80:
        score -= 20

    # Sade
    if weather.precipitation > 0:
        score -= 30

    # Sateen todennäköisyys
    if weather.precipitation_probability > 50:
        score -= 20

    return max(0, min(score, 100))
