# CommentCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**date_created_from** | **datetime** |  | [optional] 
**date_created_to** | **datetime** | Must occur after or on provided date_created_from | [optional] 
**topic** | [**list[CommentTopic]**](CommentTopic.md) |  | [optional] 
**is_internal** | **bool** |  | [optional] 
**is_read** | **bool** |  | [optional] 
**is_not_read** | **bool** |  | [optional] 
**work_reference_number** | **str** | Max length 100 characters | [optional] 
**author_email_address** | **str** | Max length 100 characters | [optional] 
**is_incoming** | **bool** |  | [optional] 
**is_outgoing** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

