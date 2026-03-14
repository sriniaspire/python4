from sqlalchemy import Column, Integer, String, Numeric, Date, Text
from database import Base

class ExpenseRecord(Base):

    __tablename__ = "ExpenseRecords"

    Id = Column(Integer, primary_key=True, index=True)
    Date = Column(Date, nullable=False)
    Description = Column(String(200), nullable=False)
    Amount = Column(Numeric(18,2), nullable=False)
    Category = Column(String(100), nullable=False)
    Notes = Column(Text)