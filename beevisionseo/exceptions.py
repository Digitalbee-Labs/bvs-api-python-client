# beevisionseo/exceptions.py
"""Exceptions for the BeeVisionSEO client library."""


class BeeVisionSEOError(Exception):
    """Base exception for all BeeVisionSEO errors."""

    def __init__(self, message, status_code=None, response=None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)


class ValidationError(BeeVisionSEOError):
    """Raised when URL validation fails."""
    pass


class APIError(BeeVisionSEOError):
    """Raised when the API returns an error response."""
    pass


class RateLimitError(APIError):
    """Raised when rate limit is exceeded."""
    pass


class AuthenticationError(APIError):
    """Raised when authentication fails."""
    pass