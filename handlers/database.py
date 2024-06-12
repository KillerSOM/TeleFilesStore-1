from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database as PyMongoDatabase

class Database:
    def __init__(self, database_url: str, database_name: str):
        if not isinstance(database_url, str) or not isinstance(database_name, str):
            raise TypeError("database_url and database_name must be instances of str")

        self._client = AsyncIOMotorClient(database_url)
        self.db = self._client[database_name]

# Usage example:
from configs.config import Config

try:
    db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
except TypeError as e:
    print(f"Configuration error: {e}")
