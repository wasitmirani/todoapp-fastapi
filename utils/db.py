from sqlalchemy import create_engine
from utils.settings import settings
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a database engine

Base = declarative_base()
engine = create_engine(settings.DB_URL)

# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()
    try:
        # Yield the database session what is yield in python
        # Yield is used to return a generator
        # Generator is a function that returns a sequence of values

        yield db
    finally:
        db.close()
