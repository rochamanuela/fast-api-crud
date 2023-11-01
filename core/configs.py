from pydantic.v1 import BaseSettings #NEW
from sqlalchemy.orm import declarative_base
class Settings(BaseSettings):
    """
        general configurations used in our application
    """

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.2:3306/etscursos'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True        

settings = Settings()