# coding: utf-8

"""
    Street Manager Party API

    See API specification Resource Guide > Party API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateOrganisationFpnDetailsRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'authorised_officer_name': 'str',
        'payment_methods': 'list[PaymentMethod]',
        'authorised_officer_contact_details': 'str',
        'authorised_officer_address': 'str',
        'representations_contact_details': 'str',
        'representations_contact_address': 'str'
    }

    attribute_map = {
        'authorised_officer_name': 'authorised_officer_name',
        'payment_methods': 'payment_methods',
        'authorised_officer_contact_details': 'authorised_officer_contact_details',
        'authorised_officer_address': 'authorised_officer_address',
        'representations_contact_details': 'representations_contact_details',
        'representations_contact_address': 'representations_contact_address'
    }

    def __init__(self, authorised_officer_name=None, payment_methods=None, authorised_officer_contact_details=None, authorised_officer_address=None, representations_contact_details=None, representations_contact_address=None):  # noqa: E501
        """UpdateOrganisationFpnDetailsRequest - a model defined in Swagger"""  # noqa: E501
        self._authorised_officer_name = None
        self._payment_methods = None
        self._authorised_officer_contact_details = None
        self._authorised_officer_address = None
        self._representations_contact_details = None
        self._representations_contact_address = None
        self.discriminator = None
        self.authorised_officer_name = authorised_officer_name
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if authorised_officer_contact_details is not None:
            self.authorised_officer_contact_details = authorised_officer_contact_details
        if authorised_officer_address is not None:
            self.authorised_officer_address = authorised_officer_address
        if representations_contact_details is not None:
            self.representations_contact_details = representations_contact_details
        if representations_contact_address is not None:
            self.representations_contact_address = representations_contact_address

    @property
    def authorised_officer_name(self):
        """Gets the authorised_officer_name of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501


        :return: The authorised_officer_name of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorised_officer_name

    @authorised_officer_name.setter
    def authorised_officer_name(self, authorised_officer_name):
        """Sets the authorised_officer_name of this UpdateOrganisationFpnDetailsRequest.


        :param authorised_officer_name: The authorised_officer_name of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :type: str
        """
        if authorised_officer_name is None:
            raise ValueError("Invalid value for `authorised_officer_name`, must not be `None`")  # noqa: E501

        self._authorised_officer_name = authorised_officer_name

    @property
    def payment_methods(self):
        """Gets the payment_methods of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501


        :return: The payment_methods of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :rtype: list[PaymentMethod]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this UpdateOrganisationFpnDetailsRequest.


        :param payment_methods: The payment_methods of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :type: list[PaymentMethod]
        """

        self._payment_methods = payment_methods

    @property
    def authorised_officer_contact_details(self):
        """Gets the authorised_officer_contact_details of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501


        :return: The authorised_officer_contact_details of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorised_officer_contact_details

    @authorised_officer_contact_details.setter
    def authorised_officer_contact_details(self, authorised_officer_contact_details):
        """Sets the authorised_officer_contact_details of this UpdateOrganisationFpnDetailsRequest.


        :param authorised_officer_contact_details: The authorised_officer_contact_details of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :type: str
        """

        self._authorised_officer_contact_details = authorised_officer_contact_details

    @property
    def authorised_officer_address(self):
        """Gets the authorised_officer_address of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501


        :return: The authorised_officer_address of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorised_officer_address

    @authorised_officer_address.setter
    def authorised_officer_address(self, authorised_officer_address):
        """Sets the authorised_officer_address of this UpdateOrganisationFpnDetailsRequest.


        :param authorised_officer_address: The authorised_officer_address of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :type: str
        """

        self._authorised_officer_address = authorised_officer_address

    @property
    def representations_contact_details(self):
        """Gets the representations_contact_details of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501


        :return: The representations_contact_details of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._representations_contact_details

    @representations_contact_details.setter
    def representations_contact_details(self, representations_contact_details):
        """Sets the representations_contact_details of this UpdateOrganisationFpnDetailsRequest.


        :param representations_contact_details: The representations_contact_details of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :type: str
        """

        self._representations_contact_details = representations_contact_details

    @property
    def representations_contact_address(self):
        """Gets the representations_contact_address of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501


        :return: The representations_contact_address of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._representations_contact_address

    @representations_contact_address.setter
    def representations_contact_address(self, representations_contact_address):
        """Sets the representations_contact_address of this UpdateOrganisationFpnDetailsRequest.


        :param representations_contact_address: The representations_contact_address of this UpdateOrganisationFpnDetailsRequest.  # noqa: E501
        :type: str
        """

        self._representations_contact_address = representations_contact_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateOrganisationFpnDetailsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateOrganisationFpnDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
