from pydantic import BaseSettings


class Setting(BaseSettings):
    app_name: str = "Awesome RestFull API"
    admin_semail: str

    class Config:
        env_file = ".env"
