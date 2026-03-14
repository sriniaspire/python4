from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "postgresql://postgres:Aspire%40123@localhost:5432/expense_tracker"
DATABASE_URL = "sqlite:///expense.db"

#engine = create_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL,echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()