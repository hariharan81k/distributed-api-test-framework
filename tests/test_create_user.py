import pytest

from framework.response_validator import ResponseValidator
from test_data.user_data import CREATE_USER_DATA

@pytest.mark.regression
@pytest.mark.parametrize(
    "post_data",
    CREATE_USER_DATA
)
def test_create_user(client, post_data):

    response = client.post("/users", post_data)

    ResponseValidator.assert_status(
        response,
        201
    )

    data = response.json()

    assert data["name"] == post_data["name"]
    assert data["username"] == post_data["username"]
    assert data["email"] == post_data["email"]
    assert "id" in data
