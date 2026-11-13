from pathlib import Path

from pydantic import MultiHostUrl, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DB_SERVER: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str

    @property
    @computed_field
    def DATABASE_URI(self) -> PostgresDsn:
        url = MultiHostUrl.build(  # type: ignore[attr-defined]
            scheme="postgresql+asyncpg",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_SERVER,
            port=self.DB_PORT,
            path="postgres",
        )
        return PostgresDsn(url)


settings = Settings()
