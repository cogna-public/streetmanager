# InspectionCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**inspection_type** | [**InspectionType**](InspectionType.md) |  | 
**inspection_start_date** | **datetime** | inspection_start_date must be in the past | 
**inspection_category** | **AllOfInspectionCreateRequestInspectionCategory** | See business rules section 10.2 - Inspection types and categories | [optional] 
**inspection_outcome** | [**InspectionOutcome**](InspectionOutcome.md) |  | 
**failure_reason_details** | [**list[FailureReasonDetails]**](FailureReasonDetails.md) | See business rules section 10.3 - Inspection outcomes | [optional] 
**inspection_outcome_details** | **str** | Required if inspection_outcome &#x3D; unable_to_complete_inspection or non_compliant_with_conditions Max length 500 characters | [optional] 
**was_call_logged** | **bool** | Required if inspection_outcome &#x3D; failed_high and inspection_type &#x3D; live_site | [optional] 
**call_logged_to** | **str** | Required if was_call_logged &#x3D; true Max length 100 characters | [optional] 
**call_logged_reference** | **str** | Required if was_call_logged &#x3D; true Max length 100 characters | [optional] 
**call_logged_summary** | **str** | Required if was_call_logged &#x3D; true Max length 500 characters | [optional] 
**defect_fixed_on_site** | **AllOfInspectionCreateRequestDefectFixedOnSite** | Required if inspection_outcome &#x3D; failed_high and inspection_type &#x3D; live_site | [optional] 
**additional_comments** | **str** | Max length 500 characters | [optional] 
**inspection_evidence** | **bool** |  | 
**file_ids** | **list[float]** | Required if inspection_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**reinspection_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**reinspection_date_time** | **datetime** | The date for reinspection_date_time must match the date for reinspection_date Time must occur today or a date in the future | [optional] 
**reinspection_type** | **AllOfInspectionCreateRequestReinspectionType** | Defaulted to inspection_type value if this and/or reinspection_category are not provided and reinspection_date is provided | [optional] 
**reinspection_category** | **AllOfInspectionCreateRequestReinspectionCategory** | See business rules section 10.2 - Inspection types and categories Defaulted to inspection_category value if this and/or reinspection_type are not provided and reinspection_date is provided | [optional] 
**username** | **str** | Max length 100 characters Should be populated with the user creating the inspection | 
**inspector_name** | **str** | Max length 100 characters | [optional] 
**made_safe_by_ha** | **bool** | Required if inspection_type &#x3D; section 81 and inspection_outcome &#x3D; Failed - high or Failed - low | [optional] 
**non_compliance_reference_number** | **str** | Max length 106 characters Created inspection will be linked to an existing non-compliance with this reference number inspection_type must be reinstatement or non_compliance_follow_up | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

