# NonComplianceSummaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_compliance_reference_number** | **str** |  | 
**work_reference_number** | **str** |  | 
**promoter_organisation** | **str** |  | 
**ha_organisation** | **str** |  | 
**date_created** | **datetime** |  | 
**associated_inspections** | **float** |  | 
**non_compliance_status** | [**NonComplianceStatusResponse**](NonComplianceStatusResponse.md) |  | 
**non_compliance_status_string** | **str** |  | 
**latest_ha_response_status** | [**NonComplianceResponseStatusResponse**](NonComplianceResponseStatusResponse.md) |  | 
**latest_ha_response_status_string** | **str** |  | 
**latest_ha_response_date** | **datetime** |  | 
**latest_promoter_response_status** | **AllOfNonComplianceSummaryResponseLatestPromoterResponseStatus** |  | [optional] 
**latest_promoter_response_status_string** | **str** |  | [optional] 
**latest_promoter_response_date** | **datetime** |  | [optional] 
**street** | **str** |  | 
**town** | **str** |  | 
**area** | **str** |  | 
**most_recent_inspection_type** | [**InspectionTypeResponse**](InspectionTypeResponse.md) |  | 
**most_recent_inspection_type_string** | **str** |  | 
**most_recent_inspection_outcome** | [**InspectionOutcomeResponse**](InspectionOutcomeResponse.md) |  | 
**most_recent_inspection_outcome_string** | **str** |  | 
**most_recent_inspection_promoter_response_status** | **AllOfNonComplianceSummaryResponseMostRecentInspectionPromoterResponseStatus** |  | [optional] 
**most_recent_inspection_promoter_response_status_string** | **str** |  | [optional] 
**most_recent_inspection_ha_response_status** | **AllOfNonComplianceSummaryResponseMostRecentInspectionHaResponseStatus** |  | [optional] 
**most_recent_inspection_ha_response_status_string** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

