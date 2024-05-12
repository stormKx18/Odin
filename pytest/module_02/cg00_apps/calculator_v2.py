class Calculator:
    """
    Basic Calculator class.
    Constructor requires two numbers.
    """

    __num1 = 0
    __num2 = 0

    @property
    def number1(self):
        return self.__num1

    @number1.setter
    def number1(self, num1):
        self.__num1 = num1

    @property
    def number2(self):
        return self.__num1

    @number2.setter
    def number2(self, num2):
        self.__num2 = num2

    def calc_add(self):
        return self.__num1 + self.__num2

    def calc_diff(self):
        return self.__num1 - self.__num2

    def calc_prod(self):
        return self.__num1 * self.__num2

    def calc_division(self):
        return self.__num1 / self.__num2


if __name__ == '__main__':
    print("Import and use it!")
