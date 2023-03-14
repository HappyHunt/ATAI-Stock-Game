import json
import logging
import requests

from json import JSONDecodeError
from .error import ClientError, ServerError
from .utils import cleanNoneValue, encoded_string


class Futures(object):
    def __init__(self):
        self.base_url = "https://testnet.binancefuture.com"
        self.session = requests.Session()
        return

    # MARKET
    from .market import klines

    # METHODS
    def query(self, url_path, payload=None):
        return self.send_request("GET", url_path, payload=payload)

    def send_request(self, http_method, url_path, payload=None, special=False):
        if payload is None:
            payload = {}
        url = self.base_url + url_path
        logging.debug("url: " + url)
        params = cleanNoneValue(
            {
                "url": url,
                "params": self._prepare_params(payload, special)
            }
        )
        response = self._dispatch_request(http_method)(**params)
        logging.debug("raw response from server:" + response.text)
        self._handle_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if len(result) != 0:
            result["data"] = data
            return result

        return data

    def _prepare_params(self, params, special=False):
        return encoded_string(cleanNoneValue(params), special)

    def _dispatch_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")

    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(status_code, None, response.text, response.headers)
            raise ClientError(status_code, err["code"], err["msg"], response.headers)
        raise ServerError(status_code, response.text)