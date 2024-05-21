from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="postgres_", env_file=".env", extra="ignore"
    )

    host: str
    port: int
    db: str
    user: str
    password: str

    @property
    def url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        )

    echo: bool = True


db_settings = DBSettings()
