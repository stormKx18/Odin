from module_02.cg00_apps.employee import Employee


def test_base_annual_salary():
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 100000.00
    base_salary = employee.base_annual_salary
    assert base_salary == 100000.00


# TODO: Employee name test
def test_employee_name():
    employee = Employee("Peter", "Parker")
    employee.base_annual_salary = 100000.00
    first_name = employee.first_name
    last_name = employee.last_name
    assert first_name == "Peter"
    assert last_name == "Parker"
