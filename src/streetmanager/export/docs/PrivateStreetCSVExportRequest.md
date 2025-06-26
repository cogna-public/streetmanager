# PrivateStreetCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**private_street_reference_number** | **str** | Max length 100 characters | [optional] 
**start_date_from** | **datetime** |  | [optional] 
**start_date_to** | **datetime** | Must occur on or after start_date_from | [optional] 
**end_date_from** | **datetime** |  | [optional] 
**end_date_to** | **datetime** | Must occur on or after end_date_from | [optional] 
**date_created_from** | **datetime** |  | [optional] 
**date_created_to** | **datetime** | Must occur on or after date_created_from | [optional] 
**private_street_status** | [**list[PrivateStreetStatus]**](PrivateStreetStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

