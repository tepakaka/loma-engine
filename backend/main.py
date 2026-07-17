from fastapi import FastAPI

from backend.api.weather import router as weather_router
from backend.api.analysis import router as analysis_router

app = FastAPI(title="Loma Engine API")

app.include_router(weather_router)
app.include_router(analysis_router)


@app.get("/")
def root():
    return {"message": "Loma Engine API"}