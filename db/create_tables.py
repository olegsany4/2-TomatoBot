import asyncio
from db.models import Base
from db.session import async_engine

async def create_all():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("All tables created.")

if __name__ == "__main__":
    asyncio.run(create_all())
