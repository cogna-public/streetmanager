# MaterialClassificationCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**highway_authority_swa_code** | **str** | Max length 4 characters | 
**material_classification_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point Mandatory field Single GeoJSON Object | 
**street_name** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**town** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**area_name** | **str** | Max length 100 characters Use Street Lookup API endpoint /nsg/streets to lookup this information If not provided, populated with NSG data related to supplied USRN | [optional] 
**usrn** | **float** | Is whole number between 1000001 and 99999999 inclusive See business rules section 1.4 - USRN | 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**file_id** | **float** | Can only be one file Limited to 10MBs | [optional] 
**material_classification_classification** | [**MaterialClassificationClassification**](MaterialClassificationClassification.md) |  | 
**hazardous_material_type** | [**list[HazardousMaterialType]**](HazardousMaterialType.md) | Mandatory if material_classification_classification is hazardous | [optional] 
**hazardous_material_type_other_description** | **str** | Mandatory if MaterialClassificationClassification is hazardous and hazardous_material_type is other Max 500 chars | [optional] 
**layer_affected** | [**list[LayerAffected]**](LayerAffected.md) | Mandatory | 
**sample_date** | **datetime** | Mandatory Must be today or in the past | 
**location_description** | **str** | Mandatory | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

