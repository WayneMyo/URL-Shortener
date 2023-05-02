from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from database import Base
from datetime import timedelta

"""
SQLAlchemy models for the URL shortener, including:

- Counter: The table to store the counter value.
- Url: The table to store the original URL and its corresponding shortened URL.
"""

class Counter(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False, default=0)

class UrlStatus(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, index=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False, default=lambda: func.current_timestamp() + timedelta(days=7)) # Default expiration date is 7 days from the current date
    status = Column(Enum(UrlStatus), default=UrlStatus.ACTIVE, nullable=False) # Default status is active
