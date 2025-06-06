from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    ENV_STATE: str | None = None


class GlobalConfig(BaseConfig):
    DATABASE_URL: str | None = None
    DB_FORCE_ROLL_BACK: bool = False


class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="DEV_")
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    REDIS_SERVER: str
    REDIS_PORT: str
    API_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_JWT_EXPIRED: int = 30  # minutes
    REFRESH_JWT_EXPIRED: int = 10080  # minutes


class TestConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="TEST_")
    DB_FORCE_ROLL_BACK: bool = True
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    REDIS_SERVER: str
    REDIS_PORT: str
    API_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_JWT_EXPIRED: int = 30  # minutes
    REFRESH_JWT_EXPIRED: int = 10080  # minutes


@lru_cache()
def get_config(env_state: str):
    configs = {"dev": DevConfig, "test": TestConfig}
    return configs[env_state]()


config = get_config(BaseConfig().ENV_STATE)
