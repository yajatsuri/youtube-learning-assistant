from app.database.base import Base
from app.database.database import engine

# Import all models so SQLAlchemy registers them
from app.models.note import Note
from app.models.flashcard import Flashcard


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


if __name__ == "__main__":
    init_db()
