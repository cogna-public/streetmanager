# WorkResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_reference_number** | **str** |  | 
**workstream_prefix** | **str** |  | 
**promoter_swa_code** | **str** |  | 
**promoter_organisation** | **str** |  | 
**promoter_organisation_industry_type** | **AllOfWorkResponsePromoterOrganisationIndustryType** |  | [optional] 
**promoter_organisation_industry_type_string** | **str** |  | [optional] 
**highway_authority_swa_code** | **str** |  | 
**highway_authority** | **str** |  | 
**street_name** | **str** |  | 
**town** | **str** |  | [optional] 
**area_name** | **str** |  | [optional] 
**road_category** | **float** |  | 
**works_coordinates** | **object** |  | 
**usrn** | **float** |  | 
**inspection_units** | **float** |  | [optional] 
**work_status** | [**WorkStatusResponse**](WorkStatusResponse.md) |  | 
**work_status_string** | **str** |  | 
**works_location_description** | **str** |  | 
**work_start_date** | **datetime** |  | [optional] 
**work_end_date** | **datetime** |  | [optional] 
**work_start_time** | **datetime** |  | [optional] 
**work_end_time** | **datetime** |  | [optional] 
**description_of_work** | **str** |  | [optional] 
**active_permit** | **AllOfWorkResponseActivePermit** |  | [optional] 
**forward_plan** | **AllOfWorkResponseForwardPlan** |  | [optional] 
**permits** | [**list[PermitSummaryResponse]**](PermitSummaryResponse.md) |  | [optional] 
**history** | [**list[WorkHistorySummaryResponse]**](WorkHistorySummaryResponse.md) |  | 
**sites** | [**list[SiteSummaryResponse]**](SiteSummaryResponse.md) |  | [optional] 
**inspections** | [**list[InspectionSummaryResponse]**](InspectionSummaryResponse.md) |  | [optional] 
**fpns** | [**list[FPNSummaryResponse]**](FPNSummaryResponse.md) |  | [optional] 
**section_81** | **AllOfWorkResponseSection81** |  | [optional] 
**files** | [**list[FileResponse]**](FileResponse.md) |  | [optional] 
**pbi_sample_inspections** | [**list[PbiSampleInspectionSummaryResponse]**](PbiSampleInspectionSummaryResponse.md) |  | [optional] 
**number_of_sites** | **float** |  | [optional] 
**section74s** | [**list[Section74SummaryResponse]**](Section74SummaryResponse.md) |  | [optional] 
**street_line** | **object** |  | [optional] 
**private_street_notice** | **AllOfWorkResponsePrivateStreetNotice** |  | [optional] 
**non_compliances** | [**list[NonComplianceSummaryResponse]**](NonComplianceSummaryResponse.md) |  | [optional] 
**latest_comments** | [**list[CommentResponse]**](CommentResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

