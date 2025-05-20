# Street Manager Python Client

A Python client library for the Street Manager API, providing access to work, geojson, and lookup endpoints.

## Installation

```bash
uv add streetmanager
```

## Usage

```python
# Import the client modules
from streetmanager.work import swagger_client as work_client
from streetmanager.geojson import swagger_client as geojson_client
from streetmanager.lookup import swagger_client as lookup_client

# Create API client instances
work_api = work_client.DefaultApi()
geojson_api = geojson_client.DefaultApi()
lookup_api = lookup_client.DefaultApi()

# Use the APIs
# Example: Get work details
work_response = work_api.get_work(work_id="123")

# Example: Get GeoJSON data
geojson_response = geojson_api.get_work_geojson(work_id="123")

# Example: Lookup street details
street_response = lookup_api.get_street(usrn="123456")
```

## Features

- Work API client for managing street works
- GeoJSON API client for accessing geographical data
- Lookup API client for street information

## Requirements

- Python 3.12 or higher
- Dependencies are automatically installed with the package

## License

<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/geojson-swagger.json>
<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/work-swagger.json>
<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/lookup-swagger.json>

