# Section74CreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**permit_reference_number** | **str** |  | 
**location_description** | **str** | Max length 500 characters | 
**location_types** | [**list[LocationType]**](LocationType.md) | Array values must be unique | 
**inspection_date** | **datetime** | Date must be today or a date in the past | 
**overrun_warning_reasons** | [**list[OverrunWarningReason]**](OverrunWarningReason.md) | Array values must be unique | 
**overrun_warning_details** | **str** | Max length 500 characters | 
**officer_name** | **str** | Max length 100 characters | 
**officer_contact_details** | **str** | Max length 100 characters | 
**schedule_follow_up_inspection** | **bool** |  | 
**reinspection_date** | **datetime** | Date must occur today or a date in the future | [optional] 
**reinspection_date_time** | **datetime** | The date for reinspection_date_time must match the date for reinspection_date Time must occur today or a date in the future | [optional] 
**section_74_evidence** | **bool** |  | 
**file_ids** | **list[float]** | Required if section_74_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

