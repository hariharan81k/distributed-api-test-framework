import pytest

from framework.response_validator import ResponseValidator

@pytest.mark.regression
def test_delete_user(client):

    response = client.delete("/users/1")

    ResponseValidator.assert_status(
        response,
        200
    )
