# Padrão do código, para a facilidade na codificação
from pydantic.v1 import BaseSettings 
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1' # padronizado a versão

    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3307/profissoes" # link do database, ou seja dependendo do modelo do banco essa parte é modificada
    # nome do banco no caso "profissoes"
    DBBaseModel = declarative_base()
    
class Config:
    case_sensitive = False # Pegando se a configurações da env está funcionando
    env_file = "env"
    
#  Parte mais importante do config

settings = Settings()