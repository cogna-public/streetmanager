# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_streets**](DefaultApi.md#get_streets) | **POST** /nsg/streets/search | 
[**get_streets_by_query**](DefaultApi.md#get_streets_by_query) | **GET** /nsg/search | 
[**get_streets_by_usrn**](DefaultApi.md#get_streets_by_usrn) | **GET** /nsg/streets/{usrn} | 

# **get_streets**
> list[StreetResponse] get_streets(body)



See API specification Resource Guide > Street Lookup API > Get streets endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.StreetsRequest() # StreetsRequest | 

try:
    api_response = api_instance.get_streets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_streets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StreetsRequest**](StreetsRequest.md)|  | 

### Return type

[**list[StreetResponse]**](StreetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streets_by_query**
> list[StreetSummaryResponse] get_streets_by_query(query)



See API specification Resource Guide > Street Lookup API > Get nsg search endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | 

try:
    api_response = api_instance.get_streets_by_query(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_streets_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 

### Return type

[**list[StreetSummaryResponse]**](StreetSummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streets_by_usrn**
> StreetResponse get_streets_by_usrn(usrn)



See API specification Resource Guide > Street Lookup API > Get streets endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
usrn = 1.2 # float | 

try:
    api_response = api_instance.get_streets_by_usrn(usrn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_streets_by_usrn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usrn** | **float**|  | 

### Return type

[**StreetResponse**](StreetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

