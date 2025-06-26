# ReinstatementCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**status** | [**list[ReinstatementStatus]**](ReinstatementStatus.md) |  | [optional] 
**latest_reinstatements_only** | **bool** |  | [optional] 
**registration_date_from** | **datetime** |  | [optional] 
**registration_date_to** | **datetime** | Must occur on or after the provided registration_date_from | [optional] 
**end_date_from** | **datetime** |  | [optional] 
**end_date_to** | **datetime** | Must occur on or after the end_date_from | [optional] 
**work_reference_number** | **str** | Max length 100 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

