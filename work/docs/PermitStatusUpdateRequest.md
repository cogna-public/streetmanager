# PermitStatusUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**permit_status** | [**PermitStatus**](PermitStatus.md) |  | 
**additional_comments** | **str** | Required if permit_status &#x3D; refused Max length 500 characters | [optional] 
**permit_cancellation_reason** | **AllOfPermitStatusUpdateRequestPermitCancellationReason** |  | [optional] 
**permit_cancellation_reason_other** | **str** | Required if permit_cancellation_reason is other | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

