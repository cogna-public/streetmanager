# OrganisationUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line_one** | **str** | Max length 255 characters Alphanumeric characters only | 
**address_line_two** | **str** | Max length 255 characters Alphanumeric characters only | [optional] 
**locality** | **str** | Max length 255 characters Alphanumeric characters only | [optional] 
**town** | **str** | Max length 255 characters Alphanumeric characters only | [optional] 
**postcode** | **str** | Max length 8 characters Alphanumeric characters only | 
**email** | **str** | Max length 320 characters Must be valid email | [optional] 
**phone_number** | **str** | Max length 20 characters | 
**primary_contact_name** | **str** | Max length 100 characters | 
**primary_contact_email** | **str** | Max length 100 characters Must be valid email | 
**primary_contact_number** | **str** | Max length 20 characters | 
**primary_admin_name** | **str** | Max length 100 characters | 
**primary_admin_email** | **str** | Max length 100 characters Must be valid email | 
**primary_admin_number** | **str** | Max length 20 characters | 
**industry_sector** | **AllOfOrganisationUpdateRequestIndustrySector** | Must be a valid IndustrySector Mandatory if organisation is PROMOTER or HIGHWAY AUTHORITY | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

