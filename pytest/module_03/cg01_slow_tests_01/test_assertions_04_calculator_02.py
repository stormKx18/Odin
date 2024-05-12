# TODO: Add imports
import pytest
import time
from module_02.cg00_apps.calculator import Calculator


# def test_division():
#     calci = Calculator(10, 0)
#     calci.calc_division()

# TODO: Add
def test_division_with_pytes_raises_1():
    time.sleep(5)
    calci = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError):
        calci.calc_division()


def test_division_with_pytes_raises_2():
    time.sleep(10)
    calci = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError) as exp_info:
        calci.calc_division()
    print()
    print(exp_info)
    print()
    print("Here is the string: " + str(exp_info.value))
    assert "division by zero" in str(exp_info.value)
