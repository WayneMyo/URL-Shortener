import hashlib
import base64

"""
Utility functions for the URL shortener, including:

- generate_short_url: Takes the original URL and counter value as inputs and generates a shortened URL string.
"""

def generate_short_url(url: str, counter_value: int, length: int = 6) -> str:
    # Hash the original URL with SHA256
    sha256 = hashlib.sha256(url.encode('utf-8')).digest()

    # Concatenate the counter and the hash
    unique_id = f"{counter_value}{sha256}"

    # Encode the unique_id using Base62
    base62_encoded = base64.b62encode(unique_id.encode('utf-8'))
    short_url = base62_encoded.decode('utf-8')[:length]

    return short_url
