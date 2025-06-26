# Section58CSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**ha_organisation_name** | **str** |  | [optional] 
**start_date_from** | **datetime** |  | [optional] 
**start_date_to** | **datetime** | Must occur on or after the provided start_date_from | [optional] 
**section_58_status** | [**list[Section58Status]**](Section58Status.md) |  | [optional] 
**section_58_reference_number** | **str** | Max length 100 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

