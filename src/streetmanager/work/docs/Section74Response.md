# Section74Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permit_reference_number** | **str** |  | 
**section_74_reference_number** | **str** |  | 
**date_created** | **datetime** |  | 
**overrun_warning_reasons** | [**list[OverrunWarningReasonResponse]**](OverrunWarningReasonResponse.md) |  | 
**overrun_warning_reasons_string** | **list[str]** |  | 
**ha_status** | [**Section74HAStatusResponse**](Section74HAStatusResponse.md) |  | 
**ha_status_string** | **str** |  | 
**location_description** | **str** |  | 
**location_types** | [**list[LocationTypeResponse]**](LocationTypeResponse.md) |  | 
**location_types_string** | **list[str]** |  | 
**inspection_date** | **datetime** |  | 
**overrun_warning_details** | **str** |  | 
**officer_name** | **str** |  | 
**officer_contact_details** | **str** |  | 
**section_74_evidence** | **bool** |  | 
**files** | [**list[FileSummaryResponse]**](FileSummaryResponse.md) |  | [optional] 
**latest_ha_response_date** | **datetime** |  | [optional] 
**latest_promoter_response_date** | **datetime** |  | [optional] 
**latest_ha_additional_details** | **str** |  | [optional] 
**latest_promoter_additional_details** | **str** |  | [optional] 
**ha_reason_for_dispute** | **str** |  | [optional] 
**promoter_reason_for_dispute** | **str** |  | [optional] 
**site_visited_date** | **datetime** |  | [optional] 
**site_cleared_date** | **datetime** |  | [optional] 
**ha_response_number_of_days_overrun** | **float** |  | [optional] 
**draft_invoice_reference** | **str** |  | [optional] 
**invoice_reference** | **str** |  | [optional] 
**draft_invoice_amount** | **float** |  | [optional] 
**final_agreed_amount** | **float** |  | [optional] 
**promoter_status** | **AllOfSection74ResponsePromoterStatus** |  | [optional] 
**promoter_status_string** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

