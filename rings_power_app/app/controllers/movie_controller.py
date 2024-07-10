from fastapi import APIRouter, HTTPException, Query
from app.services.history_service import HistoryService
from app.models.movie import Movie
from app.utils.logger import Logger
from app.config import movie_service

router = APIRouter()
history_service = HistoryService()
logger = Logger()

@router.get("/")
async def get_movies(name: str = Query(None, description="Substring to search for in movie names"), user: str = Query(None, description="Name of the user looking for the movie ")):
    try:
        movies = await movie_service.get_movies(name, user)
        logger.log("Consulta de filmes realizada com sucesso.")

        for movie_data in movies:
            await history_service.save_search(movie_data, user)

        return movies
    except Exception as e:
        logger.log(f"Erro ao consultar filmes: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno ao buscar filmes")


@router.get("/{movie_id}")
async def get_movie_by_id(movie_id: str, user: str = Query(None, description="Name of the user looking for the movie ")):
    try:
        movie = await movie_service.get_movie_by_id(movie_id)
        logger.log(f"Consulta do filme com ID {movie_id} realizada com sucesso.")
        movie_data = movie['docs'][0]
        movie_instance = Movie(**movie_data)
        print(movie_instance)
        await history_service.save_search(movie_instance, user)
        return movie_instance
    except Exception as e:
        logger.log(f"Erro ao consultar filme com ID {movie_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno ao buscar filme")
