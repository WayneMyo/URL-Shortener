from fastapi import HTTPException

class ShortUrlNotFound(HTTPException):
    """Raised when a short URL is not found in the database."""

    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Short URL not found",
        )
