# swagger_client.DefaultApi

All URIs are relative to *https://department-for-transport-streetmanager.github.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activities**](DefaultApi.md#get_activities) | **GET** /activities | 
[**get_alteration_duration_challenges**](DefaultApi.md#get_alteration_duration_challenges) | **GET** /alterations/duration-challenges | 
[**get_alterations**](DefaultApi.md#get_alterations) | **GET** /alterations | 
[**get_comments**](DefaultApi.md#get_comments) | **GET** /comments | 
[**get_csv_exports**](DefaultApi.md#get_csv_exports) | **GET** /csv-exports | 
[**get_expiring_interim_reinstatements**](DefaultApi.md#get_expiring_interim_reinstatements) | **GET** /reinstatements/expiring-interims | 
[**get_forward_plans**](DefaultApi.md#get_forward_plans) | **GET** /forward-plans | 
[**get_fpn_files**](DefaultApi.md#get_fpn_files) | **GET** /fixed-penalty-notices/files | 
[**get_fpns**](DefaultApi.md#get_fpns) | **GET** /fixed-penalty-notices | 
[**get_geographical_areas**](DefaultApi.md#get_geographical_areas) | **GET** /geographical-areas | 
[**get_inspection_files**](DefaultApi.md#get_inspection_files) | **GET** /inspections/files | 
[**get_inspections**](DefaultApi.md#get_inspections) | **GET** /inspections | 
[**get_interested_party_permits**](DefaultApi.md#get_interested_party_permits) | **GET** /interested-party-permits | 
[**get_material_classifications**](DefaultApi.md#get_material_classifications) | **GET** /material-classifications | 
[**get_non_compliances**](DefaultApi.md#get_non_compliances) | **GET** /non-compliances | 
[**get_pbi_sample_generation_jobs**](DefaultApi.md#get_pbi_sample_generation_jobs) | **GET** /pbi-sample-generation-jobs | 
[**get_pbi_sample_inspection_targets**](DefaultApi.md#get_pbi_sample_inspection_targets) | **GET** /pbi-sample-inspection-targets | 
[**get_pbi_sample_inspections**](DefaultApi.md#get_pbi_sample_inspections) | **GET** /pbi-sample-inspections | 
[**get_permit_duration_challenges**](DefaultApi.md#get_permit_duration_challenges) | **GET** /permits/duration-challenges | 
[**get_permit_files**](DefaultApi.md#get_permit_files) | **GET** /permits/files | 
[**get_permits**](DefaultApi.md#get_permits) | **GET** /permits | 
[**get_private_street_files**](DefaultApi.md#get_private_street_files) | **GET** /private-street-notices/files | 
[**get_private_streets**](DefaultApi.md#get_private_streets) | **GET** /private-street-notices | 
[**get_reinspections**](DefaultApi.md#get_reinspections) | **GET** /reinspections | 
[**get_reinstatement_files**](DefaultApi.md#get_reinstatement_files) | **GET** /reinstatements/files | 
[**get_reinstatements**](DefaultApi.md#get_reinstatements) | **GET** /reinstatements | 
[**get_reinstatements_due**](DefaultApi.md#get_reinstatements_due) | **GET** /permits/reinstatements-due | 
[**get_section58s**](DefaultApi.md#get_section58s) | **GET** /section-58s | 
[**get_section74_files**](DefaultApi.md#get_section74_files) | **GET** /section-74s/files | 
[**get_section74s**](DefaultApi.md#get_section74s) | **GET** /section-74s | 
[**get_section81_files**](DefaultApi.md#get_section81_files) | **GET** /section-81s/files | 
[**get_section81s**](DefaultApi.md#get_section81s) | **GET** /section-81s | 
[**get_work_files**](DefaultApi.md#get_work_files) | **GET** /works/files | 
[**get_works**](DefaultApi.md#get_works) | **GET** /works | 
[**get_workstreams**](DefaultApi.md#get_workstreams) | **GET** /workstreams | 

# **get_activities**
> ActivityReportingResponse get_activities(ha_organisation_name=ha_organisation_name, activity_activity_type=activity_activity_type, offset=offset, query=query, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Activities for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
ha_organisation_name = 'ha_organisation_name_example' # str |  (optional)
activity_activity_type = [swagger_client.ActivityActivityType()] # list[ActivityActivityType] |  (optional)
offset = 1.2 # float |  (optional)
query = 'query_example' # str |  (optional)
sort_column = swagger_client.ActivitySortColumn() # ActivitySortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_activities(ha_organisation_name=ha_organisation_name, activity_activity_type=activity_activity_type, offset=offset, query=query, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ha_organisation_name** | **str**|  | [optional] 
 **activity_activity_type** | [**list[ActivityActivityType]**](ActivityActivityType.md)|  | [optional] 
 **offset** | **float**|  | [optional] 
 **query** | **str**|  | [optional] 
 **sort_column** | [**ActivitySortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**ActivityReportingResponse**](ActivityReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alteration_duration_challenges**
> AlterationDurationChallengeReportingResponse get_alteration_duration_challenges(offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, organisation=organisation, geographical_area_reference_number=geographical_area_reference_number, duration_challenge_review_status=duration_challenge_review_status, duration_challenge_non_acceptance_response_status=duration_challenge_non_acceptance_response_status, work_status=work_status, street_descriptor=street_descriptor, usrn=usrn, permit_alteration_reference_number=permit_alteration_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Permit Alteration Duration Challenges for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
offset = 1.2 # float |  (optional)
sort_column = swagger_client.AlterationDurationChallengeSortColumn() # AlterationDurationChallengeSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
organisation = 'organisation_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
duration_challenge_review_status = [swagger_client.DurationChallengeReviewStatus()] # list[DurationChallengeReviewStatus] |  (optional)
duration_challenge_non_acceptance_response_status = [swagger_client.DurationChallengeNonAcceptanceResponseStatus()] # list[DurationChallengeNonAcceptanceResponseStatus] |  (optional)
work_status = [swagger_client.WorkStatus()] # list[WorkStatus] |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
permit_alteration_reference_number = 'permit_alteration_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_alteration_duration_challenges(offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, organisation=organisation, geographical_area_reference_number=geographical_area_reference_number, duration_challenge_review_status=duration_challenge_review_status, duration_challenge_non_acceptance_response_status=duration_challenge_non_acceptance_response_status, work_status=work_status, street_descriptor=street_descriptor, usrn=usrn, permit_alteration_reference_number=permit_alteration_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alteration_duration_challenges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **sort_column** | [**AlterationDurationChallengeSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **duration_challenge_review_status** | [**list[DurationChallengeReviewStatus]**](DurationChallengeReviewStatus.md)|  | [optional] 
 **duration_challenge_non_acceptance_response_status** | [**list[DurationChallengeNonAcceptanceResponseStatus]**](DurationChallengeNonAcceptanceResponseStatus.md)|  | [optional] 
 **work_status** | [**list[WorkStatus]**](WorkStatus.md)|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **permit_alteration_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**AlterationDurationChallengeReportingResponse**](AlterationDurationChallengeReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alterations**
> AlterationReportingResponse get_alterations(alteration_status=alteration_status, alteration_type=alteration_type, work_status=work_status, work_category=work_category, lane_rental_assessment_outcome=lane_rental_assessment_outcome, start_date_created=start_date_created, end_date_created=end_date_created, offset=offset, sort_column=sort_column, sort_direction=sort_direction, is_traffic_sensitive=is_traffic_sensitive, is_high_impact_traffic_management=is_high_impact_traffic_management, is_duration_extension=is_duration_extension, is_early_start=is_early_start, is_deemed=is_deemed, lane_rental_charges_not_agreed=lane_rental_charges_not_agreed, lane_rental_charges_potentially_apply=lane_rental_charges_potentially_apply, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, status_update_date_from=status_update_date_from, status_update_date_to=status_update_date_to, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, permit_alteration_reference_number=permit_alteration_reference_number, include_total_count=include_total_count)



Returns all alterations associated with the logged in user's organisation. Optional date range filter for date_created Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
alteration_status = [swagger_client.AlterationStatus()] # list[AlterationStatus] |  (optional)
alteration_type = [swagger_client.AlterationType()] # list[AlterationType] |  (optional)
work_status = [swagger_client.WorkStatus()] # list[WorkStatus] |  (optional)
work_category = [swagger_client.WorkCategory()] # list[WorkCategory] |  (optional)
lane_rental_assessment_outcome = [swagger_client.LaneRentalAssessmentOutcome()] # list[LaneRentalAssessmentOutcome] |  (optional)
start_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.AlterationSortColumn() # AlterationSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
is_traffic_sensitive = true # bool |  (optional)
is_high_impact_traffic_management = true # bool |  (optional)
is_duration_extension = true # bool |  (optional)
is_early_start = true # bool |  (optional)
is_deemed = true # bool |  (optional)
lane_rental_charges_not_agreed = true # bool |  (optional)
lane_rental_charges_potentially_apply = true # bool |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
status_update_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
status_update_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
permit_alteration_reference_number = 'permit_alteration_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_alterations(alteration_status=alteration_status, alteration_type=alteration_type, work_status=work_status, work_category=work_category, lane_rental_assessment_outcome=lane_rental_assessment_outcome, start_date_created=start_date_created, end_date_created=end_date_created, offset=offset, sort_column=sort_column, sort_direction=sort_direction, is_traffic_sensitive=is_traffic_sensitive, is_high_impact_traffic_management=is_high_impact_traffic_management, is_duration_extension=is_duration_extension, is_early_start=is_early_start, is_deemed=is_deemed, lane_rental_charges_not_agreed=lane_rental_charges_not_agreed, lane_rental_charges_potentially_apply=lane_rental_charges_potentially_apply, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, status_update_date_from=status_update_date_from, status_update_date_to=status_update_date_to, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, permit_alteration_reference_number=permit_alteration_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alterations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alteration_status** | [**list[AlterationStatus]**](AlterationStatus.md)|  | [optional] 
 **alteration_type** | [**list[AlterationType]**](AlterationType.md)|  | [optional] 
 **work_status** | [**list[WorkStatus]**](WorkStatus.md)|  | [optional] 
 **work_category** | [**list[WorkCategory]**](WorkCategory.md)|  | [optional] 
 **lane_rental_assessment_outcome** | [**list[LaneRentalAssessmentOutcome]**](LaneRentalAssessmentOutcome.md)|  | [optional] 
 **start_date_created** | **datetime**|  | [optional] 
 **end_date_created** | **datetime**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**AlterationSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **is_traffic_sensitive** | **bool**|  | [optional] 
 **is_high_impact_traffic_management** | **bool**|  | [optional] 
 **is_duration_extension** | **bool**|  | [optional] 
 **is_early_start** | **bool**|  | [optional] 
 **is_deemed** | **bool**|  | [optional] 
 **lane_rental_charges_not_agreed** | **bool**|  | [optional] 
 **lane_rental_charges_potentially_apply** | **bool**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **status_update_date_from** | **datetime**|  | [optional] 
 **status_update_date_to** | **datetime**|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **permit_alteration_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**AlterationReportingResponse**](AlterationReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> CommentReportingResponse get_comments(offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, date_created_from=date_created_from, date_created_to=date_created_to, topic=topic, is_internal=is_internal, is_read=is_read, is_not_read=is_not_read, work_reference_number=work_reference_number, author_email_address=author_email_address, is_incoming=is_incoming, is_outgoing=is_outgoing, include_total_count=include_total_count)



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
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
date_created_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_created_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
topic = [swagger_client.CommentTopic()] # list[CommentTopic] |  (optional)
is_internal = true # bool |  (optional)
is_read = true # bool |  (optional)
is_not_read = true # bool |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
author_email_address = 'author_email_address_example' # str |  (optional)
is_incoming = true # bool |  (optional)
is_outgoing = true # bool |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_comments(offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, date_created_from=date_created_from, date_created_to=date_created_to, topic=topic, is_internal=is_internal, is_read=is_read, is_not_read=is_not_read, work_reference_number=work_reference_number, author_email_address=author_email_address, is_incoming=is_incoming, is_outgoing=is_outgoing, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **date_created_from** | **datetime**|  | [optional] 
 **date_created_to** | **datetime**|  | [optional] 
 **topic** | [**list[CommentTopic]**](CommentTopic.md)|  | [optional] 
 **is_internal** | **bool**|  | [optional] 
 **is_read** | **bool**|  | [optional] 
 **is_not_read** | **bool**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **author_email_address** | **str**|  | [optional] 
 **is_incoming** | **bool**|  | [optional] 
 **is_outgoing** | **bool**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**CommentReportingResponse**](CommentReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csv_exports**
> CSVExportReportingResponse get_csv_exports(offset=offset, swa_code=swa_code, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get CSV Exports for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority, Admin

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
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_csv_exports(offset=offset, swa_code=swa_code, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_csv_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**CSVExportReportingResponse**](CSVExportReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expiring_interim_reinstatements**
> ReinstatementReportingResponse get_expiring_interim_reinstatements(sort_column=sort_column, sort_direction=sort_direction, offset=offset, swa_code=swa_code, registration_date_from=registration_date_from, registration_date_to=registration_date_to, end_date_from=end_date_from, end_date_to=end_date_to, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, work_reference_number_exact=work_reference_number_exact, include_total_count=include_total_count)



Returns expiring interim associated with the logged in user's organisation. Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
sort_column = swagger_client.ReinstatementSortColumn() # ReinstatementSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
registration_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
registration_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
work_reference_number_exact = 'work_reference_number_exact_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_expiring_interim_reinstatements(sort_column=sort_column, sort_direction=sort_direction, offset=offset, swa_code=swa_code, registration_date_from=registration_date_from, registration_date_to=registration_date_to, end_date_from=end_date_from, end_date_to=end_date_to, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, work_reference_number_exact=work_reference_number_exact, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_expiring_interim_reinstatements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_column** | [**ReinstatementSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **registration_date_from** | **datetime**|  | [optional] 
 **registration_date_to** | **datetime**|  | [optional] 
 **end_date_from** | **datetime**|  | [optional] 
 **end_date_to** | **datetime**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **work_reference_number_exact** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**ReinstatementReportingResponse**](ReinstatementReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forward_plans**
> ForwardPlanReportingResponse get_forward_plans(forward_plan_status=forward_plan_status, proposed_start_date=proposed_start_date, proposed_end_date=proposed_end_date, work_start_date_from=work_start_date_from, work_start_date_to=work_start_date_to, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, forward_plan_reference_number=forward_plan_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get ForwardPlans for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
forward_plan_status = [swagger_client.ForwardPlanStatus()] # list[ForwardPlanStatus] |  (optional)
proposed_start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
proposed_end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_start_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_start_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.ForwardPlanSortColumn() # ForwardPlanSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
forward_plan_reference_number = 'forward_plan_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_forward_plans(forward_plan_status=forward_plan_status, proposed_start_date=proposed_start_date, proposed_end_date=proposed_end_date, work_start_date_from=work_start_date_from, work_start_date_to=work_start_date_to, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, forward_plan_reference_number=forward_plan_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_forward_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_plan_status** | [**list[ForwardPlanStatus]**](ForwardPlanStatus.md)|  | [optional] 
 **proposed_start_date** | **datetime**|  | [optional] 
 **proposed_end_date** | **datetime**|  | [optional] 
 **work_start_date_from** | **datetime**|  | [optional] 
 **work_start_date_to** | **datetime**|  | [optional] 
 **work_end_date_from** | **datetime**|  | [optional] 
 **work_end_date_to** | **datetime**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**ForwardPlanSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **forward_plan_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**ForwardPlanReportingResponse**](ForwardPlanReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpn_files**
> FileSummaryReportingResponse get_fpn_files(fpn_reference_number, file_type=file_type)



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
fpn_reference_number = 'fpn_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_fpn_files(fpn_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fpn_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fpn_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpns**
> FPNReportingResponse get_fpns(status=status, start_date=start_date, end_date=end_date, offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, offence_code=offence_code, status_changed_date_from=status_changed_date_from, status_changed_date_to=status_changed_date_to, sort_column=sort_column, sort_direction=sort_direction, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get FPNs for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
status = [swagger_client.FPNStatus()] # list[FPNStatus] |  (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
offence_code = [swagger_client.OffenceCode()] # list[OffenceCode] |  (optional)
status_changed_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
status_changed_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sort_column = swagger_client.FPNSortColumn() # FPNSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_fpns(status=status, start_date=start_date, end_date=end_date, offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, offence_code=offence_code, status_changed_date_from=status_changed_date_from, status_changed_date_to=status_changed_date_to, sort_column=sort_column, sort_direction=sort_direction, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fpns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[FPNStatus]**](FPNStatus.md)|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **offence_code** | [**list[OffenceCode]**](OffenceCode.md)|  | [optional] 
 **status_changed_date_from** | **datetime**|  | [optional] 
 **status_changed_date_to** | **datetime**|  | [optional] 
 **sort_column** | [**FPNSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**FPNReportingResponse**](FPNReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_geographical_areas**
> list[GeographicalAreaResponse] get_geographical_areas()



Returns all geographic areas associated with the logged in user's organisation Authenticated user must have one of the following roles: Admin, HighwayAuthority

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
    api_response = api_instance.get_geographical_areas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_geographical_areas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GeographicalAreaResponse]**](GeographicalAreaResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspection_files**
> FileSummaryReportingResponse get_inspection_files(inspection_reference_number, file_type=file_type)



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
inspection_reference_number = 'inspection_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_inspection_files(inspection_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_inspection_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspections**
> InspectionReportingResponse get_inspections(start_date=start_date, end_date=end_date, inspection_type=inspection_type, inspection_outcome=inspection_outcome, start_date_created=start_date_created, end_date_created=end_date_created, offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, inspection_category=inspection_category, promoter_outcome_status=promoter_outcome_status, ha_outcome_status=ha_outcome_status, is_auto_accepted=is_auto_accepted, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get inspections for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
inspection_type = [swagger_client.InspectionType()] # list[InspectionType] |  (optional)
inspection_outcome = [swagger_client.InspectionOutcome()] # list[InspectionOutcome] |  (optional)
start_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.InspectionSortColumn() # InspectionSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
inspection_category = [swagger_client.InspectionCategory()] # list[InspectionCategory] |  (optional)
promoter_outcome_status = [swagger_client.PromoterInspectionOutcomeStatusType()] # list[PromoterInspectionOutcomeStatusType] |  (optional)
ha_outcome_status = [swagger_client.HAInspectionOutcomeStatusType()] # list[HAInspectionOutcomeStatusType] |  (optional)
is_auto_accepted = true # bool |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_inspections(start_date=start_date, end_date=end_date, inspection_type=inspection_type, inspection_outcome=inspection_outcome, start_date_created=start_date_created, end_date_created=end_date_created, offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, inspection_category=inspection_category, promoter_outcome_status=promoter_outcome_status, ha_outcome_status=ha_outcome_status, is_auto_accepted=is_auto_accepted, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_inspections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **inspection_type** | [**list[InspectionType]**](InspectionType.md)|  | [optional] 
 **inspection_outcome** | [**list[InspectionOutcome]**](InspectionOutcome.md)|  | [optional] 
 **start_date_created** | **datetime**|  | [optional] 
 **end_date_created** | **datetime**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**InspectionSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **inspection_category** | [**list[InspectionCategory]**](InspectionCategory.md)|  | [optional] 
 **promoter_outcome_status** | [**list[PromoterInspectionOutcomeStatusType]**](PromoterInspectionOutcomeStatusType.md)|  | [optional] 
 **ha_outcome_status** | [**list[HAInspectionOutcomeStatusType]**](HAInspectionOutcomeStatusType.md)|  | [optional] 
 **is_auto_accepted** | **bool**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**InspectionReportingResponse**](InspectionReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interested_party_permits**
> PermitReportingResponse get_interested_party_permits(offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, street_descriptor=street_descriptor, permit_reference_number=permit_reference_number, work_reference_number=work_reference_number, work_start_date_from=work_start_date_from, work_start_date_to=work_start_date_to, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, start_date_created=start_date_created, end_date_created=end_date_created, work_status=work_status, work_category=work_category, is_high_impact_traffic_management=is_high_impact_traffic_management, usrn=usrn, promoter_organisation_name=promoter_organisation_name, ha_organisation_name=ha_organisation_name, include_total_count=include_total_count)



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
offset = 1.2 # float |  (optional)
sort_column = swagger_client.PermitSortColumn() # PermitSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
permit_reference_number = 'permit_reference_number_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
work_start_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_start_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_status = [swagger_client.WorkStatus()] # list[WorkStatus] |  (optional)
work_category = [swagger_client.WorkCategory()] # list[WorkCategory] |  (optional)
is_high_impact_traffic_management = true # bool |  (optional)
usrn = 'usrn_example' # str |  (optional)
promoter_organisation_name = 'promoter_organisation_name_example' # str |  (optional)
ha_organisation_name = 'ha_organisation_name_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_interested_party_permits(offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, street_descriptor=street_descriptor, permit_reference_number=permit_reference_number, work_reference_number=work_reference_number, work_start_date_from=work_start_date_from, work_start_date_to=work_start_date_to, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, start_date_created=start_date_created, end_date_created=end_date_created, work_status=work_status, work_category=work_category, is_high_impact_traffic_management=is_high_impact_traffic_management, usrn=usrn, promoter_organisation_name=promoter_organisation_name, ha_organisation_name=ha_organisation_name, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_interested_party_permits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **sort_column** | [**PermitSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **permit_reference_number** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **work_start_date_from** | **datetime**|  | [optional] 
 **work_start_date_to** | **datetime**|  | [optional] 
 **work_end_date_from** | **datetime**|  | [optional] 
 **work_end_date_to** | **datetime**|  | [optional] 
 **start_date_created** | **datetime**|  | [optional] 
 **end_date_created** | **datetime**|  | [optional] 
 **work_status** | [**list[WorkStatus]**](WorkStatus.md)|  | [optional] 
 **work_category** | [**list[WorkCategory]**](WorkCategory.md)|  | [optional] 
 **is_high_impact_traffic_management** | **bool**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **promoter_organisation_name** | **str**|  | [optional] 
 **ha_organisation_name** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**PermitReportingResponse**](PermitReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_material_classifications**
> MaterialClassificationReportingResponse get_material_classifications(street_descriptor=street_descriptor, usrn=usrn, offset=offset, sort_direction=sort_direction, material_classification_reference_number=material_classification_reference_number, material_classification_classification=material_classification_classification, date_sample_taken_from=date_sample_taken_from, date_sample_taken_to=date_sample_taken_to, date_created_from=date_created_from, date_created_to=date_created_to, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Material Classifications for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
offset = 1.2 # float |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
material_classification_reference_number = 'material_classification_reference_number_example' # str |  (optional)
material_classification_classification = swagger_client.MaterialClassificationClassification() # MaterialClassificationClassification |  (optional)
date_sample_taken_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_sample_taken_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_created_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_created_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_material_classifications(street_descriptor=street_descriptor, usrn=usrn, offset=offset, sort_direction=sort_direction, material_classification_reference_number=material_classification_reference_number, material_classification_classification=material_classification_classification, date_sample_taken_from=date_sample_taken_from, date_sample_taken_to=date_sample_taken_to, date_created_from=date_created_from, date_created_to=date_created_to, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_material_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **material_classification_reference_number** | **str**|  | [optional] 
 **material_classification_classification** | [**MaterialClassificationClassification**](.md)|  | [optional] 
 **date_sample_taken_from** | **datetime**|  | [optional] 
 **date_sample_taken_to** | **datetime**|  | [optional] 
 **date_created_from** | **datetime**|  | [optional] 
 **date_created_to** | **datetime**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**MaterialClassificationReportingResponse**](MaterialClassificationReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_compliances**
> NonComplianceReportingResponse get_non_compliances(non_compliance_date_created_from=non_compliance_date_created_from, non_compliance_date_created_to=non_compliance_date_created_to, non_compliance_reference_number=non_compliance_reference_number, non_compliance_status=non_compliance_status, ha_response_status=ha_response_status, promoter_response_status=promoter_response_status, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, offset=offset, sort_column=sort_column, sort_direction=sort_direction, most_recent_inspection_type=most_recent_inspection_type, most_recent_inspection_outcome=most_recent_inspection_outcome, most_recent_inspection_promoter_response_status=most_recent_inspection_promoter_response_status, most_recent_inspection_ha_response_status=most_recent_inspection_ha_response_status, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get non compliances for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
non_compliance_date_created_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
non_compliance_date_created_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
non_compliance_reference_number = 'non_compliance_reference_number_example' # str |  (optional)
non_compliance_status = [swagger_client.NonComplianceStatus()] # list[NonComplianceStatus] |  (optional)
ha_response_status = [swagger_client.NonComplianceResponseStatus()] # list[NonComplianceResponseStatus] |  (optional)
promoter_response_status = [swagger_client.NonComplianceResponseStatus()] # list[NonComplianceResponseStatus] |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.NonComplianceSortColumn() # NonComplianceSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
most_recent_inspection_type = [swagger_client.InspectionType()] # list[InspectionType] |  (optional)
most_recent_inspection_outcome = [swagger_client.InspectionOutcome()] # list[InspectionOutcome] |  (optional)
most_recent_inspection_promoter_response_status = [swagger_client.PromoterInspectionOutcomeStatusType()] # list[PromoterInspectionOutcomeStatusType] |  (optional)
most_recent_inspection_ha_response_status = [swagger_client.HAInspectionOutcomeStatusType()] # list[HAInspectionOutcomeStatusType] |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_non_compliances(non_compliance_date_created_from=non_compliance_date_created_from, non_compliance_date_created_to=non_compliance_date_created_to, non_compliance_reference_number=non_compliance_reference_number, non_compliance_status=non_compliance_status, ha_response_status=ha_response_status, promoter_response_status=promoter_response_status, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, offset=offset, sort_column=sort_column, sort_direction=sort_direction, most_recent_inspection_type=most_recent_inspection_type, most_recent_inspection_outcome=most_recent_inspection_outcome, most_recent_inspection_promoter_response_status=most_recent_inspection_promoter_response_status, most_recent_inspection_ha_response_status=most_recent_inspection_ha_response_status, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_non_compliances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **non_compliance_date_created_from** | **datetime**|  | [optional] 
 **non_compliance_date_created_to** | **datetime**|  | [optional] 
 **non_compliance_reference_number** | **str**|  | [optional] 
 **non_compliance_status** | [**list[NonComplianceStatus]**](NonComplianceStatus.md)|  | [optional] 
 **ha_response_status** | [**list[NonComplianceResponseStatus]**](NonComplianceResponseStatus.md)|  | [optional] 
 **promoter_response_status** | [**list[NonComplianceResponseStatus]**](NonComplianceResponseStatus.md)|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**NonComplianceSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **most_recent_inspection_type** | [**list[InspectionType]**](InspectionType.md)|  | [optional] 
 **most_recent_inspection_outcome** | [**list[InspectionOutcome]**](InspectionOutcome.md)|  | [optional] 
 **most_recent_inspection_promoter_response_status** | [**list[PromoterInspectionOutcomeStatusType]**](PromoterInspectionOutcomeStatusType.md)|  | [optional] 
 **most_recent_inspection_ha_response_status** | [**list[HAInspectionOutcomeStatusType]**](HAInspectionOutcomeStatusType.md)|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**NonComplianceReportingResponse**](NonComplianceReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbi_sample_generation_jobs**
> PbiSampleGenerationJobsReportingResponse get_pbi_sample_generation_jobs(offset=offset, include_total_count=include_total_count)



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
offset = 1.2 # float |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_pbi_sample_generation_jobs(offset=offset, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pbi_sample_generation_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**PbiSampleGenerationJobsReportingResponse**](PbiSampleGenerationJobsReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbi_sample_inspection_targets**
> PbiSampleInspectionTargetReportingResponse get_pbi_sample_inspection_targets(offset=offset, quarter_start_date=quarter_start_date, sort_column=sort_column, sort_direction=sort_direction, include_total_count=include_total_count)



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
offset = 1.2 # float |  (optional)
quarter_start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sort_column = swagger_client.PbiSampleInspectionTargetSortColumn() # PbiSampleInspectionTargetSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_pbi_sample_inspection_targets(offset=offset, quarter_start_date=quarter_start_date, sort_column=sort_column, sort_direction=sort_direction, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pbi_sample_inspection_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **quarter_start_date** | **datetime**|  | [optional] 
 **sort_column** | [**PbiSampleInspectionTargetSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**PbiSampleInspectionTargetReportingResponse**](PbiSampleInspectionTargetReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pbi_sample_inspections**
> PbiSampleInspectionReportingResponse get_pbi_sample_inspections(offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, sort_direction=sort_direction, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, sample_expiry_date_from=sample_expiry_date_from, sample_expiry_date_to=sample_expiry_date_to, sort_column=sort_column, include_total_count=include_total_count)



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
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
sample_expiry_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sample_expiry_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
sort_column = swagger_client.PbiSampleInspectionSortColumn() # PbiSampleInspectionSortColumn |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_pbi_sample_inspections(offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, sort_direction=sort_direction, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, sample_expiry_date_from=sample_expiry_date_from, sample_expiry_date_to=sample_expiry_date_to, sort_column=sort_column, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pbi_sample_inspections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **sample_expiry_date_from** | **datetime**|  | [optional] 
 **sample_expiry_date_to** | **datetime**|  | [optional] 
 **sort_column** | [**PbiSampleInspectionSortColumn**](.md)|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**PbiSampleInspectionReportingResponse**](PbiSampleInspectionReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_duration_challenges**
> PermitDurationChallengeReportingResponse get_permit_duration_challenges(offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, organisation=organisation, geographical_area_reference_number=geographical_area_reference_number, duration_challenge_review_status=duration_challenge_review_status, duration_challenge_non_acceptance_response_status=duration_challenge_non_acceptance_response_status, work_status=work_status, street_descriptor=street_descriptor, usrn=usrn, permit_reference_number=permit_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Permit Duration Challenges for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
offset = 1.2 # float |  (optional)
sort_column = swagger_client.PermitDurationChallengeSortColumn() # PermitDurationChallengeSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
organisation = 'organisation_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
duration_challenge_review_status = [swagger_client.DurationChallengeReviewStatus()] # list[DurationChallengeReviewStatus] |  (optional)
duration_challenge_non_acceptance_response_status = [swagger_client.DurationChallengeNonAcceptanceResponseStatus()] # list[DurationChallengeNonAcceptanceResponseStatus] |  (optional)
work_status = [swagger_client.WorkStatus()] # list[WorkStatus] |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
permit_reference_number = 'permit_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_permit_duration_challenges(offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, organisation=organisation, geographical_area_reference_number=geographical_area_reference_number, duration_challenge_review_status=duration_challenge_review_status, duration_challenge_non_acceptance_response_status=duration_challenge_non_acceptance_response_status, work_status=work_status, street_descriptor=street_descriptor, usrn=usrn, permit_reference_number=permit_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit_duration_challenges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **sort_column** | [**PermitDurationChallengeSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **duration_challenge_review_status** | [**list[DurationChallengeReviewStatus]**](DurationChallengeReviewStatus.md)|  | [optional] 
 **duration_challenge_non_acceptance_response_status** | [**list[DurationChallengeNonAcceptanceResponseStatus]**](DurationChallengeNonAcceptanceResponseStatus.md)|  | [optional] 
 **work_status** | [**list[WorkStatus]**](WorkStatus.md)|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **permit_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**PermitDurationChallengeReportingResponse**](PermitDurationChallengeReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permit_files**
> FileSummaryReportingResponse get_permit_files(permit_reference_number, file_type=file_type)



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
permit_reference_number = 'permit_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_permit_files(permit_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permit_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permit_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permits**
> PermitReportingResponse get_permits(status=status, work_status=work_status, work_category=work_category, lane_rental_assessment_outcome=lane_rental_assessment_outcome, active_permit_only=active_permit_only, start_date=start_date, end_date=end_date, work_start_date_from=work_start_date_from, work_start_date_to=work_start_date_to, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, start_date_created=start_date_created, end_date_created=end_date_created, offset=offset, sort_column=sort_column, sort_direction=sort_direction, is_traffic_sensitive=is_traffic_sensitive, is_high_impact_traffic_management=is_high_impact_traffic_management, has_no_final_registration=has_no_final_registration, has_excavation=has_excavation, is_early_start=is_early_start, is_deemed=is_deemed, lane_rental_charges_not_agreed=lane_rental_charges_not_agreed, lane_rental_charges_potentially_apply=lane_rental_charges_potentially_apply, swa_code=swa_code, ever_modification_requested=ever_modification_requested, hs2_works_only=hs2_works_only, consultation_works_only=consultation_works_only, consent_works_only=consent_works_only, unacknowledged_by_ha_only=unacknowledged_by_ha_only, geographical_area_reference_number=geographical_area_reference_number, is_duration_challenged=is_duration_challenged, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, permit_reference_number=permit_reference_number, work_reference_number=work_reference_number, include_total_count=include_total_count, reasonable_period_end_date_from=reasonable_period_end_date_from, reasonable_period_end_date_to=reasonable_period_end_date_to)



See API specification Resource Guide > Reporting API > Get Permits for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
status = [swagger_client.PermitStatus()] # list[PermitStatus] |  (optional)
work_status = [swagger_client.WorkStatus()] # list[WorkStatus] |  (optional)
work_category = [swagger_client.WorkCategory()] # list[WorkCategory] |  (optional)
lane_rental_assessment_outcome = [swagger_client.LaneRentalAssessmentOutcome()] # list[LaneRentalAssessmentOutcome] |  (optional)
active_permit_only = true # bool |  (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_start_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_start_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.PermitSortColumn() # PermitSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
is_traffic_sensitive = true # bool |  (optional)
is_high_impact_traffic_management = true # bool |  (optional)
has_no_final_registration = true # bool |  (optional)
has_excavation = true # bool |  (optional)
is_early_start = true # bool |  (optional)
is_deemed = true # bool |  (optional)
lane_rental_charges_not_agreed = true # bool |  (optional)
lane_rental_charges_potentially_apply = true # bool |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
ever_modification_requested = true # bool |  (optional)
hs2_works_only = true # bool |  (optional)
consultation_works_only = true # bool |  (optional)
consent_works_only = true # bool |  (optional)
unacknowledged_by_ha_only = true # bool |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
is_duration_challenged = true # bool |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
permit_reference_number = 'permit_reference_number_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)
reasonable_period_end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
reasonable_period_end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_permits(status=status, work_status=work_status, work_category=work_category, lane_rental_assessment_outcome=lane_rental_assessment_outcome, active_permit_only=active_permit_only, start_date=start_date, end_date=end_date, work_start_date_from=work_start_date_from, work_start_date_to=work_start_date_to, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, start_date_created=start_date_created, end_date_created=end_date_created, offset=offset, sort_column=sort_column, sort_direction=sort_direction, is_traffic_sensitive=is_traffic_sensitive, is_high_impact_traffic_management=is_high_impact_traffic_management, has_no_final_registration=has_no_final_registration, has_excavation=has_excavation, is_early_start=is_early_start, is_deemed=is_deemed, lane_rental_charges_not_agreed=lane_rental_charges_not_agreed, lane_rental_charges_potentially_apply=lane_rental_charges_potentially_apply, swa_code=swa_code, ever_modification_requested=ever_modification_requested, hs2_works_only=hs2_works_only, consultation_works_only=consultation_works_only, consent_works_only=consent_works_only, unacknowledged_by_ha_only=unacknowledged_by_ha_only, geographical_area_reference_number=geographical_area_reference_number, is_duration_challenged=is_duration_challenged, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, permit_reference_number=permit_reference_number, work_reference_number=work_reference_number, include_total_count=include_total_count, reasonable_period_end_date_from=reasonable_period_end_date_from, reasonable_period_end_date_to=reasonable_period_end_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_permits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[PermitStatus]**](PermitStatus.md)|  | [optional] 
 **work_status** | [**list[WorkStatus]**](WorkStatus.md)|  | [optional] 
 **work_category** | [**list[WorkCategory]**](WorkCategory.md)|  | [optional] 
 **lane_rental_assessment_outcome** | [**list[LaneRentalAssessmentOutcome]**](LaneRentalAssessmentOutcome.md)|  | [optional] 
 **active_permit_only** | **bool**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **work_start_date_from** | **datetime**|  | [optional] 
 **work_start_date_to** | **datetime**|  | [optional] 
 **work_end_date_from** | **datetime**|  | [optional] 
 **work_end_date_to** | **datetime**|  | [optional] 
 **start_date_created** | **datetime**|  | [optional] 
 **end_date_created** | **datetime**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**PermitSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **is_traffic_sensitive** | **bool**|  | [optional] 
 **is_high_impact_traffic_management** | **bool**|  | [optional] 
 **has_no_final_registration** | **bool**|  | [optional] 
 **has_excavation** | **bool**|  | [optional] 
 **is_early_start** | **bool**|  | [optional] 
 **is_deemed** | **bool**|  | [optional] 
 **lane_rental_charges_not_agreed** | **bool**|  | [optional] 
 **lane_rental_charges_potentially_apply** | **bool**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **ever_modification_requested** | **bool**|  | [optional] 
 **hs2_works_only** | **bool**|  | [optional] 
 **consultation_works_only** | **bool**|  | [optional] 
 **consent_works_only** | **bool**|  | [optional] 
 **unacknowledged_by_ha_only** | **bool**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **is_duration_challenged** | **bool**|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **permit_reference_number** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 
 **reasonable_period_end_date_from** | **datetime**|  | [optional] 
 **reasonable_period_end_date_to** | **datetime**|  | [optional] 

### Return type

[**PermitReportingResponse**](PermitReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_street_files**
> FileSummaryReportingResponse get_private_street_files(private_street_reference_number, file_type=file_type)



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
private_street_reference_number = 'private_street_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_private_street_files(private_street_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_private_street_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_street_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_private_streets**
> PrivateStreetReportingResponse get_private_streets(offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, sort_direction=sort_direction, sort_column=sort_column, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, private_street_reference_number=private_street_reference_number, start_date_from=start_date_from, start_date_to=start_date_to, end_date_from=end_date_from, end_date_to=end_date_to, date_created_from=date_created_from, date_created_to=date_created_to, private_street_status=private_street_status, include_total_count=include_total_count)



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
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
sort_column = swagger_client.PrivateStreetNoticeSortColumn() # PrivateStreetNoticeSortColumn |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
private_street_reference_number = 'private_street_reference_number_example' # str |  (optional)
start_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_created_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_created_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
private_street_status = [swagger_client.PrivateStreetStatus()] # list[PrivateStreetStatus] |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_private_streets(offset=offset, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, sort_direction=sort_direction, sort_column=sort_column, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, private_street_reference_number=private_street_reference_number, start_date_from=start_date_from, start_date_to=start_date_to, end_date_from=end_date_from, end_date_to=end_date_to, date_created_from=date_created_from, date_created_to=date_created_to, private_street_status=private_street_status, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_private_streets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **sort_column** | [**PrivateStreetNoticeSortColumn**](.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **private_street_reference_number** | **str**|  | [optional] 
 **start_date_from** | **datetime**|  | [optional] 
 **start_date_to** | **datetime**|  | [optional] 
 **end_date_from** | **datetime**|  | [optional] 
 **end_date_to** | **datetime**|  | [optional] 
 **date_created_from** | **datetime**|  | [optional] 
 **date_created_to** | **datetime**|  | [optional] 
 **private_street_status** | [**list[PrivateStreetStatus]**](PrivateStreetStatus.md)|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**PrivateStreetReportingResponse**](PrivateStreetReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reinspections**
> ReinspectionReportingResponse get_reinspections(start_date=start_date, end_date=end_date, inspection_type=inspection_type, offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, inspection_category=inspection_category, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get reinspections for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
inspection_type = [swagger_client.InspectionType()] # list[InspectionType] |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.ReinspectionSortColumn() # ReinspectionSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
inspection_category = [swagger_client.InspectionCategory()] # list[InspectionCategory] |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_reinspections(start_date=start_date, end_date=end_date, inspection_type=inspection_type, offset=offset, sort_column=sort_column, sort_direction=sort_direction, swa_code=swa_code, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, inspection_category=inspection_category, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_reinspections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **inspection_type** | [**list[InspectionType]**](InspectionType.md)|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**ReinspectionSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **inspection_category** | [**list[InspectionCategory]**](InspectionCategory.md)|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**ReinspectionReportingResponse**](ReinspectionReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reinstatement_files**
> FileSummaryReportingResponse get_reinstatement_files(reinstatement_reference_number, file_type=file_type)



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
reinstatement_reference_number = 'reinstatement_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_reinstatement_files(reinstatement_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_reinstatement_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reinstatement_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reinstatements**
> ReinstatementReportingResponse get_reinstatements(sort_column=sort_column, sort_direction=sort_direction, status=status, offset=offset, swa_code=swa_code, latest_reinstatements_only=latest_reinstatements_only, registration_date_from=registration_date_from, registration_date_to=registration_date_to, end_date_from=end_date_from, end_date_to=end_date_to, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, work_reference_number_exact=work_reference_number_exact, include_total_count=include_total_count)



Returns all reinstatements associated with the logged in user's organisation. Optional filter by status Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
sort_column = swagger_client.ReinstatementSortColumn() # ReinstatementSortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
status = [swagger_client.ReinstatementStatus()] # list[ReinstatementStatus] |  (optional)
offset = 1.2 # float |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
latest_reinstatements_only = true # bool |  (optional)
registration_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
registration_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
work_reference_number_exact = 'work_reference_number_exact_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_reinstatements(sort_column=sort_column, sort_direction=sort_direction, status=status, offset=offset, swa_code=swa_code, latest_reinstatements_only=latest_reinstatements_only, registration_date_from=registration_date_from, registration_date_to=registration_date_to, end_date_from=end_date_from, end_date_to=end_date_to, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, work_reference_number=work_reference_number, work_reference_number_exact=work_reference_number_exact, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_reinstatements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_column** | [**ReinstatementSortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **status** | [**list[ReinstatementStatus]**](ReinstatementStatus.md)|  | [optional] 
 **offset** | **float**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **latest_reinstatements_only** | **bool**|  | [optional] 
 **registration_date_from** | **datetime**|  | [optional] 
 **registration_date_to** | **datetime**|  | [optional] 
 **end_date_from** | **datetime**|  | [optional] 
 **end_date_to** | **datetime**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **work_reference_number_exact** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**ReinstatementReportingResponse**](ReinstatementReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reinstatements_due**
> ReinstatementsDueReportingResponse get_reinstatements_due(swa_code=swa_code, street_descriptor=street_descriptor, usrn=usrn, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, work_reference_number=work_reference_number, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, registration_due_date_from=registration_due_date_from, registration_due_date_to=registration_due_date_to, include_total_count=include_total_count)



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
swa_code = 'swa_code_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
work_reference_number = 'work_reference_number_example' # str |  (optional)
work_end_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
work_end_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
registration_due_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
registration_due_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_reinstatements_due(swa_code=swa_code, street_descriptor=street_descriptor, usrn=usrn, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, work_reference_number=work_reference_number, work_end_date_from=work_end_date_from, work_end_date_to=work_end_date_to, registration_due_date_from=registration_due_date_from, registration_due_date_to=registration_due_date_to, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_reinstatements_due: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swa_code** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **work_reference_number** | **str**|  | [optional] 
 **work_end_date_from** | **datetime**|  | [optional] 
 **work_end_date_to** | **datetime**|  | [optional] 
 **registration_due_date_from** | **datetime**|  | [optional] 
 **registration_due_date_to** | **datetime**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**ReinstatementsDueReportingResponse**](ReinstatementsDueReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section58s**
> Section58ReportingResponse get_section58s(ha_organisation_name=ha_organisation_name, start_date_from=start_date_from, start_date_to=start_date_to, section_58_status=section_58_status, offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, section_58_reference_number=section_58_reference_number, street_descriptor=street_descriptor, usrn=usrn, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Section 58s for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
ha_organisation_name = 'ha_organisation_name_example' # str |  (optional)
start_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
section_58_status = [swagger_client.Section58Status()] # list[Section58Status] |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.Section58SortColumn() # Section58SortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
section_58_reference_number = 'section_58_reference_number_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_section58s(ha_organisation_name=ha_organisation_name, start_date_from=start_date_from, start_date_to=start_date_to, section_58_status=section_58_status, offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, section_58_reference_number=section_58_reference_number, street_descriptor=street_descriptor, usrn=usrn, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section58s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ha_organisation_name** | **str**|  | [optional] 
 **start_date_from** | **datetime**|  | [optional] 
 **start_date_to** | **datetime**|  | [optional] 
 **section_58_status** | [**list[Section58Status]**](Section58Status.md)|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**Section58SortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **section_58_reference_number** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**Section58ReportingResponse**](Section58ReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section74_files**
> FileSummaryReportingResponse get_section74_files(section_74_reference_number, file_type=file_type)



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
section_74_reference_number = 'section_74_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_section74_files(section_74_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section74_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_74_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section74s**
> Section74ReportingResponse get_section74s(section_74_ha_status=section_74_ha_status, issue_date_from=issue_date_from, issue_date_to=issue_date_to, swa_code=swa_code, offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, section_74_reference_number=section_74_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Section 74s for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
section_74_ha_status = [swagger_client.Section74HAStatus()] # list[Section74HAStatus] |  (optional)
issue_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
issue_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.Section74SortColumn() # Section74SortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
section_74_reference_number = 'section_74_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_section74s(section_74_ha_status=section_74_ha_status, issue_date_from=issue_date_from, issue_date_to=issue_date_to, swa_code=swa_code, offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, street_descriptor=street_descriptor, usrn=usrn, section_74_reference_number=section_74_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section74s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_74_ha_status** | [**list[Section74HAStatus]**](Section74HAStatus.md)|  | [optional] 
 **issue_date_from** | **datetime**|  | [optional] 
 **issue_date_to** | **datetime**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**Section74SortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **section_74_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**Section74ReportingResponse**](Section74ReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section81_files**
> FileSummaryReportingResponse get_section81_files(section_81_reference_number, file_type=file_type)



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
section_81_reference_number = 'section_81_reference_number_example' # str | 
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_section81_files(section_81_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section81_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_81_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section81s**
> Section81ReportingResponse get_section81s(section_81_status=section_81_status, section_81_severity=section_81_severity, issue_date_from=issue_date_from, issue_date_to=issue_date_to, status_changed_date_from=status_changed_date_from, status_changed_date_to=status_changed_date_to, swa_code=swa_code, offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, section_81_type=section_81_type, street_descriptor=street_descriptor, usrn=usrn, section_81_reference_number=section_81_reference_number, include_total_count=include_total_count)



See API specification Resource Guide > Reporting API > Get Section 81s for more information Authenticated user must have one of the following roles: Planner, Contractor, HighwayAuthority

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
section_81_status = [swagger_client.Section81Status()] # list[Section81Status] |  (optional)
section_81_severity = [swagger_client.Section81Severity()] # list[Section81Severity] |  (optional)
issue_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
issue_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
status_changed_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
status_changed_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
swa_code = 'swa_code_example' # str |  (optional)
offset = 1.2 # float |  (optional)
sort_column = swagger_client.Section81SortColumn() # Section81SortColumn |  (optional)
sort_direction = swagger_client.SortDirection() # SortDirection |  (optional)
geographical_area_reference_number = ['geographical_area_reference_number_example'] # list[str] |  (optional)
organisation = 'organisation_example' # str |  (optional)
section_81_type = [swagger_client.Section81Type()] # list[Section81Type] |  (optional)
street_descriptor = 'street_descriptor_example' # str |  (optional)
usrn = 'usrn_example' # str |  (optional)
section_81_reference_number = 'section_81_reference_number_example' # str |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_section81s(section_81_status=section_81_status, section_81_severity=section_81_severity, issue_date_from=issue_date_from, issue_date_to=issue_date_to, status_changed_date_from=status_changed_date_from, status_changed_date_to=status_changed_date_to, swa_code=swa_code, offset=offset, sort_column=sort_column, sort_direction=sort_direction, geographical_area_reference_number=geographical_area_reference_number, organisation=organisation, section_81_type=section_81_type, street_descriptor=street_descriptor, usrn=usrn, section_81_reference_number=section_81_reference_number, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_section81s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_81_status** | [**list[Section81Status]**](Section81Status.md)|  | [optional] 
 **section_81_severity** | [**list[Section81Severity]**](Section81Severity.md)|  | [optional] 
 **issue_date_from** | **datetime**|  | [optional] 
 **issue_date_to** | **datetime**|  | [optional] 
 **status_changed_date_from** | **datetime**|  | [optional] 
 **status_changed_date_to** | **datetime**|  | [optional] 
 **swa_code** | **str**|  | [optional] 
 **offset** | **float**|  | [optional] 
 **sort_column** | [**Section81SortColumn**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **geographical_area_reference_number** | [**list[str]**](str.md)|  | [optional] 
 **organisation** | **str**|  | [optional] 
 **section_81_type** | [**list[Section81Type]**](Section81Type.md)|  | [optional] 
 **street_descriptor** | **str**|  | [optional] 
 **usrn** | **str**|  | [optional] 
 **section_81_reference_number** | **str**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**Section81ReportingResponse**](Section81ReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_files**
> FileSummaryReportingResponse get_work_files(work_reference_number, file_type=file_type)



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
file_type = [swagger_client.FileType()] # list[FileType] |  (optional)

try:
    api_response = api_instance.get_work_files(work_reference_number, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_work_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | 
 **file_type** | [**list[FileType]**](FileType.md)|  | [optional] 

### Return type

[**FileSummaryReportingResponse**](FileSummaryReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_works**
> WorkSearchReportingResponse get_works(work_reference_number=work_reference_number, swa_code=swa_code)



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
work_reference_number = 'work_reference_number_example' # str |  (optional)
swa_code = 'swa_code_example' # str |  (optional)

try:
    api_response = api_instance.get_works(work_reference_number=work_reference_number, swa_code=swa_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_works: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_reference_number** | **str**|  | [optional] 
 **swa_code** | **str**|  | [optional] 

### Return type

[**WorkSearchReportingResponse**](WorkSearchReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workstreams**
> WorkstreamReportingResponse get_workstreams(status=status, offset=offset, include_total_count=include_total_count)



Returns all workstreams associated with the logged in user's organisation. Optional filter by status Authenticated user must have one of the following roles: Admin

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
status = [swagger_client.WorkstreamStatus()] # list[WorkstreamStatus] |  (optional)
offset = 1.2 # float |  (optional)
include_total_count = true # bool |  (optional)

try:
    api_response = api_instance.get_workstreams(status=status, offset=offset, include_total_count=include_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workstreams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[WorkstreamStatus]**](WorkstreamStatus.md)|  | [optional] 
 **offset** | **float**|  | [optional] 
 **include_total_count** | **bool**|  | [optional] 

### Return type

[**WorkstreamReportingResponse**](WorkstreamReportingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

