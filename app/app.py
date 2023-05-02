from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import ShortUrlNotFound

app = FastAPI()

@app.exception_handler(ShortUrlNotFound)
async def short_url_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Short URL not found"},
    )