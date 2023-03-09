import pytest


@pytest.fixture(autouse=True)
def p2_setup():
    print('I am package second')
