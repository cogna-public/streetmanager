# Section58CreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**section_58_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a line string or polygon | 
**contact_organisation** | **str** | Max length 100 characters | [optional] 
**contact_details** | **str** | Max length 100 characters | [optional] 
**start_date** | **datetime** | Date must occur today or a date in the future | 
**restriction_duration** | [**Section58Duration**](Section58Duration.md) |  | 
**restriction_extent** | [**Section58Extent**](Section58Extent.md) |  | 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**additional_information** | **str** | Max length 500 characters | [optional] 
**highway_authority_swa_code** | **str** | Max length 4 characters | 
**usrn** | **float** | Is whole number between 1000001 and 99999999 inclusive See business rules section 1.4 - USRN | 
**street_name** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**town** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**area_name** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

