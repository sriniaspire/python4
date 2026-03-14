from sqlalchemy.orm import Session
import models.models as models, schemas.schemas as schemas

class ExpenseRepository:

    def create_expense(self,db: Session, expense: schemas.ExpenseCreate):
        db_expense = models.ExpenseRecord(**expense.dict())
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return db_expense


    def get_expenses(self,db: Session):
        return db.query(models.ExpenseRecord).all()


    def get_expense(self,db: Session, expense_id: int):
        return db.query(models.ExpenseRecord).filter(models.ExpenseRecord.Id == expense_id).first()


    def delete_expense(self,db: Session, expense_id: int):
        expense = db.query(models.ExpenseRecord).filter(models.ExpenseRecord.Id == expense_id).first()
        if expense:
            db.delete(expense)
            db.commit()
        return expense