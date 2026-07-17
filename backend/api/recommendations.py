from fastapi import APIRouter

from backend.weather.analysis import analyze

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.get("/")
def get_recommendations(
    limit: int = 20,
    activity: str = "camping",
):
    results = analyze(limit)

    return sorted(
        results,
        key=lambda result: result.scores.get(activity, 0),
        reverse=True,
    )
