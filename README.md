# BeeVisionSEO Python Client

A lightweight Python client for interacting with the BeeVisionSEO API.

## Installation

```bash
pip install beevisionseo
```

## Features

- Insert multiple URLs for processing
- Index a single URL
- Automatic URL validation
- Error handling
- Rate limit handling

## Quick Start

```python
from beevisionseo import BeeVisionSEOClient

# Initialize the client
client = BeeVisionSEOClient(api_key="your_api_key_here")

# Insert multiple URLs
result = client.insert_urls([
    "https://example.com/page1",
    "https://example.com/page2"
])
print(result)

# Index a single URL
index_result = client.index_url("https://example.com/page1")
print(index_result)
```

## Functional Approach

If you prefer a functional approach:

```python
from beevisionseo import insert_urls, index_url

# Insert multiple URLs
result = insert_urls(
    api_key="your_api_key_here",
    urls=["https://example.com/page1", "https://example.com/page2"]
)

# Index a single URL
index_result = index_url(
    api_key="your_api_key_here",
    url="https://example.com/page1"
)
```

## Error Handling

The library handles errors gracefully:

```python
try:
    result = client.insert_urls(["https://example.com/page1"])
except ValueError as e:
    print(f"Validation error: {str(e)}")
except Exception as e:
    print(f"API error: {str(e)}")
```

## Rate Limiting

The API has a rate limit of 10 requests per minute. The client will raise an exception if the rate limit is exceeded.

## API Reference

### `BeeVisionSEOClient`

**Parameters:**
- `api_key` (str): Your BeeVisionSEO API key
- `base_url` (str, optional): Base URL for the API. Defaults to "https://api.beevisionseo.com"

**Methods:**
- `insert_urls(urls)`: Insert URLs for processing
- `index_url(url)`: Index a single URL

### Functional API

- `create_client(api_key, base_url)`: Create a new BeeVisionSEO client
- `insert_urls(api_key, urls, base_url)`: Insert URLs for processing
- `index_url(api_key, url, base_url)`: Index a single URL

## License

MIT