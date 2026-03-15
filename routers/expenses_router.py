from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.db import get_db
import repositories.expense_repository as expense_repository, schemas.schemas as schemas
from services.expense_service import ExpenseService

router = APIRouter(prefix="/expenses")

service = ExpenseService()

@router.post("/")
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return service.add_expense(db, expense)


@router.get("/")
def read_expenses(db: Session = Depends(get_db)):
    return service.get_expenses(db)


@router.get("/{expense_id}")
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    return service.get_expenses_by_id(db, expense_id)


@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return service.delete_expense(db, expense_id)