from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from urllib.parse import quote_plus

env_file = os.path.join(os.path.dirname(__file__), "../../../.env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, extra="ignore")

    ## jwt
    jwt_sec_key: str = Field(alias="SECRET_KEY")
    jwt_algo: str = Field(alias="ALGORITHM")
    # 30 min = 30 * 60 sec
    jwt_token_expire: float = Field(
        alias="ACCESS_TOKEN_EXPIRE_MINUTES", default=30 * 60
    )

    ## Database
    db_user: str = Field(alias="DB_USER")
    db_pass: str = Field(alias="DB_PASS")
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "smart_todo"

    @property  # allows methods to be accessed as attribute
    def db_url(self) -> str:
        return f"postgresql://{quote_plus(self.db_user)}:{quote_plus(self.db_pass)}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()

if __name__ == "__main__":
    print(Settings().model_dump())
    print(str(Settings().db_url))
