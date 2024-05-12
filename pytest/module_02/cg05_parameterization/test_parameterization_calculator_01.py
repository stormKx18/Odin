import pytest
from module_02.cg00_apps.calculator import Calculator


@pytest.mark.parametrize("num1, num2, exp_result", [(50, 20, 30), (30, 20, 10), (-50, 20, -70)])
def test_difference(num1, num2, exp_result):
    calci = Calculator(num1, num2)
    result = calci.calc_diff()
    assert result == exp_result
