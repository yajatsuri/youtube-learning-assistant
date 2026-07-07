from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.init_db import init_db

from app.middleware.logging_middleware import (
    logging_middleware
)

from app.exceptions.handlers import (
    register_exception_handlers
)

from app.core.logger import (
    setup_logging
)

from app.routes.youtube import (
    router as youtube_router
)

# NEW
//from app.routes.audio import (
  //  router as audio_router
//)

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://youtube-learning-assistant-frontend-c92b.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(
    logging_middleware
)

register_exception_handlers(app)


@app.get("/")
def home():
    return {
        "message": "YouTube Learning Assistant API"
    }


app.include_router(
    youtube_router
)

//# NEW
//app.include_router(
//    audio_router
//)
