# InspectionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inspection_reference_number** | **str** |  | 
**inspection_type** | [**InspectionTypeResponse**](InspectionTypeResponse.md) |  | 
**inspection_type_string** | **str** |  | 
**inspection_start_date** | **datetime** |  | 
**inspection_category** | **AllOfInspectionResponseInspectionCategory** |  | [optional] 
**inspection_category_string** | **str** |  | [optional] 
**inspection_outcome** | [**InspectionOutcomeResponse**](InspectionOutcomeResponse.md) |  | 
**inspection_outcome_string** | **str** |  | 
**failure_reason_details** | [**list[FailureReasonDetailsResponse]**](FailureReasonDetailsResponse.md) |  | [optional] 
**inspection_outcome_details** | **str** |  | [optional] 
**was_call_logged** | **bool** |  | [optional] 
**call_logged_to** | **str** |  | [optional] 
**call_logged_reference** | **str** |  | [optional] 
**call_logged_summary** | **str** |  | [optional] 
**defect_fixed_on_site** | **AllOfInspectionResponseDefectFixedOnSite** |  | [optional] 
**defect_fixed_on_site_string** | **str** |  | [optional] 
**additional_comments** | **str** |  | [optional] 
**date_created** | **datetime** |  | 
**date_modified** | **datetime** |  | 
**files** | [**list[FileSummaryResponse]**](FileSummaryResponse.md) |  | [optional] 
**work_reference_number** | **str** |  | 
**reinspection_date** | **datetime** |  | [optional] 
**reinspection_date_time** | **datetime** |  | [optional] 
**username** | **str** |  | 
**promoter_organisation** | **str** |  | 
**highway_authority** | **str** |  | 
**inspector_name** | **str** |  | [optional] 
**made_safe_by_ha** | **bool** |  | [optional] 
**inspection_status** | [**InspectionStatusResponse**](InspectionStatusResponse.md) |  | 
**inspection_status_string** | **str** |  | 
**inspection_reason_for_withdrawal** | **AllOfInspectionResponseInspectionReasonForWithdrawal** |  | [optional] 
**inspection_reason_for_withdrawal_string** | **str** |  | [optional] 
**withdrawal_details** | **str** |  | [optional] 
**promoter_response_status** | **AllOfInspectionResponsePromoterResponseStatus** |  | [optional] 
**promoter_response_status_string** | **str** |  | [optional] 
**promoter_response_status_change_date** | **datetime** |  | [optional] 
**promoter_response_details** | **str** |  | [optional] 
**ha_response_status** | **AllOfInspectionResponseHaResponseStatus** |  | [optional] 
**ha_response_status_string** | **str** |  | [optional] 
**ha_response_status_change_date** | **datetime** |  | [optional] 
**ha_response_details** | **str** |  | [optional] 
**auto_acceptance_due_date** | **datetime** |  | [optional] 
**is_auto_accepted** | **bool** |  | 
**non_compliance_reference_number** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

