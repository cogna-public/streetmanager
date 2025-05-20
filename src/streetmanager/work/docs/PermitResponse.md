# PermitResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permit_reference_number** | **str** |  | 
**proposed_start_date** | **datetime** |  | 
**proposed_end_date** | **datetime** |  | 
**actual_start_date** | **datetime** |  | [optional] 
**actual_stop_date** | **datetime** |  | [optional] 
**permit_status** | [**PermitStatusResponse**](PermitStatusResponse.md) |  | 
**permit_status_string** | **str** |  | 
**work_category** | [**WorkCategoryResponseEnum**](WorkCategoryResponseEnum.md) |  | 
**work_category_string** | **str** |  | 
**work_reference_number** | **str** |  | 
**promoter_organisation** | **str** |  | 
**promoter_swa_code** | **str** |  | 
**promoter_contact_details** | **str** |  | 
**primary_contact** | **str** |  | [optional] 
**primary_contact_number** | **str** |  | [optional] 
**primary_contact_email** | **str** |  | [optional] 
**secondary_contact** | **str** |  | 
**secondary_contact_number** | **str** |  | 
**secondary_contact_email** | **str** |  | [optional] 
**proposed_start_time** | **datetime** |  | [optional] 
**proposed_end_time** | **datetime** |  | [optional] 
**reasonable_period_end_date** | **datetime** |  | 
**calendar_day_duration** | **float** |  | 
**working_day_duration** | **float** |  | 
**description_of_work** | **str** |  | 
**excavation** | **bool** |  | 
**project_reference_number** | **str** |  | [optional] 
**traffic_management_plan** | **bool** |  | 
**lane_rental_applicable** | **bool** |  | 
**permit_conditions** | [**list[PermitConditionResponse]**](PermitConditionResponse.md) |  | [optional] 
**street_name** | **str** |  | 
**town** | **str** |  | [optional] 
**area_name** | **str** |  | [optional] 
**usrn** | **float** |  | 
**highway_authority** | **str** |  | 
**highway_authority_swa_code** | **str** |  | 
**road_category** | **float** |  | 
**works_location_description** | **str** |  | 
**works_coordinates** | **object** |  | 
**collaborative_working** | **bool** |  | 
**collaboration_details** | **str** |  | [optional] 
**collaborative_works** | **str** |  | [optional] 
**date_created** | **datetime** |  | 
**date_modified** | **datetime** |  | 
**deadline_date** | **datetime** |  | 
**assessment_comments** | **str** |  | [optional] 
**reasons_for_refusal** | [**list[ReasonForRefusalResponse]**](ReasonForRefusalResponse.md) |  | [optional] 
**reasons_for_refusal_string** | **list[str]** |  | [optional] 
**activity_type** | [**ActivityTypeResponse**](ActivityTypeResponse.md) |  | 
**activity_type_string** | **str** |  | 
**traffic_management_type** | [**TrafficManagementTypeResponse**](TrafficManagementTypeResponse.md) |  | 
**traffic_management_type_string** | **str** |  | 
**application_type** | [**ApplicationTypeResponse**](ApplicationTypeResponse.md) |  | 
**application_type_string** | **str** |  | 
**collaboration_type** | **AllOfPermitResponseCollaborationType** |  | [optional] 
**collaboration_type_string** | **str** |  | [optional] 
**location_types** | [**list[LocationTypeResponse]**](LocationTypeResponse.md) |  | 
**location_types_string** | **list[str]** |  | 
**assessment_status** | **AllOfPermitResponseAssessmentStatus** |  | [optional] 
**assessment_status_string** | **str** |  | [optional] 
**files** | [**list[FileSummaryResponse]**](FileSummaryResponse.md) |  | [optional] 
**permit_asds** | [**list[PermitASDResponse]**](PermitASDResponse.md) |  | 
**permit_not_selected_asds** | [**list[PermitASDResponse]**](PermitASDResponse.md) |  | 
**assessment_discount** | **float** |  | [optional] 
**assessment_discount_reason** | **str** |  | [optional] 
**is_ttro_required** | **bool** |  | [optional] 
**immediate_risk** | **bool** |  | [optional] 
**is_early_start** | **bool** |  | 
**is_deemed** | **bool** |  | 
**early_start_pre_approval** | **bool** |  | [optional] 
**pre_approval_details** | **str** |  | [optional] 
**pre_approval_authoriser** | **str** |  | [optional] 
**early_start_reason** | **str** |  | [optional] 
**additional_info** | **str** |  | [optional] 
**permit_alterations** | [**list[PermitAlterationSummaryResponse]**](PermitAlterationSummaryResponse.md) |  | [optional] 
**work_type** | [**WorkTypeResponse**](WorkTypeResponse.md) |  | 
**work_type_string** | **str** |  | 
**revoke_reason** | **str** |  | [optional] 
**sliding_end_date_candidate** | **bool** |  | 
**validity_period_end_date** | **datetime** |  | 
**final_reinstatement** | **bool** |  | 
**workstream_prefix** | **str** |  | 
**close_footway** | [**CloseFootwayResponse**](CloseFootwayResponse.md) |  | 
**close_footway_string** | **str** |  | 
**lane_rental_assessment_outcome** | **AllOfPermitResponseLaneRentalAssessmentOutcome** |  | [optional] 
**lane_rental_assessment_outcome_string** | **str** |  | [optional] 
**lane_rental_assessment_additional_details** | **str** |  | [optional] 
**lane_rental_assessment_charge_band** | **AllOfPermitResponseLaneRentalAssessmentChargeBand** |  | [optional] 
**lane_rental_assessment_charge_band_string** | **str** |  | [optional] 
**lane_rental_assessment_chargeable_days** | **float** |  | [optional] 
**lane_rental_assessment_charges_agreed** | **bool** |  | [optional] 
**is_lane_rental** | **bool** |  | 
**pending_change_details** | **str** |  | [optional] 
**work_status** | [**WorkStatusResponse**](WorkStatusResponse.md) |  | 
**work_status_string** | **str** |  | 
**hs2_in_act_limits** | **bool** |  | [optional] 
**hs2_consultation_requested_response_date** | **datetime** |  | [optional] 
**hs2_highway_exemption** | **AllOfPermitResponseHs2HighwayExemption** |  | [optional] 
**hs2_highway_exemption_string** | **str** |  | [optional] 
**hs2_is_consultation** | **bool** |  | [optional] 
**hs2_is_consent** | **bool** |  | [optional] 
**hs2_highway_emails** | **list[str]** |  | [optional] 
**hs2_acknowledged** | **bool** |  | [optional] 
**hs2_acknowledged_date_time** | **datetime** |  | [optional] 
**additional_contact** | **str** |  | [optional] 
**additional_contact_number** | **str** |  | [optional] 
**additional_contact_email** | **str** |  | [optional] 
**ever_modification_requested** | **bool** |  | 
**is_duration_challenged** | **bool** |  | [optional] 
**is_covid_19_response** | **bool** |  | [optional] 
**hs2_additional_usrns** | **list[float]** |  | [optional] 
**excavation_carried_out** | **bool** |  | 
**linked_section_81** | **AllOfPermitResponseLinkedSection81** |  | [optional] 
**duration_challenge_review_status** | **AllOfPermitResponseDurationChallengeReviewStatus** |  | [optional] 
**duration_challenge_review_status_string** | **str** |  | [optional] 
**duration_challenge_reason_for_non_acceptance** | **str** |  | [optional] 
**duration_challenge_review_update_date** | **datetime** |  | [optional] 
**duration_challenge_non_acceptance_response_status** | **AllOfPermitResponseDurationChallengeNonAcceptanceResponseStatus** |  | [optional] 
**duration_challenge_non_acceptance_response_status_string** | **str** |  | [optional] 
**duration_challenge_non_acceptance_response_details** | **str** |  | [optional] 
**duration_challenge_non_acceptance_response_update_date** | **datetime** |  | [optional] 
**duration_challenge_non_acceptance_response_new_reasonable_period_end_date** | **datetime** |  | [optional] 
**duration_challenge_non_acceptance_response_old_reasonable_period_end_date** | **datetime** |  | [optional] 
**duration_challenge_follow_up_review_complete** | **bool** |  | [optional] 
**emergency_contact_name** | **str** |  | [optional] 
**emergency_contact_number** | **str** |  | [optional] 
**current_traffic_management_type** | **AllOfPermitResponseCurrentTrafficManagementType** |  | [optional] 
**current_traffic_management_type_string** | **str** |  | [optional] 
**current_traffic_management_update_date** | **datetime** |  | [optional] 
**current_traffic_management_emergency_contact_name** | **str** |  | [optional] 
**current_traffic_management_emergency_contact_number** | **str** |  | [optional] 
**close_footpath** | [**CloseFootpathResponse**](CloseFootpathResponse.md) |  | 
**close_footpath_string** | **str** |  | 
**ancillary_informations** | [**list[AncillaryInfoSummaryResponse]**](AncillaryInfoSummaryResponse.md) |  | [optional] 
**street_line** | **object** |  | [optional] 
**reinstatement_registration_due_date** | **datetime** |  | [optional] 
**usrn_contains_hazardous_material** | **bool** |  | [optional] 
**permit_cancellation_reason** | **AllOfPermitResponsePermitCancellationReason** |  | [optional] 
**permit_cancellation_reason_string** | **str** |  | [optional] 
**permit_cancellation_reason_other** | **str** |  | [optional] 
**interested_parties** | [**list[InterestedParty]**](InterestedParty.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

