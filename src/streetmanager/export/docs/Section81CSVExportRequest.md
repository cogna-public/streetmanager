# Section81CSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**status** | [**list[Section81Status]**](Section81Status.md) |  | [optional] 
**severity** | [**list[Section81Severity]**](Section81Severity.md) |  | [optional] 
**issue_date_from** | **datetime** |  | [optional] 
**issue_date_to** | **datetime** | Must occur on or after the provided issue_date_from | [optional] 
**status_changed_date_from** | **datetime** |  | [optional] 
**status_changed_date_to** | **datetime** | Must occur on or after the provided status_changed_date_from | [optional] 
**type** | [**list[Section81Type]**](Section81Type.md) |  | [optional] 
**section_81_reference_number** | **str** | Max length 100 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

