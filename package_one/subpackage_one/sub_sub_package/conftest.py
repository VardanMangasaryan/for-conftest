import pytest


@pytest.fixture(autouse=True, scope='session')
def ssp_setup():
    print('I am sub sub package 1')
    yield
    print('I am sub sub package 1 yield')
