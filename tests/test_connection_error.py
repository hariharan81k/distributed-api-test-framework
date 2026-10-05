import pytest
import requests

@pytest.mark.regression
def test_connection_error(client):

    with pytest.raises(requests.exceptions.ConnectionError):
        client.get("http://localhost:9999")
