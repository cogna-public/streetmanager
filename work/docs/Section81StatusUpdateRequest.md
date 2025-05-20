# Section81StatusUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**section_81_status** | [**Section81Status**](Section81Status.md) |  | 
**status_reason** | **str** | Required if Section81Status &#x3D; rejected, accepted_fixed, resolved or cancelled Max length 500 characters | [optional] 
**work_type** | **AllOfSection81StatusUpdateRequestWorkType** | Required if Section81Status &#x3D; accepted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

