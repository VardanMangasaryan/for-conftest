import pytest


@pytest.fixture(autouse=True, scope='session')
def p1_setup():
    print('I am package 1')
    yield
    print('I am package 1 yield')

