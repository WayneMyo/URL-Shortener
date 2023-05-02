from sqlalchemy import Column, Integer, String
from database import Base

"""
SQLAlchemy models for the URL shortener, including:

- Counter: The table to store the counter value.
- Url: The table to store the original URL and its corresponding shortened URL.
"""


class Counter(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False, default=0)

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, index=True, nullable=False)
