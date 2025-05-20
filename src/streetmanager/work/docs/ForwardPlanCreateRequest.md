# ForwardPlanCreateRequest

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
**work_reference_number** | **str** | Max length 24 characters Must be unique in the system Must contain only alphanumeric characters, dashes and underscores If not supplied it will be auto-generated | [optional] 
**start_date** | **datetime** | start_date must be within five years of end_date | 
**end_date** | **datetime** | end_date must be on or after start_date | 
**description_of_work** | **str** | Max length 500 characters | 
**project_reference_number** | **str** | Max length 100 characters | [optional] 
**traffic_management_type** | **AllOfForwardPlanCreateRequestTrafficManagementType** |  | [optional] 
**additional_info** | **str** | Max length 500 characters | [optional] 
**forward_plan_asds** | [**list[PermitASD]**](PermitASD.md) |  | [optional] 
**works_location_description** | **str** | Max length 500 characters | 
**workstream_prefix** | **str** | Must consist of 3 positive whole numbers | [optional] 
**hs2_work_type** | **AllOfForwardPlanCreateRequestHs2WorkType** | Required if promoter_swa_code &#x3D; &#x27;7374&#x27; | [optional] 
**hs2_in_act_limits** | **bool** | Required if promoter_swa_code &#x3D; &#x27;7374&#x27; | [optional] 
**hs2_consultation_requested_response_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**hs2_highway_exemption** | **AllOfForwardPlanCreateRequestHs2HighwayExemption** | Required if hs2_work_type &#x3D; &#x27;hs2_highway_works&#x27; and hs2_in_act_limits &#x3D; true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

