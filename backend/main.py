from fastapi import FastAPI

app = FastAPI(title="Loma Engine")


@app.get("/")
def root():
    return {
        "message": "Welcome to Loma Engine"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Loma Engine"
    }