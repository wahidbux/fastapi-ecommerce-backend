import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 5. Dependency function — FastAPI will call this for every request that needs
# DB access. It yields a session, and guarantees it's closed afterward, even
# if an error happens.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()