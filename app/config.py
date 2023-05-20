from pydantic import BaseSettings, Field
# BaseSettings is a pydantic class to do the validation
# ... three dots in pydantic is None
# this file config.py is there because we are settings some configurations here
# sql alchemy - take sql queries as python inputs and then convert them into sql commands


class postgresSettings(BaseSettings):
    POSTGRES_DB_NAME: str = Field(..., env = "POSTGRES_DB_NAME")
    POSTGRES_USER:str = Field(..., env = "POSTGRES_USER")
    POSTGRES_PASSWORD:str = Field(..., env = "POSTGRES_PASSWORD")
    POSTGRES_HOST:str = Field(..., env = "POSTGRES_HOST")
    POSTGRES_PORT:str = Field(..., env = "POSTGRES_PORT")

    class Config:
        env_file= '.env'

def get_postgres_settings():
    return postgresSettings()

