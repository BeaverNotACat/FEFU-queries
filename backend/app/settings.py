from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    JWT_SECRET: str

    MONGO_HOST: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str

    @cached_property
    def mongodb_url(self):
        return f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}"#"/{self.MONGO_DATABASE}"


settings = Settings()  # type: ignore
