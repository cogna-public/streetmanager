# PermitLaneRentalAssessmentUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**outcome** | [**LaneRentalAssessmentOutcome**](LaneRentalAssessmentOutcome.md) |  | 
**additional_details** | **str** | Max length 500 characters | [optional] 
**charge_band** | **AllOfPermitLaneRentalAssessmentUpdateRequestChargeBand** |  | [optional] 
**chargeable_days** | **float** | Whole number between 1 and 10000 | [optional] 
**charges_agreed** | **bool** | Required if outcome &#x3D; &#x27;chargeable&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

