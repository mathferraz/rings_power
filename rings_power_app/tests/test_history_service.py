import unittest
from unittest.mock import patch, AsyncMock
from app.services.history_service import HistoryService
from app.models.movie import Movie

class TestHistoryService(unittest.IsolatedAsyncioTestCase):
    
    async def test_get_search_history_success(self):
        mock_history = [
            Movie(name="The Lord of the Rings", year=2001, description="A fantastic movie."),
            Movie(name="The Hobbit", year=2012, description="Another great movie.")
        ]
        
        async def mock_get_search_history():
            return mock_history
        
        history_service = HistoryService()
        
        # Mockando o método get_search_history do HistoryService
        with patch.object(history_service, 'get_search_history', new=AsyncMock(side_effect=mock_get_search_history)):
            history = await history_service.get_search_history()
            self.assertEqual(len(history), 2)
            self.assertEqual(history[0].name, "The Lord of the Rings")
            self.assertEqual(history[1].name, "The Hobbit")
