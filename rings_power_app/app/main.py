from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.movie_controller import router as movie_router
from app.controllers.history_controller import router as history_router

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your React app origin(s)
    allow_credentials=True,  # Optional, allows sending cookies with requests
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.) by default
    allow_headers=["*"],  # Allow all headers by default (adjust as needed)
)

# Registrar os routers
app.include_router(movie_router, prefix="/movies", tags=["movies"])
app.include_router(history_router, prefix="/history", tags=["history"])
