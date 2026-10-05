import pytest

from framework.response_validator import ResponseValidator

from test_data.user_data import UPDATE_USER_DATA

@pytest.mark.regression
@pytest.mark.parametrize(
    "user_data",
    UPDATE_USER_DATA
)
def test_update_user(client, user_data):

    response = client.put(
        f"/users/{user_data['user_id']}",
        user_data["data"]
    )

    ResponseValidator.assert_status(
        response,
        200
        )

    data = response.json()

    assert data["name"] == user_data["data"]["name"]
    assert data["username"] == user_data["data"]["username"]
    assert data["email"] == user_data["data"]["email"]
