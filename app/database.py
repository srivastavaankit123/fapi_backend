from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.secrets import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.close()