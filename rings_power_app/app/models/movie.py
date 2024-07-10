from pydantic import BaseModel

class Movie(BaseModel):
    _id: str
    name: str
    runtimeInMinutes: int
    budgetInMillions: int
    boxOfficeRevenueInMillions: float
    academyAwardNominations: int
    academyAwardWins: int
    rottenTomatoesScore: float

