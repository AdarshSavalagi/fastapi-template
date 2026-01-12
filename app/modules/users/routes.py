import logging
from fastapi import APIRouter
from app.constants.messages import ApiMessages
from app.utils.response import ApiResponse

# 1. Initialize Logger for this module
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
def get_users():
    # Log the action (Trace ID is injected automatically)
    logger.info("Fetching all users list")
    
    # Fetch data (mocked)
    users_list = [{"id": 1, "name": "Adarsh"}]
    
    logger.debug(f"Found {len(users_list)} users")
    
    # Return formatted response
    return ApiResponse.success(
        data=users_list, 
        message=ApiMessages.SUCCESS
    )

@router.get("/fail-test")
def fail_test():
    # Log the error event
    logger.warning("Fail test endpoint called - simulating error")
    
    return ApiResponse.error(
        message="Invalid parameters",
        status_code=422
    )