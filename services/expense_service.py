from repositories.expense_repository import ExpenseRepository

class ExpenseService:

    def __init__(self):
        self.repo = ExpenseRepository()

    def get_expenses(self, db):
        return self.repo.get_expenses(db)
    
    def get_expenses_by_id(self,id,db):
        return self.repo.get_expense(db,id)

    def add_expense(self, db, expense):
        return self.repo.create_expense(db, expense)
        
    def delete_expense(self,id,db):
        return self.repo.delete_expense(db,id)  
    
    