from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    API_KEY: str
    PDF_FOLDER_A: str
    PDF_FOLDER_E: str
    INDEX_PATH: str

    class Config :
        env_file = str(Path(__file__).parent.parent / ".env")


def get_settings():
    return Settings()