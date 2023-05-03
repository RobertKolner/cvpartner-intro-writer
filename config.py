from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    cvpartner_api_key: str
    openai_api_key: str


env = Config()
cvpartner_domain = "noaignite.cvpartner.com"

__all__ = ["env", "cvpartner_domain", "logger"]
