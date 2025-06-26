# PermitSummaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_reference_number** | **str** |  | 
**permit_reference_number** | **str** |  | 
**promoter_swa_code** | **str** |  | 
**promoter_organisation** | **str** |  | 
**highway_authority** | **str** |  | 
**works_coordinates** | **object** |  | 
**location_description** | **str** |  | 
**street** | **str** |  | 
**town** | **str** |  | 
**area** | **str** |  | 
**work_category** | [**WorkCategoryResponse**](WorkCategoryResponse.md) |  | 
**work_category_string** | **str** |  | 
**description_of_work** | **str** |  | 
**traffic_management_type** | [**TrafficManagementTypeResponse**](TrafficManagementTypeResponse.md) |  | 
**traffic_management_type_string** | **str** |  | 
**assessment_status** | **AllOfPermitSummaryResponseAssessmentStatus** |  | [optional] 
**assessment_status_string** | **str** |  | [optional] 
**proposed_start_date** | **datetime** |  | 
**proposed_end_date** | **datetime** |  | 
**proposed_start_time** | **datetime** |  | [optional] 
**proposed_end_time** | **datetime** |  | [optional] 
**actual_start_date** | **datetime** |  | [optional] 
**actual_end_date** | **datetime** |  | [optional] 
**status** | [**PermitStatusResponse**](PermitStatusResponse.md) |  | 
**status_string** | **str** |  | 
**work_status** | [**WorkStatusResponse**](WorkStatusResponse.md) |  | 
**work_status_string** | **str** |  | 
**deadline_date** | **datetime** |  | 
**date_created** | **datetime** |  | 
**status_changed_date** | **datetime** |  | 
**usrn** | **float** |  | 
**is_active_permit** | **bool** |  | 
**permit_conditions** | [**list[PermitCondition]**](PermitCondition.md) |  | [optional] 
**road_category** | **float** |  | 
**is_traffic_sensitive** | **bool** |  | 
**has_no_final_reinstatement** | **bool** |  | 
**is_deemed** | **bool** |  | 
**excavation_carried_out** | **bool** |  | 
**is_early_start** | **bool** |  | 
**is_high_impact_traffic_management** | **bool** |  | 
**is_lane_rental** | **bool** |  | 
**lane_rental_assessment_outcome** | **AllOfPermitSummaryResponseLaneRentalAssessmentOutcome** |  | [optional] 
**lane_rental_assessment_outcome_string** | **str** |  | [optional] 
**lane_rental_charges_not_agreed** | **bool** |  | 
**lane_rental_charges_potentially_apply** | **bool** |  | 
**paa_to_pa_deadline_date** | **datetime** |  | [optional] 
**activity_type** | [**ActivityTypeResponse**](ActivityTypeResponse.md) |  | 
**activity_type_string** | **str** |  | 
**reasonable_period_end_date** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

