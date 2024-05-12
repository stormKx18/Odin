# TODO: Add imports
import pytest
from module_02.cg00_apps.calculator import Calculator


def test_division():
    calci = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError):
        result = calci.calc_division()


def test_division_2():
    calci = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError) as exp_info:
        result = calci.calc_division()
    print()
    print(exp_info)
    print()
    print(exp_info.value)
    assert "zero" in str(exp_info.value)
