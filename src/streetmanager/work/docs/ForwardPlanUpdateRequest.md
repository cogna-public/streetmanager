# ForwardPlanUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**works_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** | end_date must be on or after start_date | 
**works_location_description** | **str** | Max length 500 characters | 
**description_of_work** | **str** | Max length 500 characters | 
**project_reference_number** | **str** | Max length 100 characters | [optional] 
**traffic_management_type** | **AllOfForwardPlanUpdateRequestTrafficManagementType** |  | [optional] 
**additional_info** | **str** | Max length 500 characters | [optional] 
**forward_plan_asds** | [**list[PermitASD]**](PermitASD.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

