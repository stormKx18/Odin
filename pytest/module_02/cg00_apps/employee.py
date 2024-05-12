class Employee:
    __bonus_percentage = 0.20
    __additional_bonus_level_1 = 0.05
    __additional_bonus_level_2 = 0.10
    """ 50% of the employee contribution """
    __employer_contribution_to_retirement_account = 0.5

    # Class Constructor (Method with a special name)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # Private Attributes
        self.__base_annual_salary = 0
        self.__employee_retirement_contribution = 0
        self.__years_of_employment = 0
        self.__skills = {}

    @property
    def base_annual_salary(self):
        return self.__base_annual_salary

    @base_annual_salary.setter
    def base_annual_salary(self, base_annual_salary):
        if 45000.00 <= base_annual_salary <= 120000.00:
            self.__base_annual_salary = base_annual_salary
        else:
            self.__base_annual_salary = 0
            print("Annual base salary can't be less than 45,000.00 and can't be greater than 120,000.00!")

    @property
    def years_of_employment(self):
        return self.__years_of_employment

    @years_of_employment.setter
    def years_of_employment(self, years_of_employment):
        self.__years_of_employment = years_of_employment

    @property
    def employee_retirement_contribution(self):
        return self.__employee_retirement_contribution

    @employee_retirement_contribution.setter
    def employee_retirement_contribution(self, employee_retirement_contribution):
        if 0 <= employee_retirement_contribution <= 0.10:
            self.__employee_retirement_contribution = employee_retirement_contribution
        elif employee_retirement_contribution < 0:
            self.__employee_retirement_contribution = 0
        else:
            self.__employee_retirement_contribution = 0.10

    # bonus_percentage has no setter.
    # Effectively it becomes a read-only property
    @property
    def bonus_percentage(self):
        return self.__bonus_percentage

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def add_to_skills(self, skill, years_of_experience):
        self.__skills[skill] = years_of_experience

    # Methods
    def get_monthly_gross(self):
        return self.__base_annual_salary / 12

    def get_standard_annual_bonus_amount(self):
        if 0 <= self.__years_of_employment <= 5:
            return self.__base_annual_salary * self.__bonus_percentage
        elif 6 <= self.__years_of_employment <= 10:
            return self.__base_annual_salary * (self.__bonus_percentage + self.__additional_bonus_level_1)
        elif self.__years_of_employment > 10:
            return self.__base_annual_salary * (self.__bonus_percentage + self.__additional_bonus_level_2)

    def get_employee_contribution_to_retirement_account(self):
        return self.base_annual_salary * self.employee_retirement_contribution

    def get_employer_contribution_to_retirement_account(self):
        return self.get_employee_contribution_to_retirement_account() \
               * self.__employer_contribution_to_retirement_account

    def get_additional_bonus_percentage(self):
        if 0 <= self.__years_of_employment <= 5:
            return self.__bonus_percentage
        elif 6 <= self.__years_of_employment <= 10:
            return self.__additional_bonus_level_1
        elif self.__years_of_employment > 10:
            return self.__additional_bonus_level_2

    def get_total_annual_package(self):
        annual_salary = self.base_annual_salary
        annual_bonus = self.get_standard_annual_bonus_amount()
        employer_contribution_to_retirement_amount = self.get_employer_contribution_to_retirement_account()
        print(annual_salary)
        print(annual_bonus)
        print(employer_contribution_to_retirement_amount)
        total_amount = annual_salary + annual_bonus + employer_contribution_to_retirement_amount
        return total_amount


def main():
    print("Hello! Please import me!")


if __name__ == '__main__':
    main()
