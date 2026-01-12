from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Proctored Exam API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Comprehensive API for Student Exam & Proctoring System"
    
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/exam_db"
    
    # Security
    SECRET_KEY: str = "CHANGE_THIS_IN_PROD"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Docs Config (Can be disabled in Prod by setting to None)
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"

    # Distributed Tracing Config
    ENABLE_TELEMETRY: bool = False
    OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://localhost:4317"

    # Logging
    LOG_LEVEL: str = "TRACE" 
    LOG_FORMAT: str = "console"

    class Config:
        env_file = ".env"

settings = Settings()