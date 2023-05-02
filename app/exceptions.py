from fastapi import HTTPException

class ExpiredUrl(HTTPException):
    """Raised when a short URL has expired."""

    def __init__(self):
        super().__init__(
            status_code=410,
            detail="Short URL has expired",
        )

class ShortUrlNotFound(HTTPException):
    """Raised when a short URL is not found in the database."""

    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Short URL not found",
        )
