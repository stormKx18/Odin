# Topic: Categorizing Tests using markers

import pytest
from module_02.cg00_apps.calculator_v2 import Calculator


@pytest.fixture
def create_test_environment():
    calci = Calculator()
    return calci


@pytest.mark.both_positive
def test_multiply_100(create_test_environment):
    create_test_environment.number1 = 5
    create_test_environment.number2 = 9
    result = create_test_environment.calc_prod()
    assert result == 45


@pytest.mark.one_negative
def test_multiply_200(create_test_environment):
    create_test_environment.number1 = 20
    create_test_environment.number2 = -5
    result = create_test_environment.calc_prod()
    assert result == -100


@pytest.mark.both_negative
def test_multiply_300(create_test_environment):
    create_test_environment.number1 = -10
    create_test_environment.number2 = -50
    result = create_test_environment.calc_prod()
    assert result == 500
