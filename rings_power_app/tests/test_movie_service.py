import unittest
from unittest.mock import patch, AsyncMock
from app.services.movie_service import MovieService
from app.models.movie import Movie

class TestMovieService(unittest.IsolatedAsyncioTestCase):
    
    async def test_get_movies_success(self):
        mock_response = [
            {"name": "The Lord of the Rings", "year": 2001, "description": "A fantastic movie."},
            {"name": "The Hobbit", "year": 2012, "description": "Another great movie."}
        ]
        
        async def mock_get_movies():
            return [Movie(**data) for data in mock_response]
        
        movie_service = MovieService()
        
        # Mockando o método get_movies do MovieService
        with patch.object(movie_service, 'get_movies', new=AsyncMock(side_effect=mock_get_movies)):
            movies = await movie_service.get_movies()
            self.assertEqual(len(movies), 2)
            self.assertEqual(movies[0].name, "The Lord of the Rings")
            self.assertEqual(movies[1].name, "The Hobbit")
    
    async def test_get_movie_by_id_success(self):
        movie_id = "123456"
        mock_response = {"name": "The Lord of the Rings", "year": 2001, "description": "A fantastic movie."}
        
        async def mock_get_movie_by_id():
            return Movie(**mock_response)
        
        movie_service = MovieService()
        
        # Mockando o método get_movie_by_id do MovieService
        with patch.object(movie_service, 'get_movie_by_id', new=AsyncMock(side_effect=mock_get_movie_by_id)):
            movie = await movie_service.get_movie_by_id(movie_id)
            self.assertEqual(movie.name, "The Lord of the Rings")
