# PermitAlterationCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**secondary_contact** | **str** | Max length 100 characters | 
**secondary_contact_number** | **str** | Max length 100 characters | 
**secondary_contact_email** | **str** | Max length 100 characters | [optional] 
**proposed_start_date** | **datetime** |  | 
**proposed_start_time** | **datetime** | Required if work_type is immediate proposed_start_time is required if proposed_start_date is in the past | [optional] 
**proposed_end_date** | **datetime** | proposed_end_date must be on or after proposed_start_date If work_type &#x3D; planned, the maximum date range between proposed_start_date and proposed_end_date is 5 years | 
**proposed_end_time** | **datetime** | proposed_end_time is required if proposed_end_date is in the past proposed_end_time must be after the date and time for proposed_start_time | [optional] 
**description_of_work** | **str** | Max length 500 characters | 
**excavation** | **bool** | Whether an excavation will be required | 
**project_reference_number** | **str** | Max length 100 characters | [optional] 
**traffic_management_plan** | **bool** |  | 
**lane_rental_applicable** | **bool** |  | 
**permit_conditions** | [**list[PermitCondition]**](PermitCondition.md) | Array values must be unique | [optional] 
**works_location_description** | **str** | Max length 500 characters | 
**works_coordinates** | **object** | Must be a GeoJSON geometry (using British National Grid easting and northing coordinate pairs) and must be a point, line string or polygon | [optional] 
**collaborative_working** | **bool** |  | 
**collaboration_details** | **str** | Required if collaborative_working &#x3D; true Max length 500 characters | [optional] 
**collaborative_works** | **str** | Optional but only saved if collaborative_working &#x3D; true Max length 500 characters Work Reference Number of collaborative works | [optional] 
**activity_type** | [**ActivityType**](ActivityType.md) |  | 
**traffic_management_type** | [**TrafficManagementType**](TrafficManagementType.md) |  | 
**application_type** | [**ApplicationType**](ApplicationType.md) |  | 
**collaboration_type** | **AllOfPermitAlterationCreateRequestCollaborationType** | Required if collaborative_working &#x3D; true | [optional] 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**early_start_pre_approval** | **bool** | See business rules section 3.4.6 - Early start | [optional] 
**pre_approval_details** | **str** | Required if early_start_pre_approval &#x3D; true Max length 500 characters | [optional] 
**pre_approval_authoriser** | **str** | Required if early_start_pre_approval &#x3D; true Max length 100 characters | [optional] 
**early_start_reason** | **str** | Required if early_start_pre_approval &#x3D; false Max length 500 characters | [optional] 
**work_type** | [**WorkType**](WorkType.md) |  | 
**is_ttro_required** | **bool** | Required when work_type is planned | [optional] 
**immediate_risk** | **bool** | Required when work_type is immediate | [optional] 
**file_ids** | **list[float]** | Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**additional_info** | **str** | Max length 500 characters | [optional] 
**close_footway** | [**CloseFootway**](CloseFootway.md) |  | 
**close_footpath** | [**CloseFootpath**](CloseFootpath.md) |  | 
**permit_asds** | [**list[PermitASD]**](PermitASD.md) |  | [optional] 
**additional_contact** | **str** | Max length 100 characters | [optional] 
**additional_contact_number** | **str** | Max length 100 characters | [optional] 
**additional_contact_email** | **str** | Max length 100 characters | [optional] 
**hs2_consultation_requested_response_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**hs2_highway_emails** | **list[str]** | Array Max length 2 items Array values must be valid email addresses Array values max length 100 characters | [optional] 
**emergency_contact_name** | **str** | Max length 100 characters Required if traffic_management_type &#x3D; &#x27;multi_way_signals&#x27; or &#x27;two_way_signals&#x27; | [optional] 
**emergency_contact_number** | **str** | Max length 100 characters Required if traffic_management_type &#x3D; &#x27;multi_way_signals&#x27; or &#x27;two_way_signals&#x27; | [optional] 
**permit_alteration_reason** | **str** | Max length 500 characters | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

