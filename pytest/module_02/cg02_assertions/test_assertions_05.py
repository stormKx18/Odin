def get_employee_data():
    employee_information = {"Name": 'John Papa',
                            "Department": 'Network',
                            "DataOfBirth": '02/24/1975',
                            "Salary": '$70K US'}
    return employee_information


def test_employee_information_01():
    employee_01 = {"Name": 'John Papa',
                   "Department": 'Network',
                   "DataOfBirth": '02/24/1975',
                   "Salary": '$70K US'}
    assert employee_01 == get_employee_data()
