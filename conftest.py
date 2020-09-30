from alaska_framework.performance_alaska import PerformanceAlaska
from alaska_framework.alaska import Alaska
import pytest


@pytest.fixture(scope="function")
def alaska():
    alaska = Alaska()
    yield alaska
    alaska.delete_all_bears()


@pytest.fixture(scope="function")
def performance_alaska():
    performance_alaska = PerformanceAlaska()
    yield performance_alaska
    performance_alaska.delete_all_bears()
