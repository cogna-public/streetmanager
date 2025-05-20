# PermitAssessmentUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**assessment_status** | [**AssessmentStatus**](AssessmentStatus.md) |  | 
**additional_comments** | **str** | Required if assessment_status &#x3D; refused or is_duration_challenged &#x3D; true Max length 1500 characters | [optional] 
**reasons_for_refusal** | [**list[ReasonForRefusal]**](ReasonForRefusal.md) | Array values must be unique Must contain between 1 and 5 values Required if assessment_status &#x3D; refused | [optional] 
**assessment_discount** | **float** | Required if assessment_status &#x3D; granted and permit&#x27;s work_category !&#x3D; hs2_highway Is whole number between 0 and 100 inclusive | [optional] 
**revoke_reason** | **str** | Required if assessment_status &#x3D; revoked Max length 500 characters | [optional] 
**pending_change_details** | **str** | Required if assessment_status &#x3D; permit_modification_request Max length 500 characters | [optional] 
**reasonable_period_end_date** | **datetime** | Required if is_duration_challenged &#x3D; true Must be at least 2 working days from start date | [optional] 
**is_duration_challenged** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

