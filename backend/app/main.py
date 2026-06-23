from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

setup_logging()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
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
