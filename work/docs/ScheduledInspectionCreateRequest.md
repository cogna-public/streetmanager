# ScheduledInspectionCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**scheduled_inspection_type** | [**InspectionType**](InspectionType.md) |  | 
**scheduled_inspection_category** | **AllOfScheduledInspectionCreateRequestScheduledInspectionCategory** | See business rules section 10.2 - Inspection types and categories | [optional] 
**scheduled_inspection_date** | **datetime** | Date must occur today or a date in the future | 
**scheduled_inspection_date_time** | **datetime** | The date for scheduled_inspection_date_time must match the date for scheduled_inspection_date Time must occur today or a date in the future | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

