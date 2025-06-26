# InspectionCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** | Must occur on or after the provided start_date | [optional] 
**inspection_type** | [**list[InspectionType]**](InspectionType.md) |  | [optional] 
**start_date_created** | **datetime** |  | [optional] 
**end_date_created** | **datetime** | Must occur or or after the provided start_date_created | [optional] 
**work_reference_number** | **str** | Max length 100 characters | [optional] 
**inspection_category** | [**list[InspectionCategory]**](InspectionCategory.md) |  | [optional] 
**inspection_outcome** | [**list[InspectionOutcome]**](InspectionOutcome.md) |  | [optional] 
**promoter_outcome_status** | [**list[PromoterInspectionOutcomeStatusType]**](PromoterInspectionOutcomeStatusType.md) |  | [optional] 
**ha_outcome_status** | [**list[HAInspectionOutcomeStatusType]**](HAInspectionOutcomeStatusType.md) |  | [optional] 
**is_auto_accepted** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

