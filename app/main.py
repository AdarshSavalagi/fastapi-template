from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router
from app.core.logging import setup_logging
from app.core.middleware import setup_middlewares
from app.core.docs import setup_openapi
from app.core.telemetry import setup_telemetry 
from app.core.database import engine
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor


setup_logging()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    openapi_url=settings.OPENAPI_URL
)

# 1. Setup Middlewares
setup_middlewares(app)

# 2. Setup Docs
setup_openapi(app)

# 3. Setup Telemetry (Must pass 'app' to instrument it)
setup_telemetry(app)

# 4. Instrument Database (Connects OTel to your specific DB engine)
if settings.ENABLE_TELEMETRY:
    SQLAlchemyInstrumentor().instrument(engine=engine)

# 5. Include Routers
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "version": settings.PROJECT_VERSION}