from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date

if __name__ == '__main__':
    print(date.today())
    print(calculate_salary())
    print(get_employees())
