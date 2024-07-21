from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from service.adapters.abstract_client import AbstractTestClient
from service.adapters.client import SetupClientExample
from service.model.example_model import UserDetail
from service.logger_helper import logger


router = APIRouter()

def setup_abstract_test_client() -> AbstractTestClient:
    test_client: SetupClientExample = SetupClientExample("Vivek", "Arya")
    return test_client


@router.get("/api/v1/test", response_model=UserDetail)
async def test_endpoint() -> UserDetail:
    try:
        logger.info("test endpoint executed successfully")
        return setup_abstract_test_client().greet_user()
    except Exception as e:
        logger.error(f"Error in test_endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")