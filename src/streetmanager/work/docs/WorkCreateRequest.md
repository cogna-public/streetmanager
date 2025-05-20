# WorkCreateRequest

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
**secondary_contact** | **str** | Max length 100 characters | 
**secondary_contact_number** | **str** | Max length 100 characters | 
**secondary_contact_email** | **str** | Max length 100 characters | [optional] 
**proposed_start_date** | **datetime** |  | 
**proposed_start_time** | **datetime** | proposed_start_time is required if proposed_start_date is in the past | [optional] 
**proposed_end_date** | **datetime** | proposed_end_date must be on or after proposed_start_date If work_type &#x3D; planned, the maximum date range between proposed_start_date and proposed_end_date is 5 years | 
**proposed_end_time** | **datetime** | proposed_end_time is required if proposed_end_date is in the past proposed_end_time must be after the date and time for proposed_start_time | [optional] 
**description_of_work** | **str** | Max length 500 characters | 
**excavation** | **bool** | Whether an excavation will be required | 
**project_reference_number** | **str** | Max length 100 characters | [optional] 
**traffic_management_plan** | **bool** |  | 
**lane_rental_applicable** | **bool** |  | 
**permit_conditions** | [**list[PermitCondition]**](PermitCondition.md) | Array values must be unique | [optional] 
**collaborative_working** | **bool** |  | 
**collaboration_details** | **str** | Required if collaborative_working &#x3D; true Max length 500 characters | [optional] 
**collaborative_works** | **str** | Optional but only saved if collaborative_working &#x3D; true Max length 500 characters Work Reference Number of collaborative works | [optional] 
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**traffic_management_type** | [**TrafficManagementType**](TrafficManagementType.md) |  | 
**application_type** | [**ApplicationType**](ApplicationType.md) |  | 
**collaboration_type** | **AllOfWorkCreateRequestCollaborationType** | Required if collaborative_working &#x3D; true | [optional] 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**file_ids** | **list[float]** | Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**permit_asds** | [**list[PermitASD]**](PermitASD.md) |  | [optional] 
**work_type** | [**WorkType**](WorkType.md) |  | 
**is_ttro_required** | **bool** | Required when work_type is planned | [optional] 
**immediate_risk** | **bool** | Required when work_type is immediate | [optional] 
**early_start_pre_approval** | **bool** | See business rules section 3.4.6 - Early start | [optional] 
**pre_approval_details** | **str** | Required if early_start_pre_approval &#x3D; true Max length 500 characters | [optional] 
**pre_approval_authoriser** | **str** | Required if early_start_pre_approval &#x3D; true Max length 100 characters | [optional] 
**early_start_reason** | **str** | Required if early_start_pre_approval &#x3D; false Max length 500 characters | [optional] 
**additional_info** | **str** | Max length 500 characters | [optional] 
**close_footway** | [**CloseFootway**](CloseFootway.md) |  | 
**close_footpath** | [**CloseFootpath**](CloseFootpath.md) |  | 
**works_location_description** | **str** | Max length 500 characters | 
**workstream_prefix** | **str** | Must consist of 3 positive whole numbers | [optional] 
**hs2_in_act_limits** | **bool** | Required if promoter_swa_code &#x3D; &#x27;7374&#x27; | [optional] 
**hs2_consultation_requested_response_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**hs2_highway_exemption** | **AllOfWorkCreateRequestHs2HighwayExemption** | Required if work_type &#x3D; &#x27;hs2_highway_works&#x27; and hs2_in_act_limits &#x3D; true | [optional] 
**hs2_highway_emails** | **list[str]** | Array Max length 2 items Array values must be valid email addresses Array values max length 100 characters | [optional] 
**additional_contact** | **str** | Max length 100 characters | [optional] 
**additional_contact_number** | **str** | Max length 100 characters | [optional] 
**additional_contact_email** | **str** | Max length 100 characters | [optional] 
**hs2_additional_usrns** | **list[float]** | Array max length 10 items Array values must be valid USRNs | [optional] 
**emergency_contact_name** | **str** | Max length 100 characters Required if traffic_management_type &#x3D; &#x27;multi_way_signals&#x27; or &#x27;two_way_signals&#x27; | [optional] 
**emergency_contact_number** | **str** | Max length 100 characters Required if traffic_management_type &#x3D; &#x27;multi_way_signals&#x27; or &#x27;two_way_signals&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

