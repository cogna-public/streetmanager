# FPNCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**status** | [**list[FPNStatus]**](FPNStatus.md) |  | [optional] 
**start_date** | **datetime** | start_date must be before or the same as end_date if both are provided | [optional] 
**end_date** | **datetime** | end_date must be the same as or after start_date if both are provided | [optional] 
**offence_code** | [**list[OffenceCode]**](OffenceCode.md) |  | [optional] 
**status_changed_date_from** | **datetime** | status_changed_date_from must be before or the same as status_changed_date_to if both are provided | [optional] 
**status_changed_date_to** | **datetime** | end_date must be the same as or after status_changed_date_from if both are provided | [optional] 
**work_reference_number** | **str** | Max length 100 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

