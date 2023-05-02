import hashlib
import base64
from sqlalchemy.orm import Session
from app.models import Url
from app.crud import increment_and_get_counter, get_short_url_by_original_url

"""
Utility functions for the URL shortener, including:
- get_short_url_for_original_url: A function to get the short URL for a given original URL.
- generate_short_url: A function to generate a short URL for a given original URL.
"""

def get_short_url_for_original_url(db: Session, original_url: str) -> str:
    """
    Check if an original URL already exists in the database, and return its corresponding short URL.
    If not, generate a new short URL and store it in the database.
    """
    existing_url = get_short_url_by_original_url(db, original_url)
    if existing_url:
        return existing_url.short_url

    counter_value = increment_and_get_counter(db)
    short_url = generate_short_url(original_url, counter_value)
    
    new_url = Url(original_url=original_url, short_url=short_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    
    return short_url

def generate_short_url(url: str, counter_value: int, length: int = 6) -> str:
    """
    The default length value is 6. Since the Base64 encoding uses 64 unique characters, 
    there are 64^6 possible combinations of short URLs, which results in 68,719,476,736 unique short URLs.
    """

    # Hash the original URL with SHA256
    sha256 = hashlib.sha256(url.encode('utf-8')).digest()

    # Concatenate the counter and the hash
    unique_id = f"{counter_value}{sha256}"

    # Encode the unique_id using Base64
    base64_encoded = base64.urlsafe_b64encode(unique_id.encode('utf-8')).decode('utf-8')
    # Remove padding characters
    base64_encoded = base64_encoded.rstrip('=')

    short_url = base64_encoded[:length]

    return short_url
