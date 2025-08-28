from pydantic_settings import BaseSettings

class Env(BaseSettings):
    CLOVASTUDIO_API_KEY: str
    
    class Config:
        env_file = ".env"

env = Env()
