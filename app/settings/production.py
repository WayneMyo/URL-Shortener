import os
from dotenv import load_dotenv
from app.settings.base import BaseSettings

load_dotenv()

class ProductionSettings(BaseSettings):
    @property
    def DATABASE_URL(self):
        return os.getenv("PROD_DATABASE_URL")

    @property
    def LOG_LEVEL(self):
        return "INFO"
