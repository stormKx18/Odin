# TODO: Add imports
import pytest
import time
from module_02.cg00_apps.calculator import Calculator


# TODO: Add time.sleep(20)
def test_addition():
    time.sleep(20)
    calci = Calculator(10, 20)
    result = calci.calc_add()
    assert result == 30
