from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "message": f"{settings.PROJECT_NAME} Başarıyla Çalışıyor!"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}