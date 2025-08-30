import mysql.connector
from contextlib import contextmanager
import logging_setup

logger = logging_setup.set_up()

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_db_records(expense_date):
    logger.info(f"Fetching Records for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date,amount,category,notes):
    logger.info(f"Inserting Records for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes)
                       )
def delete_expense_for_current_date(expense_date):
    logger.info(f"Deleting Records for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"Fetching Records from date: {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category, SUM(amount) as total
                          FROM expenses WHERE expense_date
                          BETWEEN %s and %s
                          GROUP BY category''',
                       (start_date,end_date)
                       )
        data = cursor.fetchall()
        return data

def fetch_expense_monthly():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT month_name ,sum(amount) as Total FROM expenses GROUP BY month_name")
        results = cursor.fetchall()
        return results

if __name__ == "__main__":
    expenses = fetch_expense_monthly()
    print(expenses,"\n")