from pydantic import BaseSettings


class Settings(BaseSettings):
    QUEUE_HOST: str
    QUEUE_NAME: str
    NUMBER_KEY_1: str
    NUMBER_KEY_2: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
