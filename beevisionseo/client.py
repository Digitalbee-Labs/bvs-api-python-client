# beevisionseo/client.py
"""Client implementation for the BeeVisionSEO API."""

import requests
from typing import List, Dict

from .config import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, ENDPOINTS
from .utils import validate_urls, handle_response
from .exceptions import ValidationError


class BeeVisionSEOClient:
    """Client for the BeeVisionSEO API."""

    def __init__(self, api_key: str, base_url: str = DEFAULT_BASE_URL, timeout: int = DEFAULT_TIMEOUT):
        """
        Initialize the BeeVisionSEO client.

        Args:
            api_key: Your BeeVisionSEO API key
            base_url: Base URL for the API
            timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.headers = {
            "X-API-Key": api_key,
            "Content-Type": "application/json"
        }

    def insert_urls(self, urls: List[str]) -> Dict:
        """
        Insert URLs for processing.

        Args:
            urls: List of URLs to insert

        Returns:
            Dictionary containing either insert results or error information

        Raises:
            ValidationError: If URLs are invalid
        """
        try:
            validated_urls = validate_urls(urls)

            endpoint = f"{self.base_url}{ENDPOINTS['insert']}"
            payload = {"urls": validated_urls}

            response = requests.post(
                endpoint,
                json=payload,
                headers=self.headers,
                timeout=self.timeout
            )

            return handle_response(response)
        except ValidationError as e:
            return {
                "error": {
                    "status_code": None,
                    "message": str(e)
                }
            }
        except requests.RequestException as e:
            return {
                "error": {
                    "status_code": None,
                    "message": f"Request failed: {str(e)}"
                }
            }

    def index_url(self, url: str) -> Dict:
        """
        Index a single URL.

        Args:
            url: URL to index

        Returns:
            Dictionary containing either index results or error information

        Raises:
            ValidationError: If URL is invalid
        """
        try:
            validated_urls = validate_urls([url])

            endpoint = f"{self.base_url}{ENDPOINTS['index']}"
            payload = {"urls": validated_urls}

            response = requests.post(
                endpoint,
                json=payload,
                headers=self.headers,
                timeout=self.timeout
            )

            return handle_response(response)
        except ValidationError as e:
            return {
                "error": {
                    "status_code": None,
                    "message": str(e)
                }
            }
        except requests.RequestException as e:
            return {
                "error": {
                    "status_code": None,
                    "message": f"Request failed: {str(e)}"
                }
            }


# Convenient functions for those who prefer functional approach

def create_client(api_key: str, base_url: str = DEFAULT_BASE_URL) -> BeeVisionSEOClient:
    """
    Create a new BeeVisionSEO client.

    Args:
        api_key: Your BeeVisionSEO API key
        base_url: Base URL for the API

    Returns:
        Initialized BeeVisionSEO client
    """
    return BeeVisionSEOClient(api_key, base_url)


def insert_urls(api_key: str, urls: List[str], base_url: str = DEFAULT_BASE_URL) -> Dict:
    """
    Insert URLs for processing.

    Args:
        api_key: Your BeeVisionSEO API key
        urls: List of URLs to insert
        base_url: Base URL for the API

    Returns:
        Dictionary containing either insert results or error information
    """
    client = create_client(api_key, base_url)
    return client.insert_urls(urls)


def index_url(api_key: str, url: str, base_url: str = DEFAULT_BASE_URL) -> Dict:
    """
    Index a single URL.

    Args:
        api_key: Your BeeVisionSEO API key
        url: URL to index
        base_url: Base URL for the API

    Returns:
        Dictionary containing either index results or error information
    """
    client = create_client(api_key, base_url)
    return client.index_url(url)