from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from src.incident_finder_api.config import settings

engine = create_async_engine(
    str(settings.DATABASE_URI),
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


async def create_session():
    async with AsyncSessionLocal() as session:
        yield session
