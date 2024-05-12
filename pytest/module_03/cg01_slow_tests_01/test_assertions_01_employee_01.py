import time
from module_02.cg00_apps.employee import Employee


def test_base_annual_salary():
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 100000.00
    base_salary = employee.base_annual_salary
    # assert is the built-in function
    # Result == Expected Value
    assert base_salary == 100000.00


# TODO: add time.sleep(30)
def test_employee_name():
    time.sleep(30)
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 100000.00
    first_name = employee.first_name
    last_name = employee.last_name
    assert first_name == "Peter"
    assert last_name == "Parker"
