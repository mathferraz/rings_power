# Lord of the Rings Full Stack Project

## Overview

This project integrates with the [The One API](https://the-one-api.dev/) to retrieve and log movie data. The backend is built with FastAPI and uses Redis for caching and logging. The frontend is a React application that interacts with the backend through API calls.

## Installation

### Prerequisites

- Docker
- Docker Compose
- Node.js (for frontend development)

### Installing Dependencies

1. **Backend Dependencies:**

   ```bash
   # Inside the repository directory
   cd app
   pip install -r requirements.txt

2. **Frontend Dependencies:**
    # Inside the repository directory
    cd frontend
    npm install

Note: The node_modules folder for the frontend is not included in the repository. Please navigate to the /frontend directory and run npm install to install all necessary dependencies.

### Docker and Docker Compose Installation

    Follow the official Docker installation guide to install Docker ("https://docs.docker.com/engine/install/").
    Docker Compose is typically included in Docker desktop versions for Mac and Windows. For Linux, follow the installation guide ("https://docs.docker.com/compose/install/").

### Steps to Build and Run the Project

1. **Clone the repository:**
    git clone [<repository-url>](https://github.com/mathferraz/rings_power.git)
    cd <rings_power>

2. **Build and start the project:**
    docker-compose up --build
    This command will build and start the backend, frontend, and Redis services.

3. **Access the application:**
    Backend API: http://localhost:8000
    Frontend: http://localhost:3000

## Backend (FastAPI)

### Clean Architecture

The backend is structured following Clean Architecture principles to maintain separation of concerns and improve maintainability.
Directory Structure
app/
│
├── config.py        # Configuration settings
├── main.py          # FastAPI application instantiation
├── controllers/     # Controllers handling HTTP requests
│   ├── history_controller.py
│   └── movie_controller.py
│
├── models/          # Data models
│   └── movie.py
│
├── repositories/    # Data access layer
│   └── history_repository.py
│
├── services/        # Business logic layer
│   ├── history_service.py
│   └── movie_service.py
│
└── utils/           # Utility modules
    ├── db.py        # Database connection management
    └── logger.py    # Logging utilities

### Components

    Controllers: Handle HTTP requests and route them to appropriate services.
    Models: Define data structures used in the application.
    Repositories: Encapsulate data access logic, interacting with databases or external APIs.
    Services: Implement business logic, orchestrate operations across multiple repositories.
    Utils: Provide utility functions for database management (db.py) and logging (logger.py).

### Endpoints

    GET /movies/
        Retrieves movies from The One API based on a partial name and user query...

    GET /movies/{movie_id}
        Retrieves details of a specific movie by ID (not available in frontend)...

    GET /history/
        Retrieves all stored logs from Redis and returns them to the frontend...

## Redis

Redis is used in this project for caching and logging purposes. It stores user queries and movie data fetched from The One API.
How Redis Works

    Caching: Results from API queries are cached in Redis to improve response times for subsequent requests with the same parameters.
    Logging: When a user queries for movies, the backend logs the user's name, movie data, and timestamp in Redis. The /history/ endpoint retrieves these logs for display in the frontend.

## Testing
Running Tests

    Backend:
    cd app
    pytest
    Tests are located in tests/test_history_service.py and tests/test_movie_service.py.

    Frontend:
    Currently, no tests are implemented for the frontend.

## Postman Collection

A Postman collection (Lord of the Rings.postman_collection.json) is included...
Importing the Postman Collection

    Open Postman.
    Click on the Import button located in the upper-left corner.
    Drag and drop the Lord of the Rings.postman_collection.json file into the dialog box, or click on Choose Files to locate and select the file manually.
    Click Import to upload the collection into your Postman workspace.

### Swagger UI

FastAPI generates an interactive API documentation (Swagger UI) at http://localhost:8000/docs.

### Notes

    Ensure Docker and Docker Compose are properly installed and running before executing the project...
    Modify configurations and environment variables (docker-compose.yml, .env)...
