# InterestedPartyPermitsCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**permit_reference_number** | **str** | Max length 100 characters | [optional] 
**work_reference_number** | **str** | Max length 100 characters | [optional] 
**work_start_date_from** | **datetime** |  | [optional] 
**work_start_date_to** | **datetime** | Must occur on or after work_start_date_from | [optional] 
**work_end_date_from** | **datetime** |  | [optional] 
**work_end_date_to** | **datetime** | Must occur on or after work_end_date_from | [optional] 
**start_date_created** | **datetime** |  | [optional] 
**end_date_created** | **datetime** | Must occur on or after start_date_created | [optional] 
**work_status** | [**list[WorkStatus]**](WorkStatus.md) |  | [optional] 
**work_category** | [**list[WorkCategory]**](WorkCategory.md) |  | [optional] 
**is_high_impact_traffic_management** | **bool** |  | [optional] 
**promoter_organisation_name** | **str** | Max length 100 characters | [optional] 
**ha_organisation_name** | **str** | Max length 100 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

