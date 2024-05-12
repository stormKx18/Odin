# TODO: Add imports
import pytest
from module_02.cg00_apps.calculator import Calculator


# TODO: Add a test for addition method
def test_addition():
    calci = Calculator(10, 20)
    result = calci.calc_add()
    assert result == 30
