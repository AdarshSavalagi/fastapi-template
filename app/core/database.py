from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Create the engine (the connection to Postgres)
engine = create_engine(settings.DATABASE_URL)

# 2. Create a SessionLocal class (used to create a database session for each request)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create the Base class (all your database models will inherit from this)
Base = declarative_base()

# 4. Dependency (used in routes to get a DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()