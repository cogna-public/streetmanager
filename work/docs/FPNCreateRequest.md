# FPNCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_user_identifier** | **str** | Max length 100 characters | [optional] 
**internal_user_name** | **str** | Max length 100 characters | [optional] 
**fpn_evidence** | **bool** | Whether FPN evidence has been supplied | 
**file_ids** | **list[float]** | Required if fpn_evidence &#x3D; true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide &gt; Works API &gt; File upload for more information | [optional] 
**offence_date** | **datetime** | offence_date must be in the past | 
**offence_code** | [**OffenceCode**](OffenceCode.md) |  | 
**offence_details** | **str** | Max length 500 characters | 
**authorised_officer** | **str** | Max length 100 characters | 
**officer_contact_details** | **str** | Max length 100 characters | 
**officer_address** | **str** | Max length 500 characters | 
**representations_contact** | **str** | Max length 100 characters | 
**representations_contact_address** | **str** | Max length 500 characters | 
**payment_methods** | [**list[PaymentMethod]**](PaymentMethod.md) |  | 
**permit_reference_number** | **str** | The permit_reference_number of the associated permit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

