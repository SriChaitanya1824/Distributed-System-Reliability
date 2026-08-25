from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# Async SQLAlchemy setup
engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)  # Remove in production

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    """Async database session dependency"""
    async with AsyncSessionLocal() as session:
        yield session


async def connect():
    """Establish a connection to the database and ensure tables exist."""
    import app.models  # noqa: F401
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def disconnect():
    """Dispose of the database engine."""
    await engine.dispose()
