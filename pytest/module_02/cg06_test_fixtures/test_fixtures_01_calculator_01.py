# Topic: Test Fixtures

import pytest
from module_02.cg00_apps.calculator_v2 import Calculator


def test_addition():
    calci = Calculator()
    calci.number1 = 10
    calci.number2 = 50
    result = calci.calc_add()
    assert result == 60


def test_difference():
    calci = Calculator()
    calci.number1 = 10
    calci.number2 = 50
    result = calci.calc_diff()
    assert result == -40


def test_multiply():
    calci = Calculator()
    calci.number1 = 10
    calci.number2 = 50
    result = calci.calc_prod()
    assert result == 500
