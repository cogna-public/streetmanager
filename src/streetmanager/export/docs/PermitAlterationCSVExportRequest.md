# PermitAlterationCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**alteration_status** | [**list[AlterationStatus]**](AlterationStatus.md) |  | [optional] 
**alteration_type** | [**list[AlterationType]**](AlterationType.md) |  | [optional] 
**work_status** | [**list[WorkStatus]**](WorkStatus.md) |  | [optional] 
**work_category** | [**list[WorkCategory]**](WorkCategory.md) |  | [optional] 
**lane_rental_assessment_outcome** | [**list[LaneRentalAssessmentOutcome]**](LaneRentalAssessmentOutcome.md) |  | [optional] 
**start_date_created** | **datetime** |  | [optional] 
**end_date_created** | **datetime** | Must occur on or after the provided start_date_created | [optional] 
**is_traffic_sensitive** | **bool** |  | [optional] 
**is_high_impact_traffic_management** | **bool** |  | [optional] 
**is_duration_extension** | **bool** |  | [optional] 
**is_early_start** | **bool** |  | [optional] 
**is_deemed** | **bool** |  | [optional] 
**lane_rental_charges_not_agreed** | **bool** |  | [optional] 
**lane_rental_charges_potentially_apply** | **bool** |  | [optional] 
**status_update_date_from** | **datetime** |  | [optional] 
**status_update_date_to** | **datetime** | Must occur on or after the provided status_update_date_from | [optional] 
**permit_alteration_reference_number** | **str** | Max length 105 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

