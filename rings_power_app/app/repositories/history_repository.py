from datetime import datetime
import pytz
from app.utils.logger import Logger

logger = Logger()

class HistoryRepository:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    async def save_search(self, movie, user):
        brasilia_tz = pytz.timezone('America/Sao_Paulo')
        current_time = datetime.now(brasilia_tz).strftime("%H:%M:%S - %Y/%m/%d")

        movie_data = {
            "user": user,
            "name": movie.name,
            "academyAwardWins": movie.academyAwardWins,
            "timestamp": current_time
        }
        self.redis_client.lpush("search_history", str(movie_data))
        logger.log(f"Salvando consulta do filme {movie.name} no histórico. Dados: {movie_data}")

    async def get_history(self):
        history = self.redis_client.lrange("search_history", 0, -1)
        movie_history = [eval(movie) for movie in history]
        logger.log("Buscando histórico de consultas.")
        return movie_history
