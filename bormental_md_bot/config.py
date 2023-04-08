from typing import Optional

from pydantic import BaseSettings, PostgresDsn, RedisDsn, validator, SecretStr


class Config(BaseSettings):
    bot_token: str
    postgres_dsn: PostgresDsn
    app_host: Optional[str] = "0.0.0.0"
    app_port: Optional[int] = 9000
    webhook_domain: Optional[str]
    webhook_path: Optional[str]

    @classmethod
    @validator("webhook_path")
    def validate_webhook_path(cls, v, values):
        if values["webhook_domain"] and not v:
            raise ValueError("Webhook path is missing!")
        return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config: Config = Config()
