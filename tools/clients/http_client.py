"""Storage module for class HTTPClient"""
from typing import Optional
import requests
from requests import Response


class HTTPClient:
    """Class sending requests"""

    @staticmethod
    def get(url: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> Response:
        return requests.get(url, headers=headers, params=params)

    @staticmethod
    def post(url: str, headers: Optional[dict] = None, params: Optional[dict] = None, json: Optional[str] = None,
             data: Optional[dict] = None) -> Response:
        return requests.post(url, headers=headers, params=params, json=json, data=data)

    @staticmethod
    def put(url: str, headers: Optional[dict] = None, params: Optional[dict] = None, json: Optional[str] = None,
            data: Optional[dict] = None) -> Response:
        return requests.put(url, headers=headers, params=params, json=json, data=data)

    @staticmethod
    def delete(url: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> Response:
        return requests.delete(url, headers=headers, params=params)
