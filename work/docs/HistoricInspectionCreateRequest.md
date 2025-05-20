# HistoricInspectionCreateRequest

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
**inspection_type** | [**InspectionType**](InspectionType.md) |  | 
**inspection_start_date** | **datetime** | inspection_start_date must be in the past | 
**inspection_category** | **AllOfHistoricInspectionCreateRequestInspectionCategory** | See business rules section 10.2 - Inspection types and categories | [optional] 
**inspection_outcome** | [**InspectionOutcome**](InspectionOutcome.md) |  | 
**failure_reason_details** | [**list[HistoricFailureReasonDetails]**](HistoricFailureReasonDetails.md) | See business rules section 10.3 - Inspection outcomes | [optional] 
**inspection_outcome_details** | **str** | Required if inspection_outcome &#x3D; unable_to_complete_inspection or non_compliant_with_conditions Max length 500 characters | [optional] 
**was_call_logged** | **bool** | Required if inspection_outcome &#x3D; failed_high and inspection_type &#x3D; live_site | [optional] 
**call_logged_to** | **str** | Required if was_call_logged &#x3D; true Max length 100 characters | [optional] 
**call_logged_reference** | **str** | Required if was_call_logged &#x3D; true Max length 100 characters | [optional] 
**call_logged_summary** | **str** | Required if was_call_logged &#x3D; true Max length 500 characters | [optional] 
**defect_fixed_on_site** | **AllOfHistoricInspectionCreateRequestDefectFixedOnSite** | Required if inspection_outcome &#x3D; failed_high and inspection_type &#x3D; live_site | [optional] 
**additional_comments** | **str** | Max length 500 characters | [optional] 
**inspection_evidence** | **bool** |  | 
**file_ids** | **list[float]** | Required if inspection_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**reinspection_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**reinspection_date_time** | **datetime** | The date for reinspection_date_time must match the date for reinspection_date Time must occur today or a date in the future | [optional] 
**reinspection_type** | **AllOfHistoricInspectionCreateRequestReinspectionType** | Defaulted to inspection_type value if this and/or reinspection_category are not provided and reinspection_date is provided | [optional] 
**reinspection_category** | **AllOfHistoricInspectionCreateRequestReinspectionCategory** | See business rules section 10.2 - Inspection types and categories Defaulted to inspection_category value if this and/or reinspection_type are not provided and reinspection_date is provided | [optional] 
**username** | **str** | Max length 100 characters Should be populated with the user creating the inspection | 
**inspector_name** | **str** | Max length 100 characters | [optional] 
**made_safe_by_ha** | **bool** | Required if inspection_type &#x3D; section 81 and inspection_outcome &#x3D; Failed - high or Failed - low | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

