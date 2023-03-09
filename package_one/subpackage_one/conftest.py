import pytest


@pytest.fixture(autouse=True, scope='session')
def ps1_setup():
    print('I am sub package 1')
    yield
    print('I am sub package 1 yield')