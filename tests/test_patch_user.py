import pytest

from framework.response_validator import ResponseValidator

from test_data.user_data import PATCH_USER_DATA

@pytest.mark.regression
@pytest.mark.parametrize(
    "user_data",
    PATCH_USER_DATA
)
def test_patch_user(client, user_data):

    response = client.patch(
        f"/users/{user_data['user_id']}",
        user_data["data"]
    )

    ResponseValidator.assert_status(
        response,
        200
        )

    data = response.json()

    assert data["email"] == user_data["data"]["email"]
