from unittest import mock

import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# Two new test cases
def test_CanCalculateInputAnswer(invoice):
    # asserting that it can detect correct user input when user enters 'y'
    with mock.patch('builtins.input', return_value = 'y'):
        assert invoice.inputAnswer('builtins.input') == 'y'

    # asserting that it can detect correct user input when user enters 'n'
    with mock.patch('builtins.input', return_value = 'n'):
        assert invoice.inputAnswer('builtins.input') == 'n'

    # asserting that it can detect incorrect user input
    with mock.patch('builtins.input', return_value = 'a'):
        assert invoice.inputAnswer('builtins.input') == False


def test_CanCalculateInputNumber(invoice):
    # asserting that it can detect correct user input when user enters a float value
    with mock.patch('builtins.input', return_value = 20.77):
        assert invoice.inputNumber('builtins.input') == 20.77

    # asserting that it can detect correct user input when user enters an int value
    with mock.patch('builtins.input', return_value = 20):
        assert invoice.inputNumber('builtins.input') == 20.0

    # asserting that it can detect incorrect user input
    with mock.patch('builtins.input', return_value = 'a'):
        assert invoice.inputNumber('builtins.input') == False
