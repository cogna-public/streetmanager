# ForwardPlanResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_reference_number** | **str** |  | 
**forward_plan_reference_number** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**forward_plan_status** | [**ForwardPlanStatusResponse**](ForwardPlanStatusResponse.md) |  | 
**forward_plan_status_string** | **str** |  | 
**promoter_organisation** | **str** |  | 
**promoter_swa_code** | **str** |  | 
**promoter_contact_details** | **str** |  | 
**highway_authority** | **str** |  | 
**highway_authority_swa_code** | **str** |  | 
**workstream_prefix** | **str** |  | 
**works_coordinates** | **object** |  | 
**street_name** | **str** |  | 
**town** | **str** |  | [optional] 
**area_name** | **str** |  | [optional] 
**usrn** | **float** |  | 
**road_category** | **float** |  | 
**date_created** | **datetime** |  | 
**works_location_description** | **str** |  | 
**description_of_work** | **str** |  | 
**project_reference_number** | **str** |  | [optional] 
**traffic_management_type** | **AllOfForwardPlanResponseTrafficManagementType** |  | [optional] 
**traffic_management_type_string** | **str** |  | [optional] 
**additional_info** | **str** |  | [optional] 
**forward_plan_asds** | [**list[PermitASDResponse]**](PermitASDResponse.md) |  | [optional] 
**cancelled_reason** | **str** |  | [optional] 
**hs2_in_act_limits** | **bool** |  | [optional] 
**hs2_consultation_requested_response_date** | **datetime** |  | [optional] 
**hs2_highway_exemption** | **AllOfForwardPlanResponseHs2HighwayExemption** |  | [optional] 
**hs2_highway_exemption_string** | **str** |  | [optional] 
**hs2_works_type** | **AllOfForwardPlanResponseHs2WorksType** |  | [optional] 
**hs2_works_type_string** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

