# NonComplianceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_compliance_reference_number** | **str** |  | 
**work_reference_number** | **str** |  | 
**date_created** | **datetime** |  | 
**non_compliance_status** | [**NonComplianceStatusResponse**](NonComplianceStatusResponse.md) |  | 
**non_compliance_status_string** | **str** |  | 
**jsm_requested_by** | **str** |  | [optional] 
**jsm_suggested_time** | **datetime** |  | [optional] 
**jsm_status** | **AllOfNonComplianceResponseJsmStatus** |  | [optional] 
**jsm_status_string** | **str** |  | [optional] 
**promoter_response_status** | **AllOfNonComplianceResponsePromoterResponseStatus** |  | [optional] 
**promoter_response_status_string** | **str** |  | [optional] 
**promoter_response_update_date** | **datetime** |  | [optional] 
**promoter_response_additional_details** | **str** |  | [optional] 
**promoter_response_jsm_date** | **datetime** |  | [optional] 
**ha_response_status** | [**NonComplianceResponseStatusResponse**](NonComplianceResponseStatusResponse.md) |  | 
**ha_response_status_string** | **str** |  | 
**ha_response_update_date** | **datetime** |  | [optional] 
**ha_response_additional_details** | **str** |  | [optional] 
**ha_response_jsm_date** | **datetime** |  | [optional] 
**latest_inspection** | [**InspectionResponse**](InspectionResponse.md) |  | 
**linked_inspections** | [**list[InspectionSummaryResponse]**](InspectionSummaryResponse.md) |  | 
**linked_permits** | [**list[PermitSummaryResponse]**](PermitSummaryResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

