# Topic: Categorizing Tests using markers

import pytest
from module_02.cg00_apps.calculator_v2 import Calculator


@pytest.fixture
def create_test_environment():
    calci = Calculator()
    return calci


@pytest.mark.both_positive
def test_addition_100(create_test_environment):
    create_test_environment.number1 = 10
    create_test_environment.number2 = 50
    result = create_test_environment.calc_add()
    assert result == 60


@pytest.mark.one_negative
def test_addition_200(create_test_environment):
    create_test_environment.number1 = -50
    create_test_environment.number2 = 30
    result = create_test_environment.calc_add()
    assert result == -20


@pytest.mark.both_negative
def test_addition_300(create_test_environment):
    create_test_environment.number1 = -10
    create_test_environment.number2 = -50
    result = create_test_environment.calc_add()
    assert result == -60
