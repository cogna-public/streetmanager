# FeesCSVExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Must be within 30 days of provided end_date Must be provided if end_date is provided | 
**end_date** | **datetime** | Must occur on or after the provided start_date | 
**swa_code** | **str** | Must be provided if user is a contractor Max length 4 characters | [optional] 
**fee_report_format** | **AllOfFeesCSVExportRequestFeeReportFormat** |  | 
**swa_code_filter** | **str** | Required if fee_report_format &#x3D; single_org_one_csv Max length 4 characters | [optional] 
**export_description** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

