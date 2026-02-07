from fastapi import FastAPI

app = FastAPI(title="Paw Project API")

@app.get("/health")
def health():
    return {"ok": True}

