# Street Manager Python Client

A Python client library for the Street Manager API, providing access to work, geojson, lookup, and party endpoints.

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
from streetmanager.party import swagger_client as party_client

# Create API client instances
work_api = work_client.DefaultApi()
geojson_api = geojson_client.DefaultApi()
lookup_api = lookup_client.DefaultApi()
party_api = party_client.DefaultApi()

# Use the APIs
# Example: Get work details
work_response = work_api.get_work(work_id="123")

# Example: Get GeoJSON data
geojson_response = geojson_api.get_work_geojson(work_id="123")

# Example: Lookup street details
street_response = lookup_api.get_street(usrn="123456")

# Example: Get party details
party_response = party_api.get_party(party_id="123")
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
- GeoJSON API client for accessing geographical data
- Lookup API client for street information
- Party API client for managing party information

## Requirements

- Python 3.12 or higher
- Dependencies are automatically installed with the package

<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/geojson-swagger.json>

<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/work-swagger.json>

<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/lookup-swagger.json>

<https://department-for-transport-streetmanager.github.io/street-manager-docs/api-documentation/V6/V6.0/json/party-swagger.json>
