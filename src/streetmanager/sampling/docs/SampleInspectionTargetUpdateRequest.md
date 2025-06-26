# SampleInspectionTargetUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 50 characters | [optional] 
**inspection_units_baseline** | **float** | Required if annual_inspection_units not provided Must be whole number | [optional] 
**annual_inspection_units** | [**list[AnnualInspectionUnitsSummary]**](AnnualInspectionUnitsSummary.md) | Required if inspection_units_baseline not provided | [optional] 
**inspection_rate** | **float** | Must be between 20 and 100 | 
**target_a** | **float** | Sum of target_a + target_b + target_c must not exceed the quarterly quota Must be whole number See API specification Resource Guide &gt; Sampling API &gt; Sample inspection quota for more information | 
**target_b** | **float** | Sum of target_a + target_b + target_c must not exceed the quarterly quota Must be whole number See API specification Resource Guide &gt; Sampling API &gt; Sample inspection quota for more information | 
**target_c** | **float** | Sum of target_a + target_b + target_c must not exceed the quarterly quota Must be whole number See API specification Resource Guide &gt; Sampling API &gt; Sample inspection quota for more information | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

