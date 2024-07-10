from fastapi import APIRouter, HTTPException
from app.services.history_service import HistoryService
from app.models.movie import Movie
from app.utils.logger import Logger

router = APIRouter()
history_service = HistoryService()
logger = Logger()

@router.get("/")
async def get_search_history():
    try:
        history = await history_service.get_search_history()
        logger.log("Consulta de histórico de pesquisas realizada com sucesso.")
        return history
    except Exception as e:
        logger.log(f"Erro ao consultar histórico de pesquisas: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno ao buscar histórico")
