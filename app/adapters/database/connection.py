from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.database.models import FormPopulationODM
from app.settings import settings


async def mongodb_session_factory():
    client = AsyncIOMotorClient(settings.mongodb_url)
    await init_beanie(
        database=client.get_database(settings.MONGO_DATABASE),
        document_models=[FormPopulationODM]
    )
