# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sample_inspection_target**](DefaultApi.md#create_sample_inspection_target) | **POST** /sample-inspection-targets | 
[**delete_sample_inspection_target**](DefaultApi.md#delete_sample_inspection_target) | **DELETE** /sample-inspection-targets/{sampleInspectionTargetReferenceNumber} | 
[**end_quarter**](DefaultApi.md#end_quarter) | **POST** /sample-inspections/end-quarter | 
[**generate_sample_inspections**](DefaultApi.md#generate_sample_inspections) | **POST** /sample-inspections | 
[**get_previous_annual_inspection_units**](DefaultApi.md#get_previous_annual_inspection_units) | **GET** /previous-annual-inspection-units | 
[**get_sample_inspection_quota**](DefaultApi.md#get_sample_inspection_quota) | **GET** /sample-inspection-quota | 
[**get_sample_inspection_target**](DefaultApi.md#get_sample_inspection_target) | **GET** /sample-inspection-targets/{sampleInspectionTargetReferenceNumber} | 
[**revert_end_quarter**](DefaultApi.md#revert_end_quarter) | **POST** /sample-inspections/revert-end-quarter | 
[**start_quarter**](DefaultApi.md#start_quarter) | **POST** /sample-inspections/start-quarter | 
[**update_sample_inspection_target**](DefaultApi.md#update_sample_inspection_target) | **PUT** /sample-inspection-targets/{sampleInspectionTargetReferenceNumber} | 

# **create_sample_inspection_target**
> SampleInspectionTargetCreateResponse create_sample_inspection_target(body)



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
body = swagger_client.SampleInspectionTargetCreateRequest() # SampleInspectionTargetCreateRequest | 

try:
    api_response = api_instance.create_sample_inspection_target(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_sample_inspection_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SampleInspectionTargetCreateRequest**](SampleInspectionTargetCreateRequest.md)|  | 

### Return type

[**SampleInspectionTargetCreateResponse**](SampleInspectionTargetCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sample_inspection_target**
> delete_sample_inspection_target(sample_inspection_target_reference_number)



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
sample_inspection_target_reference_number = 'sample_inspection_target_reference_number_example' # str | 

try:
    api_instance.delete_sample_inspection_target(sample_inspection_target_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_sample_inspection_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_inspection_target_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_quarter**
> end_quarter()



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

try:
    api_instance.end_quarter()
except ApiException as e:
    print("Exception when calling DefaultApi->end_quarter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sample_inspections**
> generate_sample_inspections(body)



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
body = swagger_client.GenerateSampleInspectionsRequest() # GenerateSampleInspectionsRequest | 

try:
    api_instance.generate_sample_inspections(body)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_sample_inspections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateSampleInspectionsRequest**](GenerateSampleInspectionsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_previous_annual_inspection_units**
> AnnualInspectionUnitsResponse get_previous_annual_inspection_units(promoter_org_ref, financial_year_start_date=financial_year_start_date)



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
promoter_org_ref = 'promoter_org_ref_example' # str | 
financial_year_start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_previous_annual_inspection_units(promoter_org_ref, financial_year_start_date=financial_year_start_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_previous_annual_inspection_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promoter_org_ref** | **str**|  | 
 **financial_year_start_date** | **datetime**|  | [optional] 

### Return type

[**AnnualInspectionUnitsResponse**](AnnualInspectionUnitsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_inspection_quota**
> SampleInspectionQuotaResponse get_sample_inspection_quota(inspection_units, inspection_rate)



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
inspection_units = [3.4] # list[float] | 
inspection_rate = 1.2 # float | 

try:
    api_response = api_instance.get_sample_inspection_quota(inspection_units, inspection_rate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sample_inspection_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_units** | [**list[float]**](float.md)|  | 
 **inspection_rate** | **float**|  | 

### Return type

[**SampleInspectionQuotaResponse**](SampleInspectionQuotaResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_inspection_target**
> SampleInspectionTargetResponse get_sample_inspection_target(sample_inspection_target_reference_number)



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
sample_inspection_target_reference_number = 'sample_inspection_target_reference_number_example' # str | 

try:
    api_response = api_instance.get_sample_inspection_target(sample_inspection_target_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sample_inspection_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sample_inspection_target_reference_number** | **str**|  | 

### Return type

[**SampleInspectionTargetResponse**](SampleInspectionTargetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_end_quarter**
> revert_end_quarter()



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

try:
    api_instance.revert_end_quarter()
except ApiException as e:
    print("Exception when calling DefaultApi->revert_end_quarter: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_quarter**
> start_quarter(body)



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
body = swagger_client.SampleInspectionStartQuarterRequest() # SampleInspectionStartQuarterRequest | 

try:
    api_instance.start_quarter(body)
except ApiException as e:
    print("Exception when calling DefaultApi->start_quarter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SampleInspectionStartQuarterRequest**](SampleInspectionStartQuarterRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sample_inspection_target**
> update_sample_inspection_target(body, sample_inspection_target_reference_number)



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
body = swagger_client.SampleInspectionTargetUpdateRequest() # SampleInspectionTargetUpdateRequest | 
sample_inspection_target_reference_number = 'sample_inspection_target_reference_number_example' # str | 

try:
    api_instance.update_sample_inspection_target(body, sample_inspection_target_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_sample_inspection_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SampleInspectionTargetUpdateRequest**](SampleInspectionTargetUpdateRequest.md)|  | 
 **sample_inspection_target_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

