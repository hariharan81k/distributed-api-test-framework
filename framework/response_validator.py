class ResponseValidator:

    @staticmethod
    def assert_status(response, expected_status):

        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, "
            f"but got {response.status_code}"
        )

    @staticmethod
    def assert_json_field(response, field, expected_value):

        data = response.json()

        assert field in data, (
            f"Expected field '{field}' "
            f"was not found in response"
        )

        assert data[field] == expected_value, (
            f"Expected '{field}' to be '{expected_value}', "
            f"but got '{data[field]}'"
        )

    @staticmethod
    def assert_json_fields_exist(response, fields):

        data = response.json()

        for field in fields:

            assert field in data, (
                f"Expected field '{field}' "
                f"was not found in response"
            )
