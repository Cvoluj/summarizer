from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    """
    ServersSettings class is used for loading .env, but with pydantic-settings lib
    working with .env feels much better, also this class is cool for creating differents paths from .env
    
    f. e. we can create method that returns strings with env variables 
    @property
    def DB_URL():
        ...
        
    and than use this like connections string
    """
    
    
    PY_PORT: int  # we can define port from .env file
    
    model_config = SettingsConfigDict(env_file='.env')


server_setting = ServerSettings()