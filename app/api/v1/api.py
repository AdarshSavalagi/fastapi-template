from fastapi import APIRouter
from app.modules.users import routes as user_routes

api_router = APIRouter()

# Include the 'users' module
api_router.include_router(user_routes.router, prefix="/users", tags=["users"])