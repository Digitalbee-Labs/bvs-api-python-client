"""
BeeVisionSEO Python Client Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lightweight Python client for interacting with the BeeVisionSEO API.

:copyright: (c) 2025 BeeVisionSEO
:license: MIT
"""

from .client import (
    BeeVisionSEOClient,
    create_client,
    insert_urls,
    index_url
)
from .exceptions import BeeVisionSEOError

__version__ = "0.1.0"
__author__ = "BeeVisionSEO Team"
__all__ = [
    'BeeVisionSEOClient',
    'create_client',
    'insert_urls',
    'index_url',
    'BeeVisionSEOError'
]