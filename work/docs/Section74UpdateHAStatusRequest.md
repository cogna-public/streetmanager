# Section74UpdateHAStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**status** | [**Section74HAStatus**](Section74HAStatus.md) |  | 
**site_cleared_date** | **datetime** | Required when status is charges_ended Date must be today or a date in the past | [optional] 
**additional_details** | **str** | Required when status is status is withdrawn Max length 500 characters | [optional] 
**number_of_days_overrun** | **float** | Required when status is draft_invoice_issued or resolved Must be a positive whole number | [optional] 
**draft_invoice_amount** | **float** | Required when status is draft_invoice_issued. Must be positive number. Can contain decimals to two decimal places. | [optional] 
**draft_invoice_reference** | **str** | Optional. Valid when status is draft_invoice_issued. Max length 100 characters | [optional] 
**final_agreed_amount** | **float** | Required when status is resolved. Must be positive number. Can contain decimals to two decimal places. | [optional] 
**invoice_reference** | **str** | Optional. Valid when status is resolved. Max length 100 characters | [optional] 
**reason_for_dispute** | **str** | Required when status is warning_disputed. Max length 500 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

