import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Setting up in-memory database for testing
DATABASE_URL = "sqlite:///:memory:"

# Creating the SQLAlchemy Engine and Session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basis for the data model
Base = declarative_base()


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    # Opens a new database session for testing
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)