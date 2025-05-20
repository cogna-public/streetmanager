# PermitAlterationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permit_alteration_reference_number** | **str** |  | 
**date_created** | **datetime** |  | 
**deadline_date** | **datetime** |  | 
**alteration_status** | [**AlterationStatusResponse**](AlterationStatusResponse.md) |  | 
**alteration_status_string** | **str** |  | 
**alteration_type** | [**AlterationTypeResponse**](AlterationTypeResponse.md) |  | 
**alteration_type_string** | **str** |  | 
**permit_status** | **AllOfPermitAlterationResponsePermitStatus** |  | [optional] 
**permit_status_string** | **str** |  | [optional] 
**assessment_discount** | **float** |  | [optional] 
**assessment_comments** | **str** |  | [optional] 
**permit_alteration_reason** | **str** |  | 
**original** | [**PermitResponse**](PermitResponse.md) |  | 
**proposed** | [**PermitResponse**](PermitResponse.md) |  | 
**duration_challenge_review_status** | **AllOfPermitAlterationResponseDurationChallengeReviewStatus** |  | [optional] 
**duration_challenge_review_status_string** | **str** |  | [optional] 
**duration_challenge_reason_for_non_acceptance** | **str** |  | [optional] 
**duration_challenge_review_update_date** | **datetime** |  | [optional] 
**duration_challenge_non_acceptance_response_status** | **AllOfPermitAlterationResponseDurationChallengeNonAcceptanceResponseStatus** |  | [optional] 
**duration_challenge_non_acceptance_response_status_string** | **str** |  | [optional] 
**duration_challenge_non_acceptance_response_details** | **str** |  | [optional] 
**duration_challenge_non_acceptance_response_update_date** | **datetime** |  | [optional] 
**duration_challenge_non_acceptance_response_new_reasonable_period_end_date** | **datetime** |  | [optional] 
**duration_challenge_non_acceptance_response_old_reasonable_period_end_date** | **datetime** |  | [optional] 
**duration_challenge_follow_up_review_complete** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

