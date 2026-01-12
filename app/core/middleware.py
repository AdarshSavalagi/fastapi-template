from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Import your custom middlewares
from app.middlewares.auth import JWTAuthMiddleware
from app.middlewares.logging import LoggingMiddleware


def setup_middlewares(app: FastAPI):
    """
    Register all middlewares here.
    Note: Middleware is applied in reverse order (bottom to top).
    """
    

    app.add_middleware(JWTAuthMiddleware)

    app.add_middleware(LoggingMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, change this to ["http://localhost:3000"]
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )