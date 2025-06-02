from redis.asyncio import Redis

from app.config.settings import config


class RedisClient:
    """Asynchronous Redis client for key-value operations.

    Attributes:
        redis (redis.asyncio.Redis): Redis connection instance.
    """

    def __init__(self):
        self.redis = None

    async def connect(self):
        """Establish a connection to the Redis server."""
        self.redis = Redis(
            host=config.REDIS_SERVER,
            port=config.REDIS_PORT,
            decode_responses=True,
            db=1,
        )

    async def close(self):
        """Close the Redis connection if it exists."""
        if self.redis:
            await self.redis.aclose()

    async def set(self, key, value, ttl=None):
        """Set a key-value pair in Redis.

        Args:
            key (str): The key to set.
            value (str): The value to associate with the key.
            ttl (int, optional): Time to live in seconds. Defaults to None.
        """
        await self.redis.set(key, value, ex=ttl)

    async def get(self, key):
        """Retrieve the value associated with a key from Redis.

        Args:
            key (str): The key to retrieve.

        Returns:
            str: The value associated with the key, or None if not found.
        """
        return await self.redis.get(key)

    async def delete(self, key):
        """Delete a key from Redis.

        Args:
            key (str): The key to delete.
        """
        await self.redis.delete(key)


redis_client = RedisClient()
