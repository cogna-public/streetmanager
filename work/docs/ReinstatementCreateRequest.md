# ReinstatementCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**reinstatement_status** | [**ReinstatementStatus**](ReinstatementStatus.md) |  | 
**reinstatement_date** | **datetime** | reinstatement_date must be in the past Must be after actual start date Must be before actual end date (if entered) | 
**depth** | **float** | Is number between 0 and 99.99 inclusive, to two decimal places. Required if reinstatement type is excavation. | [optional] 
**length** | **float** | Is number between 0 and 9999.99 inclusive, to two decimal places Required if reinstatement type is excavation. | [optional] 
**width** | **float** | Is number between 0 and 99.99 inclusive, to two decimal places Required if reinstatement type is excavation. | [optional] 
**reinstatement_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon | 
**secondary_reinstatement_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon, if provided | [optional] 
**location_description** | **str** | Max length 500 characters | 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique Must not contain null or undefined values | 
**reinstatement_evidence** | **bool** | Whether reinstatement evidence has been supplied | 
**file_ids** | **list[float]** | Required if reinstatement_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**final_reinstatement** | **bool** | Whether it is a final reinstatement Required if reinstatement type is excavation | [optional] 
**number_of_holes** | **float** | Must be a number between 0 and 100 Required if reinstatement type is not excavation | [optional] 
**permit_reference_number** | **str** | Max length 100 characters | [optional] 
**response_to_remedial_works** | **bool** | Must be provided if base_courses_affected is provided | [optional] 
**base_courses_affected** | **bool** | Must be provided if response_to_remedial_works is provided | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

