# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_hs2_permit**](DefaultApi.md#acknowledge_hs2_permit) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/hs2_acknowledgement | 
[**add_file_to_work**](DefaultApi.md#add_file_to_work) | **POST** /works/{workReferenceNumber}/files | 
[**authenticate**](DefaultApi.md#authenticate) | **POST** /authenticate | 
[**calculate_duration**](DefaultApi.md#calculate_duration) | **GET** /duration | 
[**cancel_activity**](DefaultApi.md#cancel_activity) | **PUT** /activity/{activityReferenceNumber}/cancel | 
[**cancel_forward_plan**](DefaultApi.md#cancel_forward_plan) | **PUT** /works/{workReferenceNumber}/forward-plans/{forwardPlanReferenceNumber}/cancel | 
[**cancel_private_street_notice**](DefaultApi.md#cancel_private_street_notice) | **PUT** /works/{workReferenceNumber}/private-street-notices/{privateStreetReferenceNumber}/cancel | 
[**create_activity**](DefaultApi.md#create_activity) | **POST** /activity | 
[**create_ancillary_info**](DefaultApi.md#create_ancillary_info) | **POST** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/ancillary-informations | 
[**create_forward_plan**](DefaultApi.md#create_forward_plan) | **POST** /forward-plans | 
[**create_fpn**](DefaultApi.md#create_fpn) | **POST** /works/{workReferenceNumber}/fixed-penalty-notices | 
[**create_geographical_area**](DefaultApi.md#create_geographical_area) | **POST** /geographical-areas | 
[**create_historic_fpn**](DefaultApi.md#create_historic_fpn) | **POST** /historic-works/fixed-penalty-notices | 
[**create_historic_inspection**](DefaultApi.md#create_historic_inspection) | **POST** /historic-works/inspections | 
[**create_inspection**](DefaultApi.md#create_inspection) | **POST** /works/{workReferenceNumber}/inspections | 
[**create_materials_classification**](DefaultApi.md#create_materials_classification) | **POST** /material-classifications | 
[**create_non_notifiable_site**](DefaultApi.md#create_non_notifiable_site) | **POST** /non-notifiable-works/sites | 
[**create_permit**](DefaultApi.md#create_permit) | **POST** /works/{workReferenceNumber}/permits | 
[**create_permit_alteration**](DefaultApi.md#create_permit_alteration) | **POST** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/alterations | 
[**create_private_street_notice**](DefaultApi.md#create_private_street_notice) | **POST** /private-street-notices | 
[**create_reinstatement**](DefaultApi.md#create_reinstatement) | **POST** /works/{workReferenceNumber}/sites/{siteReferenceNumber}/reinstatements | 
[**create_scheduled_inspection**](DefaultApi.md#create_scheduled_inspection) | **POST** /works/{workReferenceNumber}/scheduled-inspections | 
[**create_section58**](DefaultApi.md#create_section58) | **POST** /section-58s | 
[**create_section74**](DefaultApi.md#create_section74) | **POST** /works/{workReferenceNumber}/section-74s | 
[**create_section81**](DefaultApi.md#create_section81) | **POST** /section-81-works/section-81s | 
[**create_site**](DefaultApi.md#create_site) | **POST** /works/{workReferenceNumber}/sites | 
[**create_work**](DefaultApi.md#create_work) | **POST** /works | 
[**delete_file**](DefaultApi.md#delete_file) | **DELETE** /files/{fileId} | 
[**delete_fpn**](DefaultApi.md#delete_fpn) | **DELETE** /works/{workReferenceNumber}/fixed-penalty-notices/{fpnReferenceNumber} | 
[**delete_inspection**](DefaultApi.md#delete_inspection) | **DELETE** /works/{workReferenceNumber}/inspections/{inspectionReferenceNumber} | 
[**delete_reinstatement**](DefaultApi.md#delete_reinstatement) | **DELETE** /works/{workReferenceNumber}/sites/{siteReferenceNumber}/reinstatements/{reinstatementReferenceNumber} | 
[**delete_scheduled_inspection**](DefaultApi.md#delete_scheduled_inspection) | **DELETE** /works/{workReferenceNumber}/scheduled-inspections | 
[**duration_challenge_non_acceptance_response**](DefaultApi.md#duration_challenge_non_acceptance_response) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/alterations/{permitAlterationReferenceNumber}/duration-challenge-non-acceptance-response | 
[**duration_challenge_review**](DefaultApi.md#duration_challenge_review) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/alterations/{permitAlterationReferenceNumber}/duration-challenge-review | 
[**get_activity**](DefaultApi.md#get_activity) | **GET** /activity/{activityReferenceNumber} | 
[**get_ancillary_info**](DefaultApi.md#get_ancillary_info) | **GET** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/ancillary-informations/{ancillaryInformationReferenceNumber} | 
[**get_comment**](DefaultApi.md#get_comment) | **GET** /works/{workReferenceNumber}/comments/{commentReferenceNumber} | 
[**get_earliest_permit**](DefaultApi.md#get_earliest_permit) | **GET** /works/{workReferenceNumber}/earliest-permit | 
[**get_fee_matrix**](DefaultApi.md#get_fee_matrix) | **GET** /fee-matrix/{organisationReference} | 
[**get_file**](DefaultApi.md#get_file) | **GET** /files/{fileId} | 
[**get_forward_plan**](DefaultApi.md#get_forward_plan) | **GET** /works/{workReferenceNumber}/forward-plans/{forwardPlanReferenceNumber} | 
[**get_fpn**](DefaultApi.md#get_fpn) | **GET** /works/{workReferenceNumber}/fixed-penalty-notices/{fpnReferenceNumber} | 
[**get_inspection**](DefaultApi.md#get_inspection) | **GET** /works/{workReferenceNumber}/inspections/{inspectionReferenceNumber} | 
[**get_material_classification**](DefaultApi.md#get_material_classification) | **GET** /material-classifications/{materialClassificationReferenceNumber} | 
[**get_non_compliance**](DefaultApi.md#get_non_compliance) | **GET** /works/{workReferenceNumber}/non-compliances/{nonComplianceReferenceNumber} | 
[**get_permit**](DefaultApi.md#get_permit) | **GET** /works/{workReferenceNumber}/permits/{permitReferenceNumber} | 
[**get_permit_alteration**](DefaultApi.md#get_permit_alteration) | **GET** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/alterations/{permitAlterationReferenceNumber} | 
[**get_private_street_notice**](DefaultApi.md#get_private_street_notice) | **GET** /works/{workReferenceNumber}/private-street-notices/{privateStreetReferenceNumber} | 
[**get_section58**](DefaultApi.md#get_section58) | **GET** /section-58s/{section58ReferenceNumber} | 
[**get_section74**](DefaultApi.md#get_section74) | **GET** /works/{workReferenceNumber}/section-74s/{section74ReferenceNumber} | 
[**get_section81**](DefaultApi.md#get_section81) | **GET** /works/{workReferenceNumber}/section-81s/{section81ReferenceNumber} | 
[**get_site**](DefaultApi.md#get_site) | **GET** /works/{workReferenceNumber}/sites/{siteReferenceNumber} | 
[**get_work**](DefaultApi.md#get_work) | **GET** /works/{workReferenceNumber} | 
[**get_work_category**](DefaultApi.md#get_work_category) | **GET** /permits/category | 
[**get_work_history**](DefaultApi.md#get_work_history) | **GET** /works/{workReferenceNumber}/history | 
[**impose_change**](DefaultApi.md#impose_change) | **POST** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/alterations/impose | 
[**link_permit_to_non_compliance**](DefaultApi.md#link_permit_to_non_compliance) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/link-non-compliance | 
[**link_section81_to_permit**](DefaultApi.md#link_section81_to_permit) | **POST** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/link-section-81 | 
[**mark_comment_as_read**](DefaultApi.md#mark_comment_as_read) | **PUT** /works/{workReferenceNumber}/comments/{commentReferenceNumber}/read | 
[**mark_permit_as_under_assessment**](DefaultApi.md#mark_permit_as_under_assessment) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/under-assessment | 
[**post_comment**](DefaultApi.md#post_comment) | **POST** /works/{workReferenceNumber}/comments | 
[**reassign_section81**](DefaultApi.md#reassign_section81) | **PUT** /works/{workReferenceNumber}/section-81s/{section81ReferenceNumber}/reassign-section-81 | 
[**remove_ancillary_info**](DefaultApi.md#remove_ancillary_info) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/ancillary-informations/{ancillaryInformationReferenceNumber}/remove | 
[**revert_actual_start_date**](DefaultApi.md#revert_actual_start_date) | **PUT** /works/{workReferenceNumber}/revert-start | 
[**revert_actual_stop_date**](DefaultApi.md#revert_actual_stop_date) | **PUT** /works/{workReferenceNumber}/revert-stop | 
[**subsume_site**](DefaultApi.md#subsume_site) | **PUT** /works/{workReferenceNumber}/sites/{siteReferenceNumber}/subsume | 
[**unlink_section81_from_permit**](DefaultApi.md#unlink_section81_from_permit) | **POST** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/unlink-section-81 | 
[**update_activity**](DefaultApi.md#update_activity) | **PUT** /activity/{activityReferenceNumber} | 
[**update_actual_start_date**](DefaultApi.md#update_actual_start_date) | **PUT** /works/{workReferenceNumber}/start | 
[**update_actual_stop_date**](DefaultApi.md#update_actual_stop_date) | **PUT** /works/{workReferenceNumber}/stop | 
[**update_assessment_status**](DefaultApi.md#update_assessment_status) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/assessment | 
[**update_current_traffic_management_type**](DefaultApi.md#update_current_traffic_management_type) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/current-traffic-management-type | 
[**update_excavation_carried_out**](DefaultApi.md#update_excavation_carried_out) | **PUT** /works/{workReferenceNumber}/excavation-carried-out | 
[**update_final_reinstatement**](DefaultApi.md#update_final_reinstatement) | **PUT** /works/{workReferenceNumber}/final-reinstatement | 
[**update_forward_plan**](DefaultApi.md#update_forward_plan) | **PUT** /works/{workReferenceNumber}/forward-plans/{forwardPlanReferenceNumber} | 
[**update_fpn_status**](DefaultApi.md#update_fpn_status) | **PUT** /works/{workReferenceNumber}/fixed-penalty-notices/{fpnReferenceNumber}/status | 
[**update_geographical_area**](DefaultApi.md#update_geographical_area) | **PUT** /geographical-areas/{geographicalAreaReferenceNumber} | 
[**update_inspection_outcome_status**](DefaultApi.md#update_inspection_outcome_status) | **PUT** /works/{workReferenceNumber}/inspections/{inspectionReferenceNumber}/status | 
[**update_non_compliance_status**](DefaultApi.md#update_non_compliance_status) | **PUT** /works/{workReferenceNumber}/non-compliances/{nonComplianceReferenceNumber}/status | 
[**update_permit_alteration_status**](DefaultApi.md#update_permit_alteration_status) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/alterations/{permitAlterationReferenceNumber}/status | 
[**update_permit_discount**](DefaultApi.md#update_permit_discount) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/permit-discount | 
[**update_permit_duration_challenge_non_acceptance_response**](DefaultApi.md#update_permit_duration_challenge_non_acceptance_response) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/duration-challenge-non-acceptance-response | 
[**update_permit_duration_challenge_review**](DefaultApi.md#update_permit_duration_challenge_review) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/duration-challenge-review | 
[**update_permit_lane_rental_assessment**](DefaultApi.md#update_permit_lane_rental_assessment) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/lane-rental-assessments | 
[**update_permit_status**](DefaultApi.md#update_permit_status) | **PUT** /works/{workReferenceNumber}/permits/{permitReferenceNumber}/status | 
[**update_section58_status**](DefaultApi.md#update_section58_status) | **PUT** /section-58s/{section58ReferenceNumber}/status | 
[**update_section74_ha_status**](DefaultApi.md#update_section74_ha_status) | **PUT** /works/{workReferenceNumber}/section-74s/{section74ReferenceNumber}/highway-authority-status | 
[**update_section74_promoter_status**](DefaultApi.md#update_section74_promoter_status) | **PUT** /works/{workReferenceNumber}/section-74s/{section74ReferenceNumber}/promoter-status | 
[**update_section81_status**](DefaultApi.md#update_section81_status) | **PUT** /works/{workReferenceNumber}/section-81s/{section81ReferenceNumber}/status | 
[**upload_file**](DefaultApi.md#upload_file) | **POST** /files | 
[**withdraw_inspection**](DefaultApi.md#withdraw_inspection) | **PUT** /works/{workReferenceNumber}/inspections/{inspectionReferenceNumber}/withdraw | 

# **acknowledge_hs2_permit**
> acknowledge_hs2_permit(body, work_reference_number, permit_reference_number)



Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.HS2AcknowledgementRequest() # HS2AcknowledgementRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.acknowledge_hs2_permit(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->acknowledge_hs2_permit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HS2AcknowledgementRequest**](HS2AcknowledgementRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_file_to_work**
> add_file_to_work(body, work_reference_number)



See API specification Resource Guide > Works API > File upload for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.AddFileToWorkRequest() # AddFileToWorkRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.add_file_to_work(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->add_file_to_work: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddFileToWorkRequest**](AddFileToWorkRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate**
> AuthenticationResponse authenticate(body)



If authenticating for the first time with a temporary password, a 307 Temporary Redirect to `/authenticate/initial` will be returned, which can be called with the same request body.  A sessionToken property may be returned from this redirect endpoint, which can be used to set a permanent password with the `/set-password` endpoint on the Party API.  See API specification Security section for more information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.AuthenticationRequest() # AuthenticationRequest | 

try:
    api_response = api_instance.authenticate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationRequest**](AuthenticationRequest.md)|  | 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_duration**
> DurationCalculationResponse calculate_duration(start_date=start_date, end_date=end_date)



See business rules section 1.2 - Dates and times See glossary - Working day Utility endpoint. Can be used to check what durations will be assigned to a work/permit based on start and end date Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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

try:
    api_response = api_instance.calculate_duration(start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->calculate_duration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**DurationCalculationResponse**](DurationCalculationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_activity**
> cancel_activity(body, activity_reference_number)



Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.ActivityCancelRequest() # ActivityCancelRequest | 
activity_reference_number = 'activity_reference_number_example' # str | 

try:
    api_instance.cancel_activity(body, activity_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityCancelRequest**](ActivityCancelRequest.md)|  | 
 **activity_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_forward_plan**
> cancel_forward_plan(body, work_reference_number, forward_plan_reference_number)



Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.ForwardPlanCancelRequest() # ForwardPlanCancelRequest | 
work_reference_number = 'work_reference_number_example' # str | 
forward_plan_reference_number = 'forward_plan_reference_number_example' # str | 

try:
    api_instance.cancel_forward_plan(body, work_reference_number, forward_plan_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_forward_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForwardPlanCancelRequest**](ForwardPlanCancelRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **forward_plan_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_private_street_notice**
> cancel_private_street_notice(body, work_reference_number, private_street_reference_number)



See business rules section 2.1.7 - Works on private streets Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.PrivateStreetNoticeCancelRequest() # PrivateStreetNoticeCancelRequest | 
work_reference_number = 'work_reference_number_example' # str | 
private_street_reference_number = 'private_street_reference_number_example' # str | 

try:
    api_instance.cancel_private_street_notice(body, work_reference_number, private_street_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_private_street_notice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrivateStreetNoticeCancelRequest**](PrivateStreetNoticeCancelRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **private_street_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity**
> ActivityCreateResponse create_activity(body)



See business rules section 9 - Activities Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.ActivityCreateRequest() # ActivityCreateRequest | 

try:
    api_response = api_instance.create_activity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityCreateRequest**](ActivityCreateRequest.md)|  | 

### Return type

[**ActivityCreateResponse**](ActivityCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ancillary_info**
> CreateAncillaryInfoResponse create_ancillary_info(body, work_reference_number, permit_reference_number)



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
body = swagger_client.CreateAncillaryInfoRequest() # CreateAncillaryInfoRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_response = api_instance.create_ancillary_info(body, work_reference_number, permit_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_ancillary_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAncillaryInfoRequest**](CreateAncillaryInfoRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

[**CreateAncillaryInfoResponse**](CreateAncillaryInfoResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_forward_plan**
> ForwardPlanCreateResponse create_forward_plan(body)



See business rules section 3.3 - Forward plans Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.ForwardPlanCreateRequest() # ForwardPlanCreateRequest | 

try:
    api_response = api_instance.create_forward_plan(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_forward_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForwardPlanCreateRequest**](ForwardPlanCreateRequest.md)|  | 

### Return type

[**ForwardPlanCreateResponse**](ForwardPlanCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fpn**
> FPNCreateResponse create_fpn(body, work_reference_number)



See business rules section 11 - Fixed penalty notice (FPN) Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.FPNCreateRequest() # FPNCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.create_fpn(body, work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_fpn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FPNCreateRequest**](FPNCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

[**FPNCreateResponse**](FPNCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_geographical_area**
> GeographicalAreaCreateResponse create_geographical_area(file, internal_user_identifier, internal_user_name)



See API specification Resource Guide > Works API > Geographical Areas for more information Authenticated user must have one of the following roles: HighwayAuthority, Admin

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
file = 'file_example' # str | 
internal_user_identifier = 'internal_user_identifier_example' # str | 
internal_user_name = 'internal_user_name_example' # str | 

try:
    api_response = api_instance.create_geographical_area(file, internal_user_identifier, internal_user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_geographical_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **internal_user_identifier** | **str**|  | 
 **internal_user_name** | **str**|  | 

### Return type

[**GeographicalAreaCreateResponse**](GeographicalAreaCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_historic_fpn**
> HistoricFPNCreateResponse create_historic_fpn(body)



See business rules section 15 - Historical works See business rules section 11.2 - FPN statuses Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.HistoricFPNCreateRequest() # HistoricFPNCreateRequest | 

try:
    api_response = api_instance.create_historic_fpn(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_historic_fpn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HistoricFPNCreateRequest**](HistoricFPNCreateRequest.md)|  | 

### Return type

[**HistoricFPNCreateResponse**](HistoricFPNCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_historic_inspection**
> HistoricInspectionCreateResponse create_historic_inspection(body)



See business rules section 15 - Historical works See business rules section 10 - Inspections and non-compliance Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.HistoricInspectionCreateRequest() # HistoricInspectionCreateRequest | 

try:
    api_response = api_instance.create_historic_inspection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_historic_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HistoricInspectionCreateRequest**](HistoricInspectionCreateRequest.md)|  | 

### Return type

[**HistoricInspectionCreateResponse**](HistoricInspectionCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inspection**
> InspectionCreateResponse create_inspection(body, work_reference_number)



See business rules section 10 - Inspections and non-compliance Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.InspectionCreateRequest() # InspectionCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.create_inspection(body, work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InspectionCreateRequest**](InspectionCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

[**InspectionCreateResponse**](InspectionCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_materials_classification**
> MaterialClassificationCreateResponse create_materials_classification(body)



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
body = swagger_client.MaterialClassificationCreateRequest() # MaterialClassificationCreateRequest | 

try:
    api_response = api_instance.create_materials_classification(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_materials_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaterialClassificationCreateRequest**](MaterialClassificationCreateRequest.md)|  | 

### Return type

[**MaterialClassificationCreateResponse**](MaterialClassificationCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_non_notifiable_site**
> NonNotifiableSiteCreateResponse create_non_notifiable_site(body)



See business rules section 8 - Sites and reinstatements Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.NonNotifiableSiteCreateRequest() # NonNotifiableSiteCreateRequest | 

try:
    api_response = api_instance.create_non_notifiable_site(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_non_notifiable_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NonNotifiableSiteCreateRequest**](NonNotifiableSiteCreateRequest.md)|  | 

### Return type

[**NonNotifiableSiteCreateResponse**](NonNotifiableSiteCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_permit**
> PermitCreateResponse create_permit(body, work_reference_number)



See business rules section 3.4 - PAA and permit applications (PA) Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.PermitCreateRequest() # PermitCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.create_permit(body, work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_permit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitCreateRequest**](PermitCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

[**PermitCreateResponse**](PermitCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_permit_alteration**
> PermitAlterationCreateResponse create_permit_alteration(body, work_reference_number, permit_reference_number)



See business rules section 4 - Change requests (CR) Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.PermitAlterationCreateRequest() # PermitAlterationCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_response = api_instance.create_permit_alteration(body, work_reference_number, permit_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_permit_alteration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitAlterationCreateRequest**](PermitAlterationCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

[**PermitAlterationCreateResponse**](PermitAlterationCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_private_street_notice**
> PrivateStreetNoticeCreateResponse create_private_street_notice(body)



See business rules section 2.1.7 - Works on private streets Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.PrivateStreetNoticeCreateRequest() # PrivateStreetNoticeCreateRequest | 

try:
    api_response = api_instance.create_private_street_notice(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_private_street_notice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrivateStreetNoticeCreateRequest**](PrivateStreetNoticeCreateRequest.md)|  | 

### Return type

[**PrivateStreetNoticeCreateResponse**](PrivateStreetNoticeCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reinstatement**
> ReinstatementCreateResponse create_reinstatement(body, work_reference_number, site_reference_number)



See business rules section 8 - Sites and reinstatements Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.ReinstatementCreateRequest() # ReinstatementCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
site_reference_number = 'site_reference_number_example' # str | 

try:
    api_response = api_instance.create_reinstatement(body, work_reference_number, site_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_reinstatement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReinstatementCreateRequest**](ReinstatementCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **site_reference_number** | **str**|  | 

### Return type

[**ReinstatementCreateResponse**](ReinstatementCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scheduled_inspection**
> create_scheduled_inspection(body, work_reference_number)



See business rules section 10.4 - Scheduling inspections Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.ScheduledInspectionCreateRequest() # ScheduledInspectionCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.create_scheduled_inspection(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->create_scheduled_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduledInspectionCreateRequest**](ScheduledInspectionCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_section58**
> Section58CreateResponse create_section58(body)



See business rules section 22 - Section 58s Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.Section58CreateRequest() # Section58CreateRequest | 

try:
    api_response = api_instance.create_section58(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_section58: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section58CreateRequest**](Section58CreateRequest.md)|  | 

### Return type

[**Section58CreateResponse**](Section58CreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_section74**
> Section74CreateResponse create_section74(body, work_reference_number)



See business rules section 20 - Section 74s Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.Section74CreateRequest() # Section74CreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.create_section74(body, work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_section74: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section74CreateRequest**](Section74CreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

[**Section74CreateResponse**](Section74CreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_section81**
> Section81CreateResponse create_section81(body)



See business rules section 14.3 - Adding S81s Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.Section81CreateRequest() # Section81CreateRequest | 

try:
    api_response = api_instance.create_section81(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_section81: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section81CreateRequest**](Section81CreateRequest.md)|  | 

### Return type

[**Section81CreateResponse**](Section81CreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site**
> SiteCreateResponse create_site(body, work_reference_number)



See business rules section 8 - Sites and reinstatements Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.SiteCreateRequest() # SiteCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.create_site(body, work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SiteCreateRequest**](SiteCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

[**SiteCreateResponse**](SiteCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_work**
> WorkCreateResponse create_work(body)



See business rules section 3 - Works submissions and applications Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.WorkCreateRequest() # WorkCreateRequest | 

try:
    api_response = api_instance.create_work(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_work: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkCreateRequest**](WorkCreateRequest.md)|  | 

### Return type

[**WorkCreateResponse**](WorkCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_id)



See API specification Resource Guide > Works API > File upload for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
file_id = 1.2 # float | 

try:
    api_instance.delete_file(file_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fpn**
> delete_fpn(work_reference_number, fpn_reference_number)



See business rules section 11 - Fixed penalty notice (FPN) Authenticated user must have one of the following roles: HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
fpn_reference_number = 'fpn_reference_number_example' # str | 

try:
    api_instance.delete_fpn(work_reference_number, fpn_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_fpn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **fpn_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inspection**
> delete_inspection(work_reference_number, inspection_reference_number)



Authenticated user must have one of the following roles: HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
inspection_reference_number = 'inspection_reference_number_example' # str | 

try:
    api_instance.delete_inspection(work_reference_number, inspection_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **inspection_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reinstatement**
> delete_reinstatement(work_reference_number, site_reference_number, reinstatement_reference_number)



See business rules section 8 - Sites and reinstatements Authenticated user must have one of the following roles: Planner, Contractor

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
work_reference_number = 'work_reference_number_example' # str | 
site_reference_number = 'site_reference_number_example' # str | 
reinstatement_reference_number = 'reinstatement_reference_number_example' # str | 

try:
    api_instance.delete_reinstatement(work_reference_number, site_reference_number, reinstatement_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_reinstatement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **site_reference_number** | **str**|  | 
 **reinstatement_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_inspection**
> delete_scheduled_inspection(work_reference_number)



Authenticated user must have one of the following roles: HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.delete_scheduled_inspection(work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_scheduled_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duration_challenge_non_acceptance_response**
> duration_challenge_non_acceptance_response(body, work_reference_number, permit_reference_number, permit_alteration_reference_number)



See business rules section 21.2 - Duration challenge non acceptance response Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.PermitAlterationDurationChallengeNonAcceptanceResponseRequest() # PermitAlterationDurationChallengeNonAcceptanceResponseRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
permit_alteration_reference_number = 'permit_alteration_reference_number_example' # str | 

try:
    api_instance.duration_challenge_non_acceptance_response(body, work_reference_number, permit_reference_number, permit_alteration_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->duration_challenge_non_acceptance_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitAlterationDurationChallengeNonAcceptanceResponseRequest**](PermitAlterationDurationChallengeNonAcceptanceResponseRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **permit_alteration_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duration_challenge_review**
> duration_challenge_review(body, work_reference_number, permit_reference_number, permit_alteration_reference_number)



See business rules section 21.1 - Duration challenge review Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.PermitAlterationDurationChallengeReviewRequest() # PermitAlterationDurationChallengeReviewRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
permit_alteration_reference_number = 'permit_alteration_reference_number_example' # str | 

try:
    api_instance.duration_challenge_review(body, work_reference_number, permit_reference_number, permit_alteration_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->duration_challenge_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitAlterationDurationChallengeReviewRequest**](PermitAlterationDurationChallengeReviewRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **permit_alteration_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> ActivityResponse get_activity(activity_reference_number)



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
activity_reference_number = 'activity_reference_number_example' # str | 

try:
    api_response = api_instance.get_activity(activity_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_reference_number** | **str**|  | 

### Return type

[**ActivityResponse**](ActivityResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancillary_info**
> AncillaryInfoResponse get_ancillary_info(work_reference_number, permit_reference_number, ancillary_information_reference_number)



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
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
ancillary_information_reference_number = 'ancillary_information_reference_number_example' # str | 

try:
    api_response = api_instance.get_ancillary_info(work_reference_number, permit_reference_number, ancillary_information_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ancillary_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **ancillary_information_reference_number** | **str**|  | 

### Return type

[**AncillaryInfoResponse**](AncillaryInfoResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentResponse get_comment(work_reference_number, comment_reference_number)



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
work_reference_number = 'work_reference_number_example' # str | 
comment_reference_number = 'comment_reference_number_example' # str | 

try:
    api_response = api_instance.get_comment(work_reference_number, comment_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **comment_reference_number** | **str**|  | 

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earliest_permit**
> PermitSummaryResponse get_earliest_permit(work_reference_number)



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
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.get_earliest_permit(work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_earliest_permit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 

### Return type

[**PermitSummaryResponse**](PermitSummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_matrix**
> FeeMatrixResponse get_fee_matrix(organisation_reference)



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
organisation_reference = 'organisation_reference_example' # str | 

try:
    api_response = api_instance.get_fee_matrix(organisation_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fee_matrix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_reference** | **str**|  | 

### Return type

[**FeeMatrixResponse**](FeeMatrixResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> str get_file(file_id)



See API specification Resource Guide > Works API > File upload for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
file_id = 56 # int | 

try:
    api_response = api_instance.get_file(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.msword, application/pdf, image/png, image/jpeg, image/tiff, image/bmp

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forward_plan**
> ForwardPlanResponse get_forward_plan(work_reference_number, forward_plan_reference_number)



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
work_reference_number = 'work_reference_number_example' # str | 
forward_plan_reference_number = 'forward_plan_reference_number_example' # str | 

try:
    api_response = api_instance.get_forward_plan(work_reference_number, forward_plan_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_forward_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **forward_plan_reference_number** | **str**|  | 

### Return type

[**ForwardPlanResponse**](ForwardPlanResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpn**
> FPNResponse get_fpn(work_reference_number, fpn_reference_number)



See business rules section 11 - Fixed penalty notice (FPN) Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
fpn_reference_number = 'fpn_reference_number_example' # str | 

try:
    api_response = api_instance.get_fpn(work_reference_number, fpn_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fpn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **fpn_reference_number** | **str**|  | 

### Return type

[**FPNResponse**](FPNResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspection**
> InspectionResponse get_inspection(work_reference_number, inspection_reference_number)



See business rules section 10 - Inspections and non-compliance Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
inspection_reference_number = 'inspection_reference_number_example' # str | 

try:
    api_response = api_instance.get_inspection(work_reference_number, inspection_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **inspection_reference_number** | **str**|  | 

### Return type

[**InspectionResponse**](InspectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_classification**
> MaterialClassificationResponse get_material_classification(material_classification_reference_number)



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
material_classification_reference_number = 'material_classification_reference_number_example' # str | 

try:
    api_response = api_instance.get_material_classification(material_classification_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_material_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_classification_reference_number** | **str**|  | 

### Return type

[**MaterialClassificationResponse**](MaterialClassificationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_compliance**
> NonComplianceResponse get_non_compliance(work_reference_number, non_compliance_reference_number)



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
work_reference_number = 'work_reference_number_example' # str | 
non_compliance_reference_number = 'non_compliance_reference_number_example' # str | 

try:
    api_response = api_instance.get_non_compliance(work_reference_number, non_compliance_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_non_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **non_compliance_reference_number** | **str**|  | 

### Return type

[**NonComplianceResponse**](NonComplianceResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit**
> PermitResponse get_permit(work_reference_number, permit_reference_number)



See business rules section 3.4 - PAA and permit applications (PA) Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_response = api_instance.get_permit(work_reference_number, permit_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

[**PermitResponse**](PermitResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_alteration**
> PermitAlterationResponse get_permit_alteration(work_reference_number, permit_reference_number, permit_alteration_reference_number)



See business rules section 4 - Change requests (CR) Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
permit_alteration_reference_number = 'permit_alteration_reference_number_example' # str | 

try:
    api_response = api_instance.get_permit_alteration(work_reference_number, permit_reference_number, permit_alteration_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit_alteration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **permit_alteration_reference_number** | **str**|  | 

### Return type

[**PermitAlterationResponse**](PermitAlterationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_street_notice**
> PrivateStreetNoticeResponse get_private_street_notice(work_reference_number, private_street_reference_number)



See business rules section 2.1.7 - Works on private streets Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
private_street_reference_number = 'private_street_reference_number_example' # str | 

try:
    api_response = api_instance.get_private_street_notice(work_reference_number, private_street_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_private_street_notice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **private_street_reference_number** | **str**|  | 

### Return type

[**PrivateStreetNoticeResponse**](PrivateStreetNoticeResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section58**
> Section58Response get_section58(section58_reference_number)



See business rules section 22 - Section 58s Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
section58_reference_number = 'section58_reference_number_example' # str | 

try:
    api_response = api_instance.get_section58(section58_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section58: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section58_reference_number** | **str**|  | 

### Return type

[**Section58Response**](Section58Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section74**
> Section74Response get_section74(work_reference_number, section74_reference_number)



See business rules section 20 - Section 74s Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
section74_reference_number = 'section74_reference_number_example' # str | 

try:
    api_response = api_instance.get_section74(work_reference_number, section74_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section74: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **section74_reference_number** | **str**|  | 

### Return type

[**Section74Response**](Section74Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section81**
> Section81Response get_section81(work_reference_number, section81_reference_number)



See business rules section 14 - Section 81 (S81) Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
section81_reference_number = 'section81_reference_number_example' # str | 

try:
    api_response = api_instance.get_section81(work_reference_number, section81_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section81: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **section81_reference_number** | **str**|  | 

### Return type

[**Section81Response**](Section81Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site**
> SiteResponse get_site(work_reference_number, site_reference_number)



See business rules section 8 - Sites and reinstatements Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
site_reference_number = 'site_reference_number_example' # str | 

try:
    api_response = api_instance.get_site(work_reference_number, site_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **site_reference_number** | **str**|  | 

### Return type

[**SiteResponse**](SiteResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work**
> WorkResponse get_work(work_reference_number)



See business rules section 3 - Works submissions and applications Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.get_work(work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_work: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 

### Return type

[**WorkResponse**](WorkResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_category**
> WorkCategoryResponse get_work_category(work_type, proposed_start_date=proposed_start_date, proposed_end_date=proposed_end_date, is_ttro_required=is_ttro_required, immediate_risk=immediate_risk, work_reference_number=work_reference_number, activity_type=activity_type)



See business rules section 3.4.3 - Works categories Utility endpoint. Can be used to check what category will be assigned to a permit Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_type = swagger_client.WorkType() # WorkType | 
proposed_start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
proposed_end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
is_ttro_required = true # bool |  (optional)
immediate_risk = true # bool |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
activity_type = swagger_client.ActivityType() # ActivityType |  (optional)

try:
    api_response = api_instance.get_work_category(work_type, proposed_start_date=proposed_start_date, proposed_end_date=proposed_end_date, is_ttro_required=is_ttro_required, immediate_risk=immediate_risk, work_reference_number=work_reference_number, activity_type=activity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_work_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_type** | [**WorkType**](.md)|  | 
 **proposed_start_date** | **datetime**|  | [optional] 
 **proposed_end_date** | **datetime**|  | [optional] 
 **is_ttro_required** | **bool**|  | [optional] 
 **immediate_risk** | **bool**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **activity_type** | [**ActivityType**](.md)|  | [optional] 

### Return type

[**WorkCategoryResponse**](WorkCategoryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_history**
> WorkHistoryResponse get_work_history(work_reference_number, offset=offset)



See business rules section 7.2 - Works history Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
work_reference_number = 'work_reference_number_example' # str | 
offset = 1.2 # float |  (optional)

try:
    api_response = api_instance.get_work_history(work_reference_number, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_work_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **offset** | **float**|  | [optional] 

### Return type

[**WorkHistoryResponse**](WorkHistoryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **impose_change**
> ImposeChangeResponse impose_change(body, work_reference_number, permit_reference_number)



See business rules section 4 - Change requests (CR) Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.ImposeChangeRequest() # ImposeChangeRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_response = api_instance.impose_change(body, work_reference_number, permit_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->impose_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImposeChangeRequest**](ImposeChangeRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

[**ImposeChangeResponse**](ImposeChangeResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_permit_to_non_compliance**
> link_permit_to_non_compliance(body, work_reference_number, permit_reference_number)



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
body = swagger_client.PermitNonComplianceLinkRequest() # PermitNonComplianceLinkRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.link_permit_to_non_compliance(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->link_permit_to_non_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitNonComplianceLinkRequest**](PermitNonComplianceLinkRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_section81_to_permit**
> LinkSection81ToPermitResponse link_section81_to_permit(body, work_reference_number, permit_reference_number)



Creates a link between a Permit and a Section 81 Authenticated user must have one of the following roles: Planner, Contractor The Permit and Section 81 must both exist already, not have any existing links created, and the authenticated user must have write access to the associated workstreams for both.

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
body = swagger_client.LinkSection81ToPermitRequest() # LinkSection81ToPermitRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_response = api_instance.link_section81_to_permit(body, work_reference_number, permit_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->link_section81_to_permit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LinkSection81ToPermitRequest**](LinkSection81ToPermitRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

[**LinkSection81ToPermitResponse**](LinkSection81ToPermitResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_comment_as_read**
> mark_comment_as_read(body, work_reference_number, comment_reference_number)



See business rules section 7.1 - Commenting on a works record Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.CommentReadRequest() # CommentReadRequest | 
work_reference_number = 'work_reference_number_example' # str | 
comment_reference_number = 'comment_reference_number_example' # str | 

try:
    api_instance.mark_comment_as_read(body, work_reference_number, comment_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->mark_comment_as_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentReadRequest**](CommentReadRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **comment_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_permit_as_under_assessment**
> mark_permit_as_under_assessment(work_reference_number, permit_reference_number, body=body)



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
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
body = swagger_client.MarkPermitAsUnderAssessmentRequest() # MarkPermitAsUnderAssessmentRequest |  (optional)

try:
    api_instance.mark_permit_as_under_assessment(work_reference_number, permit_reference_number, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->mark_permit_as_under_assessment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **body** | [**MarkPermitAsUnderAssessmentRequest**](MarkPermitAsUnderAssessmentRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment**
> CommentCreateResponse post_comment(body, work_reference_number)



See business rules section 7.1 - Commenting on a works record Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.CommentCreateRequest() # CommentCreateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_response = api_instance.post_comment(body, work_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentCreateRequest**](CommentCreateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

[**CommentCreateResponse**](CommentCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reassign_section81**
> reassign_section81(body, work_reference_number, section81_reference_number)



See business rules section 14 - Section 81 Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.ReassignSection81Request() # ReassignSection81Request | 
work_reference_number = 'work_reference_number_example' # str | 
section81_reference_number = 'section81_reference_number_example' # str | 

try:
    api_instance.reassign_section81(body, work_reference_number, section81_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->reassign_section81: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReassignSection81Request**](ReassignSection81Request.md)|  | 
 **work_reference_number** | **str**|  | 
 **section81_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_ancillary_info**
> RemoveAncillaryInfoResponse remove_ancillary_info(body, work_reference_number, permit_reference_number, ancillary_information_reference_number)



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
body = swagger_client.RemoveAncillaryInfoRequest() # RemoveAncillaryInfoRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
ancillary_information_reference_number = 'ancillary_information_reference_number_example' # str | 

try:
    api_response = api_instance.remove_ancillary_info(body, work_reference_number, permit_reference_number, ancillary_information_reference_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->remove_ancillary_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveAncillaryInfoRequest**](RemoveAncillaryInfoRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **ancillary_information_reference_number** | **str**|  | 

### Return type

[**RemoveAncillaryInfoResponse**](RemoveAncillaryInfoResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_actual_start_date**
> revert_actual_start_date(body, work_reference_number)



See business rules section 6.2 - Reverting works start Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.WorkStartRevertRequest() # WorkStartRevertRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.revert_actual_start_date(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->revert_actual_start_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkStartRevertRequest**](WorkStartRevertRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_actual_stop_date**
> revert_actual_stop_date(body, work_reference_number)



See business rules section 6.4 - Reverting works stop Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.WorkStopRevertRequest() # WorkStopRevertRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.revert_actual_stop_date(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->revert_actual_stop_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkStopRevertRequest**](WorkStopRevertRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsume_site**
> subsume_site(body, work_reference_number, site_reference_number)



See business rules section 8 - Sites and reinstatements Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.SubsumeSiteRequest() # SubsumeSiteRequest | 
work_reference_number = 'work_reference_number_example' # str | 
site_reference_number = 'site_reference_number_example' # str | 

try:
    api_instance.subsume_site(body, work_reference_number, site_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->subsume_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubsumeSiteRequest**](SubsumeSiteRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **site_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_section81_from_permit**
> unlink_section81_from_permit(body, work_reference_number, permit_reference_number)



Removes a link between a Permit and a Section 81 Authenticated user must have one of the following roles: Planner, Contractor The Permit and Section 81 must both exist already, have a link created between them, and the authenticated user must have write access to the associated workstreams for both.

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
body = swagger_client.UnlinkSection81FromPermitRequest() # UnlinkSection81FromPermitRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.unlink_section81_from_permit(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->unlink_section81_from_permit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnlinkSection81FromPermitRequest**](UnlinkSection81FromPermitRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity**
> update_activity(body, activity_reference_number)



Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.ActivityUpdateRequest() # ActivityUpdateRequest | 
activity_reference_number = 'activity_reference_number_example' # str | 

try:
    api_instance.update_activity(body, activity_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityUpdateRequest**](ActivityUpdateRequest.md)|  | 
 **activity_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_actual_start_date**
> update_actual_start_date(body, work_reference_number)



See business rules section 6.1 - Logging works start Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.WorkStartUpdateRequest() # WorkStartUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.update_actual_start_date(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_actual_start_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkStartUpdateRequest**](WorkStartUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_actual_stop_date**
> update_actual_stop_date(body, work_reference_number)



See business rules section 6.3 - Logging works stop Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.WorkStopUpdateRequest() # WorkStopUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.update_actual_stop_date(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_actual_stop_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkStopUpdateRequest**](WorkStopUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assessment_status**
> update_assessment_status(body, work_reference_number, permit_reference_number)



See business rule section 5 - Revoking a PA See business rule section 3.4.7 - PAA & PA assessment decision options Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.PermitAssessmentUpdateRequest() # PermitAssessmentUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_assessment_status(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_assessment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitAssessmentUpdateRequest**](PermitAssessmentUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_traffic_management_type**
> update_current_traffic_management_type(body, work_reference_number, permit_reference_number)



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
body = swagger_client.CurrentTrafficManagementTypeRequest() # CurrentTrafficManagementTypeRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_current_traffic_management_type(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_current_traffic_management_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CurrentTrafficManagementTypeRequest**](CurrentTrafficManagementTypeRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_excavation_carried_out**
> update_excavation_carried_out(body, work_reference_number)



Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.ExcavationCarriedOutUpdateRequest() # ExcavationCarriedOutUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.update_excavation_carried_out(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_excavation_carried_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExcavationCarriedOutUpdateRequest**](ExcavationCarriedOutUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_final_reinstatement**
> update_final_reinstatement(body, work_reference_number)



See business rules section 8.3 - Adding reinstatements

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
body = swagger_client.FinalReinstatementUpdateRequest() # FinalReinstatementUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 

try:
    api_instance.update_final_reinstatement(body, work_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_final_reinstatement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FinalReinstatementUpdateRequest**](FinalReinstatementUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_forward_plan**
> update_forward_plan(body, work_reference_number, forward_plan_reference_number)



See business rules section 3.3 - Forward plans Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.ForwardPlanUpdateRequest() # ForwardPlanUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
forward_plan_reference_number = 'forward_plan_reference_number_example' # str | 

try:
    api_instance.update_forward_plan(body, work_reference_number, forward_plan_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_forward_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForwardPlanUpdateRequest**](ForwardPlanUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **forward_plan_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fpn_status**
> update_fpn_status(body, work_reference_number, fpn_reference_number)



See business rules section 11.2 - FPN statuses Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.FPNStatusUpdateRequest() # FPNStatusUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
fpn_reference_number = 'fpn_reference_number_example' # str | 

try:
    api_instance.update_fpn_status(body, work_reference_number, fpn_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_fpn_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FPNStatusUpdateRequest**](FPNStatusUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **fpn_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_geographical_area**
> update_geographical_area(file, geographical_area_reference_number2, internal_user_identifier, internal_user_name, geographical_area_reference_number)



See API specification Resource Guide > Works API > Geographical Areas for more information Authenticated user must have one of the following roles: HighwayAuthority, Admin

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
file = 'file_example' # str | 
geographical_area_reference_number2 = 'geographical_area_reference_number_example' # str | 
internal_user_identifier = 'internal_user_identifier_example' # str | 
internal_user_name = 'internal_user_name_example' # str | 
geographical_area_reference_number = 'geographical_area_reference_number_example' # str | 

try:
    api_instance.update_geographical_area(file, geographical_area_reference_number2, internal_user_identifier, internal_user_name, geographical_area_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_geographical_area: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **geographical_area_reference_number2** | **str**|  | 
 **internal_user_identifier** | **str**|  | 
 **internal_user_name** | **str**|  | 
 **geographical_area_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inspection_outcome_status**
> update_inspection_outcome_status(body, work_reference_number, inspection_reference_number)



See business rules section 10 - Inspections and non-compliance Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.InspectionOutcomeStatusRequest() # InspectionOutcomeStatusRequest | 
work_reference_number = 'work_reference_number_example' # str | 
inspection_reference_number = 'inspection_reference_number_example' # str | 

try:
    api_instance.update_inspection_outcome_status(body, work_reference_number, inspection_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_inspection_outcome_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InspectionOutcomeStatusRequest**](InspectionOutcomeStatusRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **inspection_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_non_compliance_status**
> update_non_compliance_status(body, work_reference_number, non_compliance_reference_number)



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
body = swagger_client.NonComplianceResponseStatusRequest() # NonComplianceResponseStatusRequest | 
work_reference_number = 'work_reference_number_example' # str | 
non_compliance_reference_number = 'non_compliance_reference_number_example' # str | 

try:
    api_instance.update_non_compliance_status(body, work_reference_number, non_compliance_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_non_compliance_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NonComplianceResponseStatusRequest**](NonComplianceResponseStatusRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **non_compliance_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permit_alteration_status**
> update_permit_alteration_status(body, work_reference_number, permit_reference_number, permit_alteration_reference_number)



See business rules section 4.7 - Change request statuses Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.PermitAlterationStatusUpdateRequest() # PermitAlterationStatusUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 
permit_alteration_reference_number = 'permit_alteration_reference_number_example' # str | 

try:
    api_instance.update_permit_alteration_status(body, work_reference_number, permit_reference_number, permit_alteration_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_permit_alteration_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitAlterationStatusUpdateRequest**](PermitAlterationStatusUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 
 **permit_alteration_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permit_discount**
> update_permit_discount(body, work_reference_number, permit_reference_number)



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
body = swagger_client.PermitDiscountUpdateRequest() # PermitDiscountUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_permit_discount(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_permit_discount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitDiscountUpdateRequest**](PermitDiscountUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permit_duration_challenge_non_acceptance_response**
> update_permit_duration_challenge_non_acceptance_response(body, work_reference_number, permit_reference_number)



See business rules section 21.1 - Duration challenge review Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.PermitDurationChallengeNonAcceptanceResponseRequest() # PermitDurationChallengeNonAcceptanceResponseRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_permit_duration_challenge_non_acceptance_response(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_permit_duration_challenge_non_acceptance_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitDurationChallengeNonAcceptanceResponseRequest**](PermitDurationChallengeNonAcceptanceResponseRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permit_duration_challenge_review**
> update_permit_duration_challenge_review(body, work_reference_number, permit_reference_number)



See business rules section 21.1 - Duration challenge review Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.PermitDurationChallengeReviewRequest() # PermitDurationChallengeReviewRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_permit_duration_challenge_review(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_permit_duration_challenge_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitDurationChallengeReviewRequest**](PermitDurationChallengeReviewRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permit_lane_rental_assessment**
> update_permit_lane_rental_assessment(body, work_reference_number, permit_reference_number)



See business rule section 12.2 - Adding a lane rental assessment to a PA Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.PermitLaneRentalAssessmentUpdateRequest() # PermitLaneRentalAssessmentUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_permit_lane_rental_assessment(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_permit_lane_rental_assessment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitLaneRentalAssessmentUpdateRequest**](PermitLaneRentalAssessmentUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permit_status**
> update_permit_status(body, work_reference_number, permit_reference_number)



See business rules section 3.4.9 - Cancelling PAA & PA Authenticated user must have one of the following roles: Planner, Contractor

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
body = swagger_client.PermitStatusUpdateRequest() # PermitStatusUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
permit_reference_number = 'permit_reference_number_example' # str | 

try:
    api_instance.update_permit_status(body, work_reference_number, permit_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_permit_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermitStatusUpdateRequest**](PermitStatusUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **permit_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section58_status**
> update_section58_status(body, section58_reference_number)



See business rules section 22 - Section 58s Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.Section58UpdateStatusRequest() # Section58UpdateStatusRequest | 
section58_reference_number = 'section58_reference_number_example' # str | 

try:
    api_instance.update_section58_status(body, section58_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_section58_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section58UpdateStatusRequest**](Section58UpdateStatusRequest.md)|  | 
 **section58_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section74_ha_status**
> update_section74_ha_status(body, work_reference_number, section74_reference_number)



See business rules section 20 - Section 74s Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.Section74UpdateHAStatusRequest() # Section74UpdateHAStatusRequest | 
work_reference_number = 'work_reference_number_example' # str | 
section74_reference_number = 'section74_reference_number_example' # str | 

try:
    api_instance.update_section74_ha_status(body, work_reference_number, section74_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_section74_ha_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section74UpdateHAStatusRequest**](Section74UpdateHAStatusRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **section74_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section74_promoter_status**
> update_section74_promoter_status(body, work_reference_number, section74_reference_number)



See business rules section 20 - Section 74s Authenticated user must have one of the following roles: Planner or Contractor

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
body = swagger_client.Section74UpdatePromoterStatusRequest() # Section74UpdatePromoterStatusRequest | 
work_reference_number = 'work_reference_number_example' # str | 
section74_reference_number = 'section74_reference_number_example' # str | 

try:
    api_instance.update_section74_promoter_status(body, work_reference_number, section74_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_section74_promoter_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section74UpdatePromoterStatusRequest**](Section74UpdatePromoterStatusRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **section74_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section81_status**
> update_section81_status(body, work_reference_number, section81_reference_number)



See business rules section 14.5 - S81 statuses Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
body = swagger_client.Section81StatusUpdateRequest() # Section81StatusUpdateRequest | 
work_reference_number = 'work_reference_number_example' # str | 
section81_reference_number = 'section81_reference_number_example' # str | 

try:
    api_instance.update_section81_status(body, work_reference_number, section81_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->update_section81_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Section81StatusUpdateRequest**](Section81StatusUpdateRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **section81_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FileSummaryResponse upload_file(file, swa_code=swa_code)



See API specification Resource Guide > Works API > File upload for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
file = 'file_example' # str | 
swa_code = 'swa_code_example' # str |  (optional)

try:
    api_response = api_instance.upload_file(file, swa_code=swa_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **swa_code** | **str**|  | [optional] 

### Return type

[**FileSummaryResponse**](FileSummaryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_inspection**
> withdraw_inspection(body, work_reference_number, inspection_reference_number)



See business rules section 10 - Inspections and non-compliance Authenticated user must have one of the following roles: HighwayAuthority

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
body = swagger_client.InspectionWithdrawRequest() # InspectionWithdrawRequest | 
work_reference_number = 'work_reference_number_example' # str | 
inspection_reference_number = 'inspection_reference_number_example' # str | 

try:
    api_instance.withdraw_inspection(body, work_reference_number, inspection_reference_number)
except ApiException as e:
    print("Exception when calling DefaultApi->withdraw_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InspectionWithdrawRequest**](InspectionWithdrawRequest.md)|  | 
 **work_reference_number** | **str**|  | 
 **inspection_reference_number** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

