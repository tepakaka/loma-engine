import json
from pathlib import Path

from backend.weather.models import Location


DATA_FILE = Path(__file__).parent / "locations.json"


def load_locations() -> list[Location]:
    with open(DATA_FILE, encoding="utf-8") as file:
        data = json.load(file)

    return [
        Location(
            name=item["name"],
            region=item["region"],
            latitude=item["latitude"],
            longitude=item["longitude"],
            activities=item["activities"],
        )
        for item in data
    ]