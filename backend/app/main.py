from fastapi import FastAPI

from app.api.routes.resume import router as resume_router
from app.utils.logger import logger

app = FastAPI()

app.include_router(resume_router)

logger.info("Resume Intelligence Platform started successfully.")


@app.get("/")
def root():
    return {"message": "Resume Intelligence Platform"}