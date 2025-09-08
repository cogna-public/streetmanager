# Street Manager Python Client

[![PyPI version](https://img.shields.io/pypi/v/streetmanager.svg)](https://pypi.org/project/streetmanager/)
[![GitHub Release](https://img.shields.io/github/v/release/cogna-public/streetmanager?display_name=release)](https://github.com/cogna-public/streetmanager/releases)
[![Publish Status](https://github.com/cogna-public/streetmanager/actions/workflows/publish.yml/badge.svg)](https://github.com/cogna-public/streetmanager/actions/workflows/publish.yml)
[![Python Versions](https://img.shields.io/pypi/pyversions/streetmanager.svg)](https://pypi.org/project/streetmanager/)
[![License: MIT](https://img.shields.io/pypi/l/streetmanager.svg)](LICENSE)

A Python client library for the Street Manager API, providing access to work, reporting, lookup, geojson, party, export, event, and sampling endpoints.

## Installation

```bash
uv add streetmanager
```

## Usage

```python
# Import the client modules
from streetmanager.work import swagger_client as work_client
from streetmanager.reporting import swagger_client as reporting_client
from streetmanager.lookup import swagger_client as lookup_client
from streetmanager.geojson import swagger_client as geojson_client
from streetmanager.party import swagger_client as party_client
from streetmanager.export import swagger_client as export_client
from streetmanager.event import swagger_client as event_client
from streetmanager.sampling import swagger_client as sampling_client

# Create API client instances
work_api = work_client.DefaultApi()
reporting_api = reporting_client.DefaultApi()
lookup_api = lookup_client.DefaultApi()
geojson_api = geojson_client.DefaultApi()
party_api = party_client.DefaultApi()
export_api = export_client.DefaultApi()
event_api = event_client.DefaultApi()
sampling_api = sampling_client.DefaultApi()

# Use the APIs
# Example: Get work details
work_response = work_api.get_work(work_id="123")

# Example: Get reporting data
reporting_data = reporting_api.get_activity_reporting()

# Example: Lookup street details
street_response = lookup_api.get_street(usrn="123456")

# Example: Get GeoJSON data
geojson_response = geojson_api.get_work_geojson(work_id="123")

# Example: Get party details
party_response = party_api.get_organisation(organisation_id="123")

# Example: Create CSV export
export_request = export_client.PermitCSVExportRequest()
export_response = export_api.create_permit_csv_export(permit_csv_export_request=export_request)

# Example: Get works updates
works_updates = event_api.get_works_updates()

# Example: Get sampling data
sampling_data = sampling_api.get_sample_inspection_targets()
```

## Authentication

To authenticate with the Street Manager API, you'll need to provide your credentials and use the authentication flow:

```python
import os
from streetmanager.work import swagger_client as streetmanager_client
from streetmanager.work.swagger_client.rest import ApiException

class StreetManagerAPI:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth_response = self._perform_authentication()

    def _perform_authentication(self):
        # Initial configuration for authentication
        configuration = streetmanager_client.Configuration()
        configuration.host = self.base_url

        # Create API client for authentication
        api_client = streetmanager_client.ApiClient(configuration)
        auth_api_instance = streetmanager_client.DefaultApi(api_client)

        # Create authentication request
        auth_request = streetmanager_client.AuthenticationRequest(
            email_address=self.username, password=self.password
        )

        try:
            response = auth_api_instance.authenticate(auth_request)
            return response
        except ApiException as e:
            if e.body:
                print("Response body:", e.body)
            raise

    def get_api_instance(self) -> streetmanager_client.DefaultApi:
        if not self.auth_response:
            raise Exception("Authentication response not available. Ensure authentication was successful.")

        # Create a new configuration for the specific API calls
        configuration = streetmanager_client.Configuration()
        configuration.host = self.base_url

        # Configure for id_token
        configuration.api_key["token"] = self.auth_response.id_token
        configuration.api_key_prefix["token"] = ""

        # Create API client with the token-specific configuration
        api_client = streetmanager_client.ApiClient(configuration)
        return streetmanager_client.DefaultApi(api_client)

# Configuration
BASE_URL = "https://api.sandbox.manage-roadworks.service.gov.uk/v6/work"
USERNAME = "your-email@example.com"
PASSWORD = os.getenv("STREETMANAGER_PASSWORD")  # Store your password securely in environment variables

# Initialize the API Handler
sm_api_handler = StreetManagerAPI(BASE_URL, USERNAME, PASSWORD)

# Get an authenticated API instance
api_instance = sm_api_handler.get_api_instance()

# Now you can use the API instance for authenticated requests
work_response = api_instance.get_work(work_id="123")
```

## Features

- Work API client for managing street works
- Reporting API client for reporting functionality
- Lookup API client for street information
- GeoJSON API client for accessing geographical data
- Party API client for managing party information
- Export API client for data export functionality
- Event API client for getting works updates
- Sampling API client for sampling functionality

## Requirements

- Python 3.12 or higher
- Dependencies are automatically installed with the package

## API Documentation

The following Swagger documentation URLs are available for each API:

- [Work API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/work-swagger.json)
- [Reporting API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/reporting-swagger.json)
- [Lookup API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/lookup-swagger.json)
- [GeoJSON API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/geojson-swagger.json)
- [Party API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/party-swagger.json)
- [Export API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/export-swagger.json)
- [Event API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/event-swagger.json)
- [Sampling API](https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/sampling-swagger.json)

## Releasing

- Bump version in `pyproject.toml` (PEP 440).
- Commit and push to `main`.
- Create a GitHub Release for tag `vX.Y.Z` in `cogna-public/streetmanager` (the tag can be created in the Release UI).
- The GitHub Actions workflow builds wheels/sdist with `uv build` and publishes to PyPI via Trusted Publishing (no token required).

Quick release with Just

Use the Justfile recipe to bump, tag, push, and create the GitHub Release:

```
just release                # bump patch
just release minor          # bump minor
just release major "Notes"  # bump major with release notes
```

Notes
- Requires `gh` CLI authenticated (`gh auth status`).
- Uses `uv version --bump` to update `pyproject.toml` and tags `vX.Y.Z`.

Links
- PyPI project page: https://pypi.org/project/streetmanager/

## Changelog

- See CHANGELOG.md for notable changes and release notes.
- GitHub Releases: https://github.com/cogna-public/streetmanager/releases
