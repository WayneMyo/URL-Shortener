from sqlalchemy.orm import Session
from app.models import Counter

"""
CRUD (Create, Read, Update, Delete) operations for the URL shortener, including:

- increment_and_get_counter: Increments the counter value in the database and returns the updated counter value.
"""

def increment_and_get_counter(db: Session) -> int:
    counter = db.query(Counter).first()
    if not counter:
        counter = Counter(value=1)
        db.add(counter)
    else:
        counter.value += 1
    db.commit()
    return counter.value
