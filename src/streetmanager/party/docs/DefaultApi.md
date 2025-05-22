# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workstream**](DefaultApi.md#create_workstream) | **POST** /organisations/{organisationReference}/workstreams | 
[**forgot_password**](DefaultApi.md#forgot_password) | **POST** /forgot-password | 
[**get_organisation**](DefaultApi.md#get_organisation) | **GET** /organisations/{organisationReference} | 
[**get_organisations**](DefaultApi.md#get_organisations) | **GET** /organisations | 
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{email} | 
[**get_workstream**](DefaultApi.md#get_workstream) | **GET** /organisations/{organisationReference}/workstreams/{workstreamPrefix} | 
[**get_workstreams**](DefaultApi.md#get_workstreams) | **GET** /organisations/{organisationReference}/workstreams | 
[**logout**](DefaultApi.md#logout) | **POST** /logout | 
[**refresh**](DefaultApi.md#refresh) | **POST** /refresh | 
[**reset_password**](DefaultApi.md#reset_password) | **POST** /reset-password | 
[**update_user_details**](DefaultApi.md#update_user_details) | **PUT** /users/{email} | 
[**update_workstream**](DefaultApi.md#update_workstream) | **PUT** /organisations/{organisationReference}/workstreams/{workstreamPrefix} | 

# **create_workstream**
> WorkstreamCreateResponse create_workstream(body, organisation_reference)



See API specification Resource Guide > Party API > Post workstreams for more information Authenticated user must have one of the following roles: Planner, Admin

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
body = swagger_client.WorkstreamCreateRequest() # WorkstreamCreateRequest | 
organisation_reference = 'organisation_reference_example' # str | 

try:
    api_response = api_instance.create_workstream(body, organisation_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_workstream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkstreamCreateRequest**](WorkstreamCreateRequest.md)|  | 
 **organisation_reference** | **str**|  | 

### Return type

[**WorkstreamCreateResponse**](WorkstreamCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password**
> forgot_password(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UserForgotPasswordRequest() # UserForgotPasswordRequest | 

try:
    api_instance.forgot_password(body)
except ApiException as e:
    print("Exception when calling DefaultApi->forgot_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserForgotPasswordRequest**](UserForgotPasswordRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisation**
> OrganisationResponse get_organisation(organisation_reference)



See API specification Resource Guide > Party API > Get organisation for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
organisation_reference = 'organisation_reference_example' # str | 

try:
    api_response = api_instance.get_organisation(organisation_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_reference** | **str**|  | 

### Return type

[**OrganisationResponse**](OrganisationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisations**
> list[OrganisationSummaryResponse] get_organisations(type=type, query=query)



See API specification Resource Guide > Party API > Get organisations for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
type = [swagger_client.OrganisationType()] # list[OrganisationType] |  (optional)
query = 'query_example' # str |  (optional)

try:
    api_response = api_instance.get_organisations(type=type, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[OrganisationType]**](OrganisationType.md)|  | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**list[OrganisationSummaryResponse]**](OrganisationSummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(email, swa_code=swa_code)



Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
email = 'email_example' # str | 
swa_code = 'swa_code_example' # str |  (optional)

try:
    api_response = api_instance.get_user(email, swa_code=swa_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **swa_code** | **str**|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workstream**
> WorkstreamResponse get_workstream(organisation_reference, workstream_prefix)



See API specification Resource Guide > Party API > Get workstream for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
organisation_reference = 'organisation_reference_example' # str | 
workstream_prefix = 'workstream_prefix_example' # str | 

try:
    api_response = api_instance.get_workstream(organisation_reference, workstream_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workstream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_reference** | **str**|  | 
 **workstream_prefix** | **str**|  | 

### Return type

[**WorkstreamResponse**](WorkstreamResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workstreams**
> list[WorkstreamResponse] get_workstreams(organisation_reference)



See API specification Resource Guide > Party API > Get workstreams for more information Authenticated user must have one of the following roles: Planner, Contractor, Admin

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
organisation_reference = 'organisation_reference_example' # str | 

try:
    api_response = api_instance.get_workstreams(organisation_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workstreams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_reference** | **str**|  | 

### Return type

[**list[WorkstreamResponse]**](WorkstreamResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.LogoutRequest() # LogoutRequest | 

try:
    api_instance.logout(body)
except ApiException as e:
    print("Exception when calling DefaultApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogoutRequest**](LogoutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
> TokenRefreshResponse refresh(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.TokenRefreshRequest() # TokenRefreshRequest | 

try:
    api_response = api_instance.refresh(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRefreshRequest**](TokenRefreshRequest.md)|  | 

### Return type

[**TokenRefreshResponse**](TokenRefreshResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UserResetPasswordRequest() # UserResetPasswordRequest | 

try:
    api_instance.reset_password(body)
except ApiException as e:
    print("Exception when calling DefaultApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserResetPasswordRequest**](UserResetPasswordRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_details**
> update_user_details(body, email)



Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
body = swagger_client.UpdateUserDetailsRequest() # UpdateUserDetailsRequest | 
email = 'email_example' # str | 

try:
    api_instance.update_user_details(body, email)
except ApiException as e:
    print("Exception when calling DefaultApi->update_user_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserDetailsRequest**](UpdateUserDetailsRequest.md)|  | 
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workstream**
> update_workstream(body, organisation_reference, workstream_prefix)



See API specification Resource Guide > Party API > Put workstream for more information Authenticated user must have one of the following roles: Planner, Admin

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
body = swagger_client.WorkstreamUpdateRequest() # WorkstreamUpdateRequest | 
organisation_reference = 'organisation_reference_example' # str | 
workstream_prefix = 'workstream_prefix_example' # str | 

try:
    api_instance.update_workstream(body, organisation_reference, workstream_prefix)
except ApiException as e:
    print("Exception when calling DefaultApi->update_workstream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkstreamUpdateRequest**](WorkstreamUpdateRequest.md)|  | 
 **organisation_reference** | **str**|  | 
 **workstream_prefix** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

