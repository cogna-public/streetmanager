# NonComplianceCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_area_reference_number** | **list[str]** | Array values must be unique | [optional] 
**street_descriptor** | **str** | Max length 100 characters | [optional] 
**usrn** | **str** | Max length 100 characters | [optional] 
**swa_code** | **str** | Must be provided if user is a contractor Up to four digits | [optional] 
**export_description** | **str** | Max length 50 characters | [optional] 
**organisation** | **str** | Max length 100 characters | [optional] 
**non_compliance_reference_number** | **str** | Max length 106 characters | [optional] 
**non_compliance_status** | [**list[NonComplianceStatus]**](NonComplianceStatus.md) |  | [optional] 
**ha_response_status** | [**list[NonComplianceResponseStatus]**](NonComplianceResponseStatus.md) |  | [optional] 
**promoter_response_status** | [**list[NonComplianceResponseStatus]**](NonComplianceResponseStatus.md) |  | [optional] 
**non_compliance_date_created_from** | **datetime** |  | [optional] 
**non_compliance_date_created_to** | **datetime** | Must occur on or after non_compliance_date_created_from | [optional] 
**most_recent_inspection_type** | [**list[InspectionType]**](InspectionType.md) |  | [optional] 
**most_recent_inspection_outcome** | [**list[InspectionOutcome]**](InspectionOutcome.md) |  | [optional] 
**most_recent_inspection_promoter_response_status** | [**list[PromoterInspectionOutcomeStatusType]**](PromoterInspectionOutcomeStatusType.md) |  | [optional] 
**most_recent_inspection_ha_response_status** | [**list[HAInspectionOutcomeStatusType]**](HAInspectionOutcomeStatusType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

