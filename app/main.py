from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.routers.post import router as post_router
from app.db import get_db
from app.config import Settings

app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION,
              description=Settings.PROJECT_DESCRIPTION,
              openapi_url=Settings.OPENAPI_URL)


@app.get("/ping", tags=['Check'], response_model=str)
async def ping(db: Session = Depends(get_db)):
    return "I'm alive"

app.include_router(post_router)
