import logging
import requests


logger = logging.getLogger(__name__)


class APIClient:

    def __init__(self, base_url, timeout):
        self.base_url = base_url
        self.timeout = timeout

    def request(self, method, endpoint, data=None):

        if endpoint.startswith("http"):
            url = endpoint
        else:
            url = self.base_url + endpoint

        logger.info("%s %s", method, url)

        if data is not None:
            logger.info("Request body: %s", data)

        try:

            response = requests.request(
                method,
                url,
                json=data,
                timeout=self.timeout
            )

        except requests.exceptions.Timeout:

            logger.error(
                "Request timed out: %s %s",
                method,
                url
            )

            raise

        except requests.exceptions.ConnectionError:

            logger.error(
                "Connection failed: %s %s",
                method,
                url
            )

            raise

            logger.info(
                "%s %s -> %s",
                method,
                url,
                response.status_code
            )

        return response

    def get(self, endpoint):
        return self.request("GET", endpoint)

    def post(self, endpoint, data):
        return self.request("POST", endpoint, data)

    def put(self, endpoint, data):
        return self.request("PUT", endpoint, data)

    def patch(self, endpoint, data):
        return self.request("PATCH", endpoint, data)

    def delete(self, endpoint):
        return self.request("DELETE", endpoint)
