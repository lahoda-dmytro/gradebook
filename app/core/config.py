from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "gradebook api"
    secret_key: str
    algorithm: str
    access_token: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()