# beevisionseo/utils.py
"""Utility functions for the BeeVisionSEO client library."""

from typing import List, Dict
from urllib.parse import urlparse
import requests

from .config import MAX_URLS_PER_REQUEST, ERROR_MESSAGES
from .exceptions import ValidationError


def validate_urls(urls: List[str]) -> List[str]:
    """
    Validate the provided URLs.

    Args:
        urls: List of URLs to validate

    Returns:
        List of validated URLs

    Raises:
        ValidationError: If URLs are invalid, duplicate, or exceed maximum allowed
    """
    # Check URL limit
    if len(urls) > MAX_URLS_PER_REQUEST:
        raise ValidationError(f"You can insert a maximum of {MAX_URLS_PER_REQUEST} URLs per request.")

    # Check for duplicates
    if len(urls) != len(set(urls)):
        raise ValidationError("Duplicate URLs are not allowed.")

    # Validate each URL format
    validated_urls = []
    for url in urls:
        try:
            parsed = urlparse(url)
            if not all([parsed.scheme, parsed.netloc]):
                raise ValidationError(f"Invalid URL format: {url}")
            validated_urls.append(url)
        except Exception as e:
            raise ValidationError(f"Invalid URL: {url}. Error: {str(e)}")

    return validated_urls


def handle_response(response: requests.Response) -> Dict:
    """
    Handle the API response and return structured error info instead of raising.

    Args:
        response: Response from the API

    Returns:
        Dictionary with either 'data' or 'error' key in specified detail format
    """
    try:
        # Attempt to parse JSON response
        try:
            data = response.json()
        except ValueError as ve:
            return {
                "error": {
                    "status_code": response.status_code,
                    "detail": [{
                        "type": "invalid_json",
                        "loc": ["body"],
                        "msg": f"Invalid JSON response from server: {str(ve)}",
                        "input": response.text
                    }]
                }
            }

        # Success case
        if response.status_code == 200:
            return {"data": data}

        # Handle error cases
        if response.status_code in ERROR_MESSAGES:
            base_message = ERROR_MESSAGES[response.status_code]
            # Check if API provided detailed error messages
            if isinstance(data.get("detail"), list):
                return {
                    "error": {
                        "status_code": response.status_code,
                        "detail": data["detail"]
                    }
                }
            # Construct default error format
            error_detail = [{
                "type": "api_error",
                "loc": ["response"],
                "msg": base_message,
                "input": None
            }]
        elif response.status_code >= 500:
            error_detail = [{
                "type": "server_error",
                "loc": ["server"],
                "msg": "Server Error: An error occurred on the server.",
                "input": None
            }]
        else:
            error_detail = [{
                "type": "unknown_error",
                "loc": ["response"],
                "msg": "Unexpected error occurred.",
                "input": None
            }]

        return {
            "error": {
                "status_code": response.status_code,
                "detail": error_detail
            }
        }

    except Exception as e:
        # Catch any unexpected errors
        return {
            "error": {
                "status_code": 500,
                "detail": [{
                    "type": "internal_error",
                    "loc": ["server"],
                    "msg": f"Internal server error: {str(e)}",
                    "input": None
                }]
            }
        }