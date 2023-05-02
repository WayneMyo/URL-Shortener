from database import SessionLocal

"""
Dependencies for the FastAPI application, including:

- get_db: A generator function that provides a database session for use in FastAPI endpoint functions and ensures that the session is properly closed after the request is finished.
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
