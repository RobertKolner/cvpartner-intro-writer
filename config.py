from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    cvpartner_api_key: str
    openai_api_key: str


env = Config()


__all__ = ["env"]
