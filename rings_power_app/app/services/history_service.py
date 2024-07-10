from app.repositories.history_repository import HistoryRepository
from app.models.movie import Movie
from app.utils.db import get_redis_client

class HistoryService:
    async def save_search(self, movie: Movie, user: str):
        redis_client = get_redis_client()
        history_repository = HistoryRepository(redis_client)
        await history_repository.save_search(movie, user)
    
    async def get_search_history(self):
        redis_client = get_redis_client()
        history_repository = HistoryRepository(redis_client)
        return await history_repository.get_history()
