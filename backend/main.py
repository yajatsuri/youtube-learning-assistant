yajatsuri@Yajats-MacBook-Air frontend % cd ~/youtube-learning-assistant/backend

source venv/bin/activate

uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/yajatsuri/youtube-learning-assistant/backend']
ERROR:    [Errno 48] Address already in use
(venv) yajatsuri@Yajats-MacBook-Air backend % cat app/main.py
from app.middleware.logging_middleware import (
    logging_middleware
)
from fastapi import FastAPI
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
(venv) yajatsuri@Yajats-MacBook-Air backend % 

