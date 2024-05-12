# Topic: Categorizing Tests using markers

import pytest
from module_02.cg00_apps.calculator_v2 import Calculator


@pytest.fixture
def create_test_environment():
    calci = Calculator()
    return calci


@pytest.mark.both_positive
def test_diff_100(create_test_environment):
    create_test_environment.number1 = 110
    create_test_environment.number2 = 50
    result = create_test_environment.calc_diff()
    assert result == 60


@pytest.mark.one_negative
def test_diff_200(create_test_environment):
    create_test_environment.number1 = 100
    create_test_environment.number2 = -30
    result = create_test_environment.calc_diff()
    assert result == 130


@pytest.mark.both_negative
def test_diff_300(create_test_environment):
    create_test_environment.number1 = -10
    create_test_environment.number2 = -50
    result = create_test_environment.calc_diff()
    assert result == 40
