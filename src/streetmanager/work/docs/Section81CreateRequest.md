# Section81CreateRequest

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
**location_description** | **str** | Max length 500 characters | 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**inspection_date** | **datetime** | Date must be today or a date in the past | 
**section_81_type** | [**Section81Type**](Section81Type.md) |  | 
**section_81_severity** | **AllOfSection81CreateRequestSection81Severity** | Required if section_81_type is not unattributed_works_completed or unattributed_works_live_site | [optional] 
**made_safe_by_ha** | **bool** | Required if section_81_type is not unattributed_works_completed or unattributed_works_live_site | [optional] 
**inspector_name** | **str** | Max length 100 characters | [optional] 
**inspector_contact_number** | **str** | Max length 100 characters | [optional] 
**additional_details** | **str** | Max length 500 characters | 
**other_type_details** | **str** | Max length 100 characters | [optional] 
**reinspection_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**reinspection_date_time** | **datetime** | The date for reinspection_date_time must match the date for reinspection_date Time must occur today or a date in the future | [optional] 
**section_81_evidence** | **bool** |  | 
**file_ids** | **list[float]** | Required if section_81_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

