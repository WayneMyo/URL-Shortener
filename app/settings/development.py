import os
from dotenv import load_dotenv
from app.settings.base import BaseSettings

load_dotenv()

class DevelopmentSettings(BaseSettings):
    @property
    def DATABASE_URL(self):
        return os.getenv("DEV_DATABASE_URL")

    @property
    def LOG_LEVEL(self):
        return "DEBUG"
