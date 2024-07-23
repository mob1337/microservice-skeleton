"""
Module defining API endpoints for version 1.
"""

from fastapi import APIRouter, HTTPException
from service.adapters.abstract_client import AbstractClient
from service.adapters.client import SetupClientExample
from service.model.example_model import UserDetail
from service.logger_helper import logger

router = APIRouter()


def setup_abstract_test_client() -> AbstractClient:
    """
    Sets up an instance of SetupClientExample as AbstractClient.
    """
    test_client: SetupClientExample = SetupClientExample("Vivek", "Arya")
    return test_client


@router.get("/api/v1/test", response_model=UserDetail)
async def test_endpoint() -> UserDetail:
    """
    Endpoint for testing purposes.
    """
    try:
        logger.info("Test endpoint executed successfully")
        return setup_abstract_test_client().greet_user()
    except Exception as error_message:
        logger.error(error_message)
        raise HTTPException(
            status_code=500, detail="Internal server error"
        ) from error_message
