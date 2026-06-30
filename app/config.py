from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    #LLM Config
    NVIDIA_API_KEY: str
    Primary_model: str = "meta/llama-3.1-70b-instruct"
    fallback_model: str = "meta/llama-3.1-70b-instruct"


    #Langsmith
    langchain_tracing_v2: bool =True
    langcahin_api_key: str = ""
    langchain_project: str ="Production-API"

    #Application
    app_env: str = "development"
    log_level: str ="INFO"
    rate_limit: str = "20/minute"
    cache_ttl_seconds: int = 300
    max_retries: int =3

    model_config = {"env_fie": ".env", "extra": "ignore"}

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"
    
@lru_cache
def get_settings() -> Settings:
    """ Cached setting instance - loaded once, reused everywhere."""
    return Settings()
