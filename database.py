from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

"""
Database configuration and table creation for the URL shortener, including:

- engine: The SQLAlchemy engine connected to the SQLite database.
- SessionLocal: The session factory for creating database sessions.
- Base: The base class for SQLAlchemy models.
- create_tables: A function to create the tables in the SQLite database.
"""

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    from app.models import Counter, Url  # Import models here to avoid circular import issues
    Base.metadata.create_all(bind=engine)
