from pydantic import BaseModel
from datetime import date
from pydantic import BaseModel, field_validator
from enum import Enum

class Category(Enum):
    FOOD = "Food"
    TRAVEL = "Travel"
    SHOPPING = "Shopping"
    BILLS = "Bills"

class ExpenseBase(BaseModel):
    Date: date
    Description: str
    Amount: float
    Category: str
    Notes: str | None = None

    @field_validator("Amount")
    def validate_amount(cls,value):
        if(value <=0 ):
            raise ValueError("Amount must be greater than zero")
        return value
    @field_validator("Category")
    def validate_category(cls,value):
        if(value not in Category):
            raise ValueError(f"Category should be {" ,".join(cat.value for cat in Category)}")
        return value


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseResponse(ExpenseBase):
    Id: int

class Config:
    orm_mode = True
