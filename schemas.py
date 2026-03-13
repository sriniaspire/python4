from pydantic import BaseModel
from datetime import date


class ExpenseBase(BaseModel):
    Date: date
    Description: str
    Amount: float
    Category: str
    Notes: str | None = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseResponse(ExpenseBase):
    Id: int

class Config:
    orm_mode = True
