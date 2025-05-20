# NonNotifiableSiteCreateRequest

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
**workstream_prefix** | **str** | Must consist of 3 positive whole numbers. Default workstream if not provided | [optional] 
**reinstatement_type** | [**ReinstatementType**](ReinstatementType.md) |  | 
**reinstatement_status** | [**ReinstatementStatus**](ReinstatementStatus.md) |  | 
**reinstatement_date** | **datetime** | reinstatement_date must be in the past Must be after actual start date Must be before actual end date (if entered) | 
**reinstatement_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon | 
**secondary_reinstatement_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon, if provided | [optional] 
**location_description** | **str** | Max length 500 characters | 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique Must not contain null or undefined values | 
**reinstatement_evidence** | **bool** | Whether reinstatement evidence has been supplied | 
**file_ids** | **list[float]** | Required if reinstatement_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**number_of_holes** | **float** | Must be a number between 0 and 100 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

