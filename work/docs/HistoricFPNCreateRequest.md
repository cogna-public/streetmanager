# HistoricFPNCreateRequest

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
**historical_permit_reference** | **str** | Max length 24 characters Must be unique in the system, this will become the work_reference_number Must contain only alphanumeric characters, dashes and underscores | 
**works_location_description** | **str** | Max length 500 characters | 
**description_of_work** | **str** | Max length 500 characters | [optional] 
**work_start_date** | **datetime** | Date must be in the past | [optional] 
**work_end_date** | **datetime** | Date must be in the past work_end_date must be after the date and time for work_start_date | [optional] 
**fpn_evidence** | **bool** | Whether FPN evidence has been supplied | 
**file_ids** | **list[float]** | Required if fpn_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**offence_date** | **datetime** | offence_date must be in the past | 
**offence_code** | [**OffenceCode**](OffenceCode.md) |  | 
**offence_details** | **str** | Max length 500 characters | 
**authorised_officer** | **str** | Max length 100 characters | 
**officer_contact_details** | **str** | Max length 100 characters | 
**officer_address** | **str** | Max length 500 characters | 
**representations_contact** | **str** | Max length 100 characters | 
**representations_contact_address** | **str** | Max length 500 characters | 
**payment_methods** | [**list[PaymentMethod]**](PaymentMethod.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

