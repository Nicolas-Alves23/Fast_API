# Fazendo configurações internas do banco 

from sqlalchemy.orm import sessionmaker # vai fazer a sessão para nos
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)
Session: AsyncEngine = sessionmaker(
    autocommit=False, # O autocommit não vai acontecer, porém é possível deixar configurado no True 
    autoflush=False, # O autoflush funciona da mesma maneira da linha de cima                      
    expire_on_commit=False, 
    class_=AsyncSession,
    bind=engine
)