from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from app.core.config import settings

def setup_openapi(app: FastAPI):
    """
    Customizes the OpenAPI schema to include JWT Security
    global definitions for Swagger UI.
    """
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        
        openapi_schema = get_openapi(
            title=settings.PROJECT_NAME,
            version=settings.PROJECT_VERSION,
            description=settings.PROJECT_DESCRIPTION,
            routes=app.routes,
        )
        
        # 1. Define the Security Scheme (HTTP Bearer)
        if "components" not in openapi_schema:
            openapi_schema["components"] = {}
            
        openapi_schema["components"]["securitySchemes"] = {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
        
        # 2. Apply this security globally to all endpoints
        # (Since your Middleware protects almost everything)
        openapi_schema["security"] = [{"BearerAuth": []}]
        
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    # Assign the custom function to the app
    app.openapi = custom_openapi