# NonComplianceResponseStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**non_compliance_response_status** | [**NonComplianceResponseStatus**](NonComplianceResponseStatus.md) |  | 
**response_details** | **str** | Required when non_compliance_response_status &#x3D; &#x27;withdrawn&#x27;/&#x27;joint_site_meeting_not_needed&#x27; Max length 500 characters | [optional] 
**jsm_suggested_date** | **datetime** | Required if non_compliance_response_status &#x3D; &#x27;joint_site_meeting_suggested&#x27; Must be today or in the future | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

