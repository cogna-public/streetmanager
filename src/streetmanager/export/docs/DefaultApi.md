# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_comments_csv**](DefaultApi.md#generate_comments_csv) | **POST** /comments/csv | 
[**generate_expiring_interim_reinstatements_csv**](DefaultApi.md#generate_expiring_interim_reinstatements_csv) | **POST** /reinstatements/expiring-interims/csv | 
[**generate_fees_csv**](DefaultApi.md#generate_fees_csv) | **POST** /fees/csv | 
[**generate_forward_plans_csv**](DefaultApi.md#generate_forward_plans_csv) | **POST** /forward-plans/csv | 
[**generate_fpns_csv**](DefaultApi.md#generate_fpns_csv) | **POST** /fixed-penalty-notices/csv | 
[**generate_inspection_csv**](DefaultApi.md#generate_inspection_csv) | **POST** /inspections/csv | 
[**generate_interested_party_permits**](DefaultApi.md#generate_interested_party_permits) | **POST** /interested-party-permits/csv | 
[**generate_material_classification_csv**](DefaultApi.md#generate_material_classification_csv) | **POST** /material-classifications/csv | 
[**generate_non_compliances_csv**](DefaultApi.md#generate_non_compliances_csv) | **POST** /non-compliances/csv | 
[**generate_pbi_sample_inspection_targets_csv**](DefaultApi.md#generate_pbi_sample_inspection_targets_csv) | **POST** /pbi-sample-inspection-targets/csv | 
[**generate_pbi_sample_inspections_due_csv**](DefaultApi.md#generate_pbi_sample_inspections_due_csv) | **POST** /pbi-sample-inspections-due/csv | 
[**generate_permit_alterations_csv**](DefaultApi.md#generate_permit_alterations_csv) | **POST** /alterations/csv | 
[**generate_permits_csv**](DefaultApi.md#generate_permits_csv) | **POST** /permits/csv | 
[**generate_private_street_notices_csv**](DefaultApi.md#generate_private_street_notices_csv) | **POST** /private-street-notices/csv | 
[**generate_reinspection_csv**](DefaultApi.md#generate_reinspection_csv) | **POST** /reinspections/csv | 
[**generate_reinstatements_csv**](DefaultApi.md#generate_reinstatements_csv) | **POST** /reinstatements/csv | 
[**generate_reinstatements_due_csv**](DefaultApi.md#generate_reinstatements_due_csv) | **POST** /permits/reinstatements-due/csv | 
[**generate_section58_csv**](DefaultApi.md#generate_section58_csv) | **POST** /section-58s/csv | 
[**generate_section74_csv**](DefaultApi.md#generate_section74_csv) | **POST** /section-74s/csv | 
[**generate_section81_csv**](DefaultApi.md#generate_section81_csv) | **POST** /section-81s/csv | 
[**get_csv**](DefaultApi.md#get_csv) | **GET** /csv/{csvId} | 

# **generate_comments_csv**
> CSVExportResponse generate_comments_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Comments CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.CommentCSVExportRequest() # CommentCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_comments_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_comments_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentCSVExportRequest**](CommentCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_expiring_interim_reinstatements_csv**
> CSVExportResponse generate_expiring_interim_reinstatements_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Expiring Interim Reinstatements CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.ExpiringInterimReinstatementCSVExportRequest() # ExpiringInterimReinstatementCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_expiring_interim_reinstatements_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_expiring_interim_reinstatements_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExpiringInterimReinstatementCSVExportRequest**](ExpiringInterimReinstatementCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_fees_csv**
> CSVExportResponse generate_fees_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Fees CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.FeesCSVExportRequest() # FeesCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_fees_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_fees_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeesCSVExportRequest**](FeesCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_forward_plans_csv**
> CSVExportResponse generate_forward_plans_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Forward plans CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.ForwardPlanCSVExportRequest() # ForwardPlanCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_forward_plans_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_forward_plans_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForwardPlanCSVExportRequest**](ForwardPlanCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_fpns_csv**
> CSVExportResponse generate_fpns_csv(body=body)



See API specification Resource Guide > Data Export API > Generate FPNs CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.FPNCSVExportRequest() # FPNCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_fpns_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_fpns_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FPNCSVExportRequest**](FPNCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_inspection_csv**
> CSVExportResponse generate_inspection_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Inspections CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.InspectionCSVExportRequest() # InspectionCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_inspection_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_inspection_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InspectionCSVExportRequest**](InspectionCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_interested_party_permits**
> CSVExportResponse generate_interested_party_permits(body=body)



See API specification Resource Guide > Data Export API > Generate Interested party permits CSV for more information Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.InterestedPartyPermitsCSVExportRequest() # InterestedPartyPermitsCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_interested_party_permits(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_interested_party_permits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterestedPartyPermitsCSVExportRequest**](InterestedPartyPermitsCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_material_classification_csv**
> CSVExportResponse generate_material_classification_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Material Classification CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.MaterialClassificationCSVExportRequest() # MaterialClassificationCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_material_classification_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_material_classification_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaterialClassificationCSVExportRequest**](MaterialClassificationCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_non_compliances_csv**
> CSVExportResponse generate_non_compliances_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Non Compliances CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.NonComplianceCSVExportRequest() # NonComplianceCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_non_compliances_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_non_compliances_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NonComplianceCSVExportRequest**](NonComplianceCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pbi_sample_inspection_targets_csv**
> CSVExportResponse generate_pbi_sample_inspection_targets_csv(body=body)



See API specification Resource Guide > Data Export API > Generate PBI sample inspection targets CSV for more information Authenticated user must have one of the following roles: Admin or StreetWorksAdmin

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
body = swagger_client.PbiSampleInspectionTargetCSVExportRequest() # PbiSampleInspectionTargetCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_pbi_sample_inspection_targets_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_pbi_sample_inspection_targets_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PbiSampleInspectionTargetCSVExportRequest**](PbiSampleInspectionTargetCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pbi_sample_inspections_due_csv**
> CSVExportResponse generate_pbi_sample_inspections_due_csv(body=body)



See API specification Resource Guide > Data Export API > Generate PBI Sample Inspections Due CSV for more information Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.PbiSampleInspectionsDueCSVExportRequest() # PbiSampleInspectionsDueCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_pbi_sample_inspections_due_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_pbi_sample_inspections_due_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PbiSampleInspectionsDueCSVExportRequest**](PbiSampleInspectionsDueCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_permit_alterations_csv**
> CSVExportResponse generate_permit_alterations_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Permit alterations CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.PermitAlterationCSVExportRequest() # PermitAlterationCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_permit_alterations_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_permit_alterations_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitAlterationCSVExportRequest**](PermitAlterationCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_permits_csv**
> CSVExportResponse generate_permits_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Permits CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.PermitCSVExportRequest() # PermitCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_permits_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_permits_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitCSVExportRequest**](PermitCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_private_street_notices_csv**
> CSVExportResponse generate_private_street_notices_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Private Street Notices CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.PrivateStreetCSVExportRequest() # PrivateStreetCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_private_street_notices_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_private_street_notices_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrivateStreetCSVExportRequest**](PrivateStreetCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_reinspection_csv**
> CSVExportResponse generate_reinspection_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Inspections CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.ReinspectionCSVExportRequest() # ReinspectionCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_reinspection_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_reinspection_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReinspectionCSVExportRequest**](ReinspectionCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_reinstatements_csv**
> CSVExportResponse generate_reinstatements_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Reinstatements CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.ReinstatementCSVExportRequest() # ReinstatementCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_reinstatements_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_reinstatements_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReinstatementCSVExportRequest**](ReinstatementCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_reinstatements_due_csv**
> CSVExportResponse generate_reinstatements_due_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Reinstatements due CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.ReinstatementsDueCSVExportRequest() # ReinstatementsDueCSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_reinstatements_due_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_reinstatements_due_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReinstatementsDueCSVExportRequest**](ReinstatementsDueCSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_section58_csv**
> CSVExportResponse generate_section58_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Section 58s CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.Section58CSVExportRequest() # Section58CSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_section58_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_section58_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section58CSVExportRequest**](Section58CSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_section74_csv**
> CSVExportResponse generate_section74_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Section 74s CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.Section74CSVExportRequest() # Section74CSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_section74_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_section74_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section74CSVExportRequest**](Section74CSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_section81_csv**
> CSVExportResponse generate_section81_csv(body=body)



See API specification Resource Guide > Data Export API > Generate Section 81s CSV for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.Section81CSVExportRequest() # Section81CSVExportRequest |  (optional)

try:
    api_response = api_instance.generate_section81_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_section81_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section81CSVExportRequest**](Section81CSVExportRequest.md)|  | [optional] 

### Return type

[**CSVExportResponse**](CSVExportResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv**
> str get_csv(csv_id)



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
csv_id = 1.2 # float | 

try:
    api_response = api_instance.get_csv(csv_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_id** | **float**|  | 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

