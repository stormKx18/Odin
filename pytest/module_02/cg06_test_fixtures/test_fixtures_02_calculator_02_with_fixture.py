# Topic: Test Fixtures

import pytest
from module_02.cg00_apps.calculator_v2 import Calculator


@pytest.fixture()
def create_test_env():
    calci = Calculator()
    return calci


def test_addition(create_test_env):
    create_test_env.number1 = 10
    create_test_env.number2 = 50
    result = create_test_env.calc_add()
    assert result == 60


def test_difference(create_test_env):
    create_test_env.number1 = 10
    create_test_env.number2 = 50
    result = create_test_env.calc_diff()
    assert result == -40


def test_multiply(create_test_env):
    create_test_env.number1 = 10
    create_test_env.number2 = 50
    result = create_test_env.calc_prod()
    assert result == 500
