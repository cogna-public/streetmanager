# CreateAncillaryInfoRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**location_description** | **str** | Max length 500 characters Must be provided if ancillary_info_type is anything other than portable_traffic_signals_or_other_traffic_controls | [optional] 
**ancillary_info_description** | **str** | Max length 500 characters | 
**ancillary_info_coordinates** | **list[object]** | Array values must be unique Each point must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point Max length of 10 | 
**usrns** | **list[float]** | Array values must be unique Is whole number between 1000001 and 99999999 inclusive See business rules section 1.4 - USRN Max length of 25 | 
**ancillary_info_type** | [**AncillaryInfoType**](AncillaryInfoType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

