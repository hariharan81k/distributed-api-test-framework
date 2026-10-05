import os
import pytest

from framework.api_client import APIClient
from framework.config import BASE_URL, API_TIMEOUT


@pytest.fixture
def client():
    return APIClient(
        BASE_URL,
        API_TIMEOUT
    )

@pytest.fixture
def service_url():

    return os.getenv(
        "TEST_SERVICE_URL",
        "http://localhost:8001"
    )

@pytest.fixture
def expected_version():

    return os.getenv(
        "EXPECTED_API_VERSION",
        "v1"
    )