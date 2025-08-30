from fastapi import FastAPI, Body, HTTPException
from datetime import date
import Db_Helper
from typing import List
from pydantic import BaseModel


class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date:date
    end_date:date
app = FastAPI()


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = Db_Helper.fetch_db_records(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500,detail="Failed to get Results")
    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(
        expense_date: date,
        expenses: List[Expense]= Body(...)): #mention parameter as body else issue is caused
    # Db_Helper.delete_expense_for_current_date(expense_date)
    for exp in expenses:
        Db_Helper.insert_expense(expense_date, exp.amount, exp.category, exp.notes)
    return {"message": "Expenses Updated Successfully"}

@app.get("/month")
def get_month_stats():
    results = Db_Helper.fetch_expense_monthly()
    return results

@app.post("/analytics")
def get_analytics(date_range: DateRange= Body(...)): #mention parameter as body else issue is caused
    # Db_Helper.delete_expense_for_current_date(expense_date)
    results = Db_Helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if results is None:
        raise HTTPException(status_code=500,detail="Failed to get Results")
    total = sum([row['total'] for row in results])
    breakdown = {}
    for row in results:
        percentage = (row['total']/total*100 if total !=0 else 0)
        breakdown[row['category']] = {
            "total":row['total'],
            "percentage":percentage
        }
    return breakdown