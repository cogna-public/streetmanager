# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permit_summaries**](DefaultApi.md#get_permit_summaries) | **POST** /permits/search | 
[**get_works_updates**](DefaultApi.md#get_works_updates) | **GET** /works/updates | 
[**subscribe_to_event**](DefaultApi.md#subscribe_to_event) | **POST** /api-notifications/subscribe | 
[**unsubscribe_to_event**](DefaultApi.md#unsubscribe_to_event) | **POST** /api-notifications/unsubscribe | 

# **get_permit_summaries**
> PermitSearchReportingResponse get_permit_summaries(body)



Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.PermitSearchRequest() # PermitSearchRequest | 

try:
    api_response = api_instance.get_permit_summaries(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitSearchRequest**](PermitSearchRequest.md)|  | 

### Return type

[**PermitSearchReportingResponse**](PermitSearchReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_works_updates**
> WorkUpdateResponse get_works_updates(start_date=start_date, end_date=end_date, exclude_events_from=exclude_events_from, swa_code=swa_code, workstream_prefix=workstream_prefix, update_id=update_id, page_size=page_size)



See API specification Resource Guide > Event API > Polling for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
exclude_events_from = 'exclude_events_from_example' # str |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
workstream_prefix = ['workstream_prefix_example'] # list[str] |  (optional)
update_id = 1.2 # float |  (optional)
page_size = 1.2 # float |  (optional)

try:
    api_response = api_instance.get_works_updates(start_date=start_date, end_date=end_date, exclude_events_from=exclude_events_from, swa_code=swa_code, workstream_prefix=workstream_prefix, update_id=update_id, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_works_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **exclude_events_from** | **str**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **workstream_prefix** | [**list[str]**](str.md)|  | [optional] 
 **update_id** | **float**|  | [optional] 
 **page_size** | **float**|  | [optional] 

### Return type

[**WorkUpdateResponse**](WorkUpdateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_event**
> SubscriptionCreateResponse subscribe_to_event(body)



Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.SubscriptionCreateRequest() # SubscriptionCreateRequest | 

try:
    api_response = api_instance.subscribe_to_event(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->subscribe_to_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionCreateRequest**](SubscriptionCreateRequest.md)|  | 

### Return type

[**SubscriptionCreateResponse**](SubscriptionCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_to_event**
> unsubscribe_to_event(body)



Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.SubscriptionRemoveRequest() # SubscriptionRemoveRequest | 

try:
    api_instance.unsubscribe_to_event(body)
except ApiException as e:
    print("Exception when calling DefaultApi->unsubscribe_to_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionRemoveRequest**](SubscriptionRemoveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

