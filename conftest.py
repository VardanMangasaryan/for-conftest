import pytest
from selenium.common import NoSuchElementException


@pytest.fixture(autouse=True, scope='session')
def pp_setup():
    print('I am PythonProject3')
    yield
    print('I am PythonProject3 yield')


def pytest_runtest_setup():
    print("I'm 'pytest_runtest_setup'")


def pytest_runtest_teardown():
    print("I'm pytest_runtest_teardown")


def pytest_sessionstart():
    print("Test 'pytest_sessionstart'")


def pytest_sessionfinish():
    print("Test 'pytest_sessionfinish'")

