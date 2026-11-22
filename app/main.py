from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/healthz")
def read_root():
    return {"message": "Server working as expected."}
