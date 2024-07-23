from motor.motor_asyncio import AsyncIOMotorClient

from app.settings import settings


def mongodb_session_factory():
    return AsyncIOMotorClient(settings.mongodb_url)
