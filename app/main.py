import logging
from typing import Dict
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

from database import create_db
from app.app import app
from app.models import UrlStatus
from app.dependencies import get_db
from app.exceptions import ExpiredUrl, ShortUrlNotFound
from app.logging_config import setup_logging
from app.utils import get_short_url_for_original_url
from app.crud import get_original_url_by_short_url

"""
The main FastAPI application file, containing:

- UrlShortenRequest: Pydantic model for the request body containing the original URL.
- shorten_url: POST API endpoint to shorten the original URL and store it in the database.
- redirect_to_original: GET API endpoint to retrieve the original URL corresponding to a given shortened URL.
"""

create_db()
setup_logging()
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/v1")

class UrlShortenRequest(BaseModel):
    url: HttpUrl

@router.post("/shorten")
async def shorten_url(request: Request, url_request: UrlShortenRequest, db: Session = Depends(get_db)) -> Dict[str, str]:
    original_url = url_request.url
    logger.debug(f"Received request to shorten URL: {original_url}")

    short_url = get_short_url_for_original_url(db, original_url)

    logger.info(f"Shortened URL: {original_url} to {short_url}")
    version = request.scope['path'].split('/')[1]
    short_url_with_domain = f"{request.base_url}{version}/{short_url}"
    return {"short_url": short_url_with_domain}

@router.get("/{short_url}")
async def redirect_to_original(short_url: str, db: Session = Depends(get_db)):
    url = get_original_url_by_short_url(db, short_url)
    if url:
        if url.status == UrlStatus.ACTIVE:
            logger.info(f"Redirecting short URL {short_url} to {url.original_url}")
            return RedirectResponse(url.original_url)
        else:
            logger.warning(f"Short URL is expired: {short_url}")
            raise ExpiredUrl()
    else:
        logger.warning(f"Short URL not found: {short_url}")
        raise ShortUrlNotFound()

app.include_router(router)
