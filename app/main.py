import logging
from logging_config import setup_logging
from typing import Dict
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

from app import app
from app.models import Url
from app.crud import increment_and_get_counter
from app.utils import generate_short_url
from app.dependencies import get_db
from app.exceptions import ShortUrlNotFound

"""
The main FastAPI application file, containing:

- UrlShortenRequest: Pydantic model for the request body containing the original URL.
- shorten_url: POST API endpoint to shorten the original URL and store it in the database.
- redirect_to_original: GET API endpoint to retrieve the original URL corresponding to a given shortened URL.
"""

setup_logging()
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1")

class UrlShortenRequest(BaseModel):
    url: HttpUrl

@router.post("/shorten")
async def shorten_url(request: UrlShortenRequest, db: Session = Depends(get_db)) -> Dict[str, str]:
    original_url = request.url
    logger.debug(f"Received request to shorten URL: {original_url}")

    counter_value = increment_and_get_counter(db)
    short_url = generate_short_url(original_url, counter_value)

    new_url = Url(original_url=original_url, short_url=short_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    logger.info(f"Shortened URL: {original_url} to {short_url}")
    return {"short_url": f"{short_url}"}

@router.get("/{short_url}")
async def redirect_to_original(short_url: str, db: Session = Depends(get_db)):
    url = db.query(Url).filter(Url.short_url == short_url).first()
    if url:
        logger.info(f"Redirecting short URL {short_url} to {url.original_url}")
        return {"original_url": url.original_url}
    else:
        logger.warning(f"Short URL not found: {short_url}")
        raise ShortUrlNotFound()

app.include_router(router)
