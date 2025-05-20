# CurrentTrafficManagementTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**current_traffic_management_type** | [**TrafficManagementType**](TrafficManagementType.md) |  | 
**current_traffic_management_emergency_contact_name** | **str** | Max length 100 characters Must be provided if current_traffic_management_type is multi_way_signals or two_way_signals | [optional] 
**current_traffic_management_emergency_contact_number** | **str** | Max length 100 characters Must be provided if current_traffic_management_type is multi_way_signals or two_way_signals | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

