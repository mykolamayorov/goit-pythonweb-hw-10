from fastapi import FastAPI
from app.api.contacts import router as contacts_router

app = FastAPI(title="Contacts REST API", version="1.0.0")

app.include_router(contacts_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Contacts API is running. Open /docs for Swagger UI"}