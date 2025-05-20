# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activities_intersecting_bounds**](DefaultApi.md#get_activities_intersecting_bounds) | **GET** /activities | 
[**get_ancillary_information_intersect_bounding_box**](DefaultApi.md#get_ancillary_information_intersect_bounding_box) | **GET** /ancillary-informations | 
[**get_forward_plans_intersect_bounding_box**](DefaultApi.md#get_forward_plans_intersect_bounding_box) | **GET** /forward-plans | 
[**get_hs2_act_limits_intersecting_bounds**](DefaultApi.md#get_hs2_act_limits_intersecting_bounds) | **GET** /hs2-act-limits | 
[**get_material_classifications_intersect_bounding_box**](DefaultApi.md#get_material_classifications_intersect_bounding_box) | **GET** /material-classifications | 
[**get_section58s_intersect_bounding_box**](DefaultApi.md#get_section58s_intersect_bounding_box) | **GET** /section-58s | 
[**get_works_intersect_bounding_box**](DefaultApi.md#get_works_intersect_bounding_box) | **GET** /works | 

# **get_activities_intersecting_bounds**
> ActivityResponse get_activities_intersecting_bounds(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date)



See API specification Resource Guide > GeoJSON API > Get activities endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float | 
min_northing = 1.2 # float | 
max_easting = 1.2 # float | 
max_northing = 1.2 # float | 
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_activities_intersecting_bounds(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_activities_intersecting_bounds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | 
 **min_northing** | **float**|  | 
 **max_easting** | **float**|  | 
 **max_northing** | **float**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**ActivityResponse**](ActivityResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancillary_information_intersect_bounding_box**
> AncillaryInfoResponse get_ancillary_information_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, ancillary_info_reference_number=ancillary_info_reference_number)



See API specification Resource Guide > GeoJSON API > Get AncillaryInformations endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float | 
min_northing = 1.2 # float | 
max_easting = 1.2 # float | 
max_northing = 1.2 # float | 
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
ancillary_info_reference_number = 'ancillary_info_reference_number_example' # str |  (optional)

try:
    api_response = api_instance.get_ancillary_information_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, ancillary_info_reference_number=ancillary_info_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ancillary_information_intersect_bounding_box: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | 
 **min_northing** | **float**|  | 
 **max_easting** | **float**|  | 
 **max_northing** | **float**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **ancillary_info_reference_number** | **str**|  | [optional] 

### Return type

[**AncillaryInfoResponse**](AncillaryInfoResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forward_plans_intersect_bounding_box**
> ForwardPlanResponse get_forward_plans_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, forward_plan_reference_number=forward_plan_reference_number)



See API specification Resource Guide > GeoJSON API > Get ForwardPlans endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float | 
min_northing = 1.2 # float | 
max_easting = 1.2 # float | 
max_northing = 1.2 # float | 
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
forward_plan_reference_number = 'forward_plan_reference_number_example' # str |  (optional)

try:
    api_response = api_instance.get_forward_plans_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, forward_plan_reference_number=forward_plan_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_forward_plans_intersect_bounding_box: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | 
 **min_northing** | **float**|  | 
 **max_easting** | **float**|  | 
 **max_northing** | **float**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **forward_plan_reference_number** | **str**|  | [optional] 

### Return type

[**ForwardPlanResponse**](ForwardPlanResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hs2_act_limits_intersecting_bounds**
> Hs2ActLimitsResponse get_hs2_act_limits_intersecting_bounds(min_easting, min_northing, max_easting, max_northing, phase)



See API specification Resource Guide > GeoJSON API > Get Hs2ActLimits endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float | 
min_northing = 1.2 # float | 
max_easting = 1.2 # float | 
max_northing = 1.2 # float | 
phase = swagger_client.Hs2ActLimitPhase() # Hs2ActLimitPhase | 

try:
    api_response = api_instance.get_hs2_act_limits_intersecting_bounds(min_easting, min_northing, max_easting, max_northing, phase)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_hs2_act_limits_intersecting_bounds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | 
 **min_northing** | **float**|  | 
 **max_easting** | **float**|  | 
 **max_northing** | **float**|  | 
 **phase** | [**Hs2ActLimitPhase**](.md)|  | 

### Return type

[**Hs2ActLimitsResponse**](Hs2ActLimitsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_classifications_intersect_bounding_box**
> MaterialClassificationResponse get_material_classifications_intersect_bounding_box(min_easting=min_easting, min_northing=min_northing, max_easting=max_easting, max_northing=max_northing, sample_date_from=sample_date_from, sample_date_to=sample_date_to, usrn=usrn, classification=classification)



See API specification Resource Guide > GeoJSON API > Get Material Classifications endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float |  (optional)
min_northing = 1.2 # float |  (optional)
max_easting = 1.2 # float |  (optional)
max_northing = 1.2 # float |  (optional)
sample_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sample_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
usrn = 1.2 # float |  (optional)
classification = swagger_client.MaterialClassificationClassification() # MaterialClassificationClassification |  (optional)

try:
    api_response = api_instance.get_material_classifications_intersect_bounding_box(min_easting=min_easting, min_northing=min_northing, max_easting=max_easting, max_northing=max_northing, sample_date_from=sample_date_from, sample_date_to=sample_date_to, usrn=usrn, classification=classification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_material_classifications_intersect_bounding_box: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | [optional] 
 **min_northing** | **float**|  | [optional] 
 **max_easting** | **float**|  | [optional] 
 **max_northing** | **float**|  | [optional] 
 **sample_date_from** | **datetime**|  | [optional] 
 **sample_date_to** | **datetime**|  | [optional] 
 **usrn** | **float**|  | [optional] 
 **classification** | [**MaterialClassificationClassification**](.md)|  | [optional] 

### Return type

[**MaterialClassificationResponse**](MaterialClassificationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section58s_intersect_bounding_box**
> Section58Response get_section58s_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, section_58_reference_number=section_58_reference_number)



See API specification Resource Guide > GeoJSON API > Get Section 58s endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float | 
min_northing = 1.2 # float | 
max_easting = 1.2 # float | 
max_northing = 1.2 # float | 
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
section_58_reference_number = 'section_58_reference_number_example' # str |  (optional)

try:
    api_response = api_instance.get_section58s_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, section_58_reference_number=section_58_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section58s_intersect_bounding_box: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | 
 **min_northing** | **float**|  | 
 **max_easting** | **float**|  | 
 **max_northing** | **float**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **section_58_reference_number** | **str**|  | [optional] 

### Return type

[**Section58Response**](Section58Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_works_intersect_bounding_box**
> WorkResponse get_works_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, work_reference_number=work_reference_number)



See API specification Resource Guide > GeoJSON API > Get works endpoint for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
min_easting = 1.2 # float | 
min_northing = 1.2 # float | 
max_easting = 1.2 # float | 
max_northing = 1.2 # float | 
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)

try:
    api_response = api_instance.get_works_intersect_bounding_box(min_easting, min_northing, max_easting, max_northing, start_date=start_date, end_date=end_date, work_reference_number=work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_works_intersect_bounding_box: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_easting** | **float**|  | 
 **min_northing** | **float**|  | 
 **max_easting** | **float**|  | 
 **max_northing** | **float**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 

### Return type

[**WorkResponse**](WorkResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

