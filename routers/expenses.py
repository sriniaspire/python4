from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/expenses")
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)


@router.get("/expenses")
def read_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)


@router.get("/expenses/{expense_id}")
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.get_expense(db, expense_id)


@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.delete_expense(db, expense_id)