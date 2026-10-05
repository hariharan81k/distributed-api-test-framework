import pytest
import requests

@pytest.mark.regression
def test_api_timeout(client):

    with pytest.raises(requests.exceptions.ReadTimeout):
        client.get("https://httpbin.org/delay/10")
