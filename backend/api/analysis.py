from fastapi import APIRouter

from backend.weather.analysis import analyze

router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.get("")
def get_analysis(limit: int = 20):
    return analyze(limit)
