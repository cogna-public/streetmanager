# ActivityUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**activity_name** | **str** | Max length 100 characters | 
**activity_activity_type** | [**ActivityActivityType**](ActivityActivityType.md) |  | 
**activity_type_details** | **str** | Required if activity_activity_type &#x3D; other Max length 100 characters | [optional] 
**contact_name** | **str** | Max length 100 characters | [optional] 
**contact_details** | **str** | Max length 100 characters | [optional] 
**start_date** | **datetime** | Must be in the future | 
**start_time** | **datetime** | Must be in the future | [optional] 
**end_date** | **datetime** | Must be after start_date | 
**end_time** | **datetime** | Must be after start_date | [optional] 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**activity_location_description** | **str** | Max length 500 characters | 
**traffic_management_type** | [**TrafficManagementType**](TrafficManagementType.md) |  | 
**collaborative_working** | **bool** |  | 
**additional_info** | **str** | Max length 500 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

