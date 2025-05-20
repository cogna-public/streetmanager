# Section74UpdatePromoterStatusRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**status** | [**Section74PromoterStatus**](Section74PromoterStatus.md) |  | 
**site_visited_date** | **datetime** | Required when status is site_visited_and_rectified Date must be today or a date in the past | [optional] 
**additional_details** | **str** | Max length 500 characters | [optional] 
**reason_for_dispute** | **str** | Required when status is warning_disputed. Max length 500 characters | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

