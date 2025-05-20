# Section58UpdateStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**status** | [**Section58Status**](Section58Status.md) |  | 
**start_date** | **datetime** | Required when status is in_force Date must be a valid date | [optional] 
**cancellation_reason** | **str** | Optional. Valid when status is cancelled. Max length 500 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

