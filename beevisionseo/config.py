# beevisionseo/config.py
"""Configuration settings for the BeeVisionSEO client library."""

# Default configuration
DEFAULT_BASE_URL = "https://api.beevisionseo.com/api/v1"
MAX_URLS_PER_REQUEST = 100
DEFAULT_TIMEOUT = 30

# API endpoints
ENDPOINTS = {
    "insert": "/insert",
    "index": "/index"
}

# HTTP status code messages
ERROR_MESSAGES = {
    400: "Bad Request: The request was invalid.",
    401: "Unauthorized: Invalid or missing API key.",
    403: "Forbidden: Access denied.",
    404: "Not Found: The requested resource could not be found.",
    429: "Rate Limit Exceeded: Too many requests.",
}