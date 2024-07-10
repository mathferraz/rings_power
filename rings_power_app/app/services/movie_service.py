import httpx
from app.models.movie import Movie

api_base_url = "https://the-one-api.dev/v2"

class MovieService:
    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    async def get_movies(self, name: str = None, user: str = None):
        headers = {}
        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{api_base_url}/movie", headers=headers)
            if response.status_code == 200:
                movies_data = response.json()["docs"]
                movies = [Movie(**movie_data) for movie_data in movies_data]
                
                if name:
                    name = name.lower()
                    movies = [movie for movie in movies if name in movie.name.lower()]
                
                return movies
            else:
                raise Exception("Erro ao buscar filmes na API externa")

    async def get_movie_by_id(self, movie_id: str):
        headers = {}
        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{api_base_url}/movie/{movie_id}", headers=headers)
            if response.status_code == 200:
                movie_data = response.json()
                return movie_data
            else:
                raise Exception("Erro ao buscar filme por ID na API externa")
