import pytest

from framework.response_validator import ResponseValidator

@pytest.mark.smoke
@pytest.mark.parametrize(
    "user_id, expected_status, expected_name",
    [
        (1, 200, "Leanne Graham"),
        (2, 200, "Ervin Howell"),
        (3, 200, "Clementine Bauch"),
        (9999, 404, None),
    ]
)
def test_get_user(client, user_id, expected_status, expected_name):

    response = client.get(f"/users/{user_id}")

    ResponseValidator.assert_status(
        response,
        expected_status
    )

    if expected_status == 200:

        ResponseValidator.assert_json_field(
            response,
            "id",
            user_id
        )

        ResponseValidator.assert_json_field(
            response,
            "name",
            expected_name
        )

        ResponseValidator.assert_json_fields_exist(
            response,
            ["id", "name", "username", "email"]
        )
