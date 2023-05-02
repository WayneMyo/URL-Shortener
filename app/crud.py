from sqlalchemy.orm import Session
from app.models import Counter, Url

"""
CRUD (Create, Read, Update, Delete) operations for the URL shortener, including:

- get_or_create_counter: A function to get the counter from the database, or create it if it doesn't exist.
- increment_and_get_counter: A function to increment the counter and return its value.
- get_short_url_by_original_url: A function to get the short URL for a given original URL.
- get_original_url_by_short_url: A function to get the original URL for a given short URL.
"""

def get_or_create_counter(db: Session) -> Counter:
    counter = db.query(Counter).first()
    if not counter:
        counter = Counter(value=0)
        db.add(counter)
        db.commit()
        db.refresh(counter)
    return counter

def increment_and_get_counter(db: Session) -> int:
    counter = get_or_create_counter(db)
    counter.value += 1
    db.commit()
    return counter.value

def get_short_url_by_original_url(db: Session, original_url: str) -> Url:
    return db.query(Url).filter(Url.original_url == original_url).first()

def get_original_url_by_short_url(db: Session, short_url: str) -> Url:
    return db.query(Url).filter(Url.short_url == short_url).first()
