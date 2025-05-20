# PermitAlterationStatusUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**alteration_status** | [**AlterationStatus**](AlterationStatus.md) |  | 
**assessment_comments** | **str** | Required if alteration_status &#x3D; refused or granted_with_duration_challenge Max length 1500 characters | [optional] 
**assessment_discount** | **float** | Required if alteration_status &#x3D; granted Is whole number between 0 and 100 inclusive | [optional] 
**reasonable_period_end_date** | **datetime** | Required if alteration_status &#x3D; granted_with_duration_challenge Must be on or after the permit proposed_end_date and before the alteration updated proposed_end_date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

