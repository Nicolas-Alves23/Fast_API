from core.configs import settings
from core.database import engine
from Models import all_model

async def create_tables() -> None:
    print("Creating tables...")
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        
    print("Creating tables sucefully")
    
if __name__ == "__main__":
    import asyncio
    
    asyncio.run(create_tables())