from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.database.models import FormPopulationODM
from app.settings import settings


class MongodbSessionManager:        
    async def __aenter__(self):
        self.client = AsyncIOMotorClient(settings.mongodb_url)
        await init_beanie(
            database=self.client.get_database(settings.MONGO_DATABASE),
            document_models=[FormPopulationODM],
        )

    async def __aexit__(self, *args):
        self.client.close()

