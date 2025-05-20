# PrivateStreetNoticeCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**promoter_swa_code** | **str** | Max length 4 characters | 
**highway_authority_swa_code** | **str** | Max length 4 characters | 
**works_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon | 
**street_name** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**town** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**area_name** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**usrn** | **float** | Is whole number between 1000001 and 99999999 inclusive See business rules section 1.4 - USRN | 
**road_category** | **float** | Is whole number between 0 and 10 inclusive If not provided, populated with NSG data related to supplied USRN | [optional] 
**work_reference_number** | **str** |  | [optional] 
**secondary_contact** | **str** |  | 
**secondary_contact_number** | **str** |  | 
**secondary_contact_email** | **str** |  | [optional] 
**proposed_start_date** | **datetime** |  | 
**proposed_start_time** | **datetime** |  | [optional] 
**proposed_end_date** | **datetime** |  | 
**proposed_end_time** | **datetime** |  | [optional] 
**description_of_work** | **str** |  | 
**excavation** | **bool** |  | 
**project_reference_number** | **str** |  | [optional] 
**traffic_management_plan** | **bool** |  | 
**traffic_management_type** | [**TrafficManagementType**](TrafficManagementType.md) |  | 
**location_types** | [**list[LocationType]**](LocationType.md) |  | 
**file_ids** | **list[float]** |  | [optional] 
**close_footway** | [**CloseFootway**](CloseFootway.md) |  | 
**close_footpath** | [**CloseFootpath**](CloseFootpath.md) |  | 
**works_location_description** | **str** |  | 
**workstream_prefix** | **str** |  | [optional] 
**additional_contact** | **str** |  | [optional] 
**additional_contact_number** | **str** |  | [optional] 
**additional_contact_email** | **str** |  | [optional] 
**emergency_contact_name** | **str** |  | [optional] 
**emergency_contact_number** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

