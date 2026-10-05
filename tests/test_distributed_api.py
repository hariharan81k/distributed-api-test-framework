import os

import pytest

from framework.api_client import APIClient
from framework.response_validator import ResponseValidator
from test_data.user_data import DISTRIBUTED_CREATE_USER_DATA


@pytest.mark.distributed
@pytest.mark.parametrize(
    "endpoint, expected_status",
    [
        ("/users/1", 200),
        ("/users/999", 404),
    ]
)
def test_get_user_endpoints(
    service_url,
    endpoint,
    expected_status
):

    client = APIClient(
        service_url,
        5
    )

    response = client.get(endpoint)

    ResponseValidator.assert_status(
        response,
        expected_status
    )


@pytest.mark.distributed
def test_api_version(service_url, expected_version):

    client = APIClient(
        service_url,
        5
    )

    response = client.get("/users/1")

    ResponseValidator.assert_status(
        response,
        200
    )

    ResponseValidator.assert_json_field(
        response,
        "version",
        expected_version
    )

@pytest.mark.distributed
def test_health_check(service_url):

    client = APIClient(
        service_url,
        5
    )

    response = client.get("/health")

    ResponseValidator.assert_status(
        response,
        200
    )

    ResponseValidator.assert_json_field(
        response,
        "status",
        "healthy"
    )


@pytest.mark.distributed
@pytest.mark.parametrize(
    "user_data",
    DISTRIBUTED_CREATE_USER_DATA
)
def test_create_user(service_url, user_data):

    client = APIClient(
        service_url,
        5
    )

    response = client.post(
        "/users",
        user_data
    )

    ResponseValidator.assert_status(
        response,
        201
    )

    ResponseValidator.assert_json_field(
        response,
        "name",
        user_data["name"]
    )

    ResponseValidator.assert_json_field(
        response,
        "username",
        user_data["username"]
    )

    ResponseValidator.assert_json_field(
        response,
        "email",
        user_data["email"]
    )

    ResponseValidator.assert_json_fields_exist(
        response,
        [
            "id",
            "version"
        ]
    )

@pytest.mark.distributed
def test_update_user(service_url):

    client = APIClient(
        service_url,
        5
    )

    user_data = {
        "name": "Hariharan Updated",
        "username": "hari_updated",
        "email": "updated@example.com"
    }

    response = client.put(
        "/users/1",
        user_data
    )

    ResponseValidator.assert_status(
        response,
        200
    )

    ResponseValidator.assert_json_field(
        response,
        "name",
        user_data["name"]
    )

    ResponseValidator.assert_json_field(
        response,
        "username",
        user_data["username"]
    )

    ResponseValidator.assert_json_field(
        response,
        "email",
        user_data["email"]
    )

    ResponseValidator.assert_json_fields_exist(
        response,
        [
            "id",
            "version"
        ]
    )

@pytest.mark.distributed
def test_patch_user(service_url):

    client = APIClient(
        service_url,
        5
    )

    patch_data = {
        "email": "patched@example.com"
    }

    response = client.patch(
        "/users/1",
        patch_data
    )

    ResponseValidator.assert_status(
        response,
        200
    )

    ResponseValidator.assert_json_field(
        response,
        "email",
        patch_data["email"]
    )

    ResponseValidator.assert_json_fields_exist(
        response,
        [
            "id",
            "version"
        ]
    )

@pytest.mark.distributed
def test_delete_user(service_url):

    client = APIClient(
        service_url,
        5
    )

    response = client.delete(
        "/users/1"
    )

    ResponseValidator.assert_status(
        response,
        200
    )