# coding: utf-8

"""
    Street Manager API

    See API specification Resource Guide > Work API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FeeMatrixResponse(object):
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
        'internal_user_identifier': 'str',
        'internal_user_name': 'str',
        'major_paa_fee_traffic_sensitive': 'float',
        'major_work_permit_fee_traffic_sensitive': 'float',
        'standard_works_permit_fee_traffic_sensitive': 'float',
        'minor_works_permit_fee_traffic_sensitive': 'float',
        'immediate_works_permit_fee_traffic_sensitive': 'float',
        'permit_variation_fee_traffic_sensitive': 'float',
        'major_paa_fee_non_traffic_sensitive': 'float',
        'major_work_permit_fee_non_traffic_sensitive': 'float',
        'standard_works_permit_fee_non_traffic_sensitive': 'float',
        'minor_works_permit_fee_non_traffic_sensitive': 'float',
        'immediate_works_permit_fee_non_traffic_sensitive': 'float',
        'permit_variation_fee_non_traffic_sensitive': 'float',
        'discount_guidance': 'str'
    }

    attribute_map = {
        'internal_user_identifier': 'internal_user_identifier',
        'internal_user_name': 'internal_user_name',
        'major_paa_fee_traffic_sensitive': 'major_paa_fee_traffic_sensitive',
        'major_work_permit_fee_traffic_sensitive': 'major_work_permit_fee_traffic_sensitive',
        'standard_works_permit_fee_traffic_sensitive': 'standard_works_permit_fee_traffic_sensitive',
        'minor_works_permit_fee_traffic_sensitive': 'minor_works_permit_fee_traffic_sensitive',
        'immediate_works_permit_fee_traffic_sensitive': 'immediate_works_permit_fee_traffic_sensitive',
        'permit_variation_fee_traffic_sensitive': 'permit_variation_fee_traffic_sensitive',
        'major_paa_fee_non_traffic_sensitive': 'major_paa_fee_non_traffic_sensitive',
        'major_work_permit_fee_non_traffic_sensitive': 'major_work_permit_fee_non_traffic_sensitive',
        'standard_works_permit_fee_non_traffic_sensitive': 'standard_works_permit_fee_non_traffic_sensitive',
        'minor_works_permit_fee_non_traffic_sensitive': 'minor_works_permit_fee_non_traffic_sensitive',
        'immediate_works_permit_fee_non_traffic_sensitive': 'immediate_works_permit_fee_non_traffic_sensitive',
        'permit_variation_fee_non_traffic_sensitive': 'permit_variation_fee_non_traffic_sensitive',
        'discount_guidance': 'discount_guidance'
    }

    def __init__(self, internal_user_identifier=None, internal_user_name=None, major_paa_fee_traffic_sensitive=None, major_work_permit_fee_traffic_sensitive=None, standard_works_permit_fee_traffic_sensitive=None, minor_works_permit_fee_traffic_sensitive=None, immediate_works_permit_fee_traffic_sensitive=None, permit_variation_fee_traffic_sensitive=None, major_paa_fee_non_traffic_sensitive=None, major_work_permit_fee_non_traffic_sensitive=None, standard_works_permit_fee_non_traffic_sensitive=None, minor_works_permit_fee_non_traffic_sensitive=None, immediate_works_permit_fee_non_traffic_sensitive=None, permit_variation_fee_non_traffic_sensitive=None, discount_guidance=None):  # noqa: E501
        """FeeMatrixResponse - a model defined in Swagger"""  # noqa: E501
        self._internal_user_identifier = None
        self._internal_user_name = None
        self._major_paa_fee_traffic_sensitive = None
        self._major_work_permit_fee_traffic_sensitive = None
        self._standard_works_permit_fee_traffic_sensitive = None
        self._minor_works_permit_fee_traffic_sensitive = None
        self._immediate_works_permit_fee_traffic_sensitive = None
        self._permit_variation_fee_traffic_sensitive = None
        self._major_paa_fee_non_traffic_sensitive = None
        self._major_work_permit_fee_non_traffic_sensitive = None
        self._standard_works_permit_fee_non_traffic_sensitive = None
        self._minor_works_permit_fee_non_traffic_sensitive = None
        self._immediate_works_permit_fee_non_traffic_sensitive = None
        self._permit_variation_fee_non_traffic_sensitive = None
        self._discount_guidance = None
        self.discriminator = None
        if internal_user_identifier is not None:
            self.internal_user_identifier = internal_user_identifier
        if internal_user_name is not None:
            self.internal_user_name = internal_user_name
        self.major_paa_fee_traffic_sensitive = major_paa_fee_traffic_sensitive
        self.major_work_permit_fee_traffic_sensitive = major_work_permit_fee_traffic_sensitive
        self.standard_works_permit_fee_traffic_sensitive = standard_works_permit_fee_traffic_sensitive
        self.minor_works_permit_fee_traffic_sensitive = minor_works_permit_fee_traffic_sensitive
        self.immediate_works_permit_fee_traffic_sensitive = immediate_works_permit_fee_traffic_sensitive
        self.permit_variation_fee_traffic_sensitive = permit_variation_fee_traffic_sensitive
        self.major_paa_fee_non_traffic_sensitive = major_paa_fee_non_traffic_sensitive
        self.major_work_permit_fee_non_traffic_sensitive = major_work_permit_fee_non_traffic_sensitive
        self.standard_works_permit_fee_non_traffic_sensitive = standard_works_permit_fee_non_traffic_sensitive
        self.minor_works_permit_fee_non_traffic_sensitive = minor_works_permit_fee_non_traffic_sensitive
        self.immediate_works_permit_fee_non_traffic_sensitive = immediate_works_permit_fee_non_traffic_sensitive
        self.permit_variation_fee_non_traffic_sensitive = permit_variation_fee_non_traffic_sensitive
        self.discount_guidance = discount_guidance

    @property
    def internal_user_identifier(self):
        """Gets the internal_user_identifier of this FeeMatrixResponse.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The internal_user_identifier of this FeeMatrixResponse.  # noqa: E501
        :rtype: str
        """
        return self._internal_user_identifier

    @internal_user_identifier.setter
    def internal_user_identifier(self, internal_user_identifier):
        """Sets the internal_user_identifier of this FeeMatrixResponse.

        Max length 100 characters  # noqa: E501

        :param internal_user_identifier: The internal_user_identifier of this FeeMatrixResponse.  # noqa: E501
        :type: str
        """

        self._internal_user_identifier = internal_user_identifier

    @property
    def internal_user_name(self):
        """Gets the internal_user_name of this FeeMatrixResponse.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The internal_user_name of this FeeMatrixResponse.  # noqa: E501
        :rtype: str
        """
        return self._internal_user_name

    @internal_user_name.setter
    def internal_user_name(self, internal_user_name):
        """Sets the internal_user_name of this FeeMatrixResponse.

        Max length 100 characters  # noqa: E501

        :param internal_user_name: The internal_user_name of this FeeMatrixResponse.  # noqa: E501
        :type: str
        """

        self._internal_user_name = internal_user_name

    @property
    def major_paa_fee_traffic_sensitive(self):
        """Gets the major_paa_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The major_paa_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._major_paa_fee_traffic_sensitive

    @major_paa_fee_traffic_sensitive.setter
    def major_paa_fee_traffic_sensitive(self, major_paa_fee_traffic_sensitive):
        """Sets the major_paa_fee_traffic_sensitive of this FeeMatrixResponse.


        :param major_paa_fee_traffic_sensitive: The major_paa_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if major_paa_fee_traffic_sensitive is None:
            raise ValueError("Invalid value for `major_paa_fee_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._major_paa_fee_traffic_sensitive = major_paa_fee_traffic_sensitive

    @property
    def major_work_permit_fee_traffic_sensitive(self):
        """Gets the major_work_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The major_work_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._major_work_permit_fee_traffic_sensitive

    @major_work_permit_fee_traffic_sensitive.setter
    def major_work_permit_fee_traffic_sensitive(self, major_work_permit_fee_traffic_sensitive):
        """Sets the major_work_permit_fee_traffic_sensitive of this FeeMatrixResponse.


        :param major_work_permit_fee_traffic_sensitive: The major_work_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if major_work_permit_fee_traffic_sensitive is None:
            raise ValueError("Invalid value for `major_work_permit_fee_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._major_work_permit_fee_traffic_sensitive = major_work_permit_fee_traffic_sensitive

    @property
    def standard_works_permit_fee_traffic_sensitive(self):
        """Gets the standard_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The standard_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._standard_works_permit_fee_traffic_sensitive

    @standard_works_permit_fee_traffic_sensitive.setter
    def standard_works_permit_fee_traffic_sensitive(self, standard_works_permit_fee_traffic_sensitive):
        """Sets the standard_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.


        :param standard_works_permit_fee_traffic_sensitive: The standard_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if standard_works_permit_fee_traffic_sensitive is None:
            raise ValueError("Invalid value for `standard_works_permit_fee_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._standard_works_permit_fee_traffic_sensitive = standard_works_permit_fee_traffic_sensitive

    @property
    def minor_works_permit_fee_traffic_sensitive(self):
        """Gets the minor_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The minor_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._minor_works_permit_fee_traffic_sensitive

    @minor_works_permit_fee_traffic_sensitive.setter
    def minor_works_permit_fee_traffic_sensitive(self, minor_works_permit_fee_traffic_sensitive):
        """Sets the minor_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.


        :param minor_works_permit_fee_traffic_sensitive: The minor_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if minor_works_permit_fee_traffic_sensitive is None:
            raise ValueError("Invalid value for `minor_works_permit_fee_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._minor_works_permit_fee_traffic_sensitive = minor_works_permit_fee_traffic_sensitive

    @property
    def immediate_works_permit_fee_traffic_sensitive(self):
        """Gets the immediate_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The immediate_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._immediate_works_permit_fee_traffic_sensitive

    @immediate_works_permit_fee_traffic_sensitive.setter
    def immediate_works_permit_fee_traffic_sensitive(self, immediate_works_permit_fee_traffic_sensitive):
        """Sets the immediate_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.


        :param immediate_works_permit_fee_traffic_sensitive: The immediate_works_permit_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if immediate_works_permit_fee_traffic_sensitive is None:
            raise ValueError("Invalid value for `immediate_works_permit_fee_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._immediate_works_permit_fee_traffic_sensitive = immediate_works_permit_fee_traffic_sensitive

    @property
    def permit_variation_fee_traffic_sensitive(self):
        """Gets the permit_variation_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The permit_variation_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._permit_variation_fee_traffic_sensitive

    @permit_variation_fee_traffic_sensitive.setter
    def permit_variation_fee_traffic_sensitive(self, permit_variation_fee_traffic_sensitive):
        """Sets the permit_variation_fee_traffic_sensitive of this FeeMatrixResponse.


        :param permit_variation_fee_traffic_sensitive: The permit_variation_fee_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if permit_variation_fee_traffic_sensitive is None:
            raise ValueError("Invalid value for `permit_variation_fee_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._permit_variation_fee_traffic_sensitive = permit_variation_fee_traffic_sensitive

    @property
    def major_paa_fee_non_traffic_sensitive(self):
        """Gets the major_paa_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The major_paa_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._major_paa_fee_non_traffic_sensitive

    @major_paa_fee_non_traffic_sensitive.setter
    def major_paa_fee_non_traffic_sensitive(self, major_paa_fee_non_traffic_sensitive):
        """Sets the major_paa_fee_non_traffic_sensitive of this FeeMatrixResponse.


        :param major_paa_fee_non_traffic_sensitive: The major_paa_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if major_paa_fee_non_traffic_sensitive is None:
            raise ValueError("Invalid value for `major_paa_fee_non_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._major_paa_fee_non_traffic_sensitive = major_paa_fee_non_traffic_sensitive

    @property
    def major_work_permit_fee_non_traffic_sensitive(self):
        """Gets the major_work_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The major_work_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._major_work_permit_fee_non_traffic_sensitive

    @major_work_permit_fee_non_traffic_sensitive.setter
    def major_work_permit_fee_non_traffic_sensitive(self, major_work_permit_fee_non_traffic_sensitive):
        """Sets the major_work_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.


        :param major_work_permit_fee_non_traffic_sensitive: The major_work_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if major_work_permit_fee_non_traffic_sensitive is None:
            raise ValueError("Invalid value for `major_work_permit_fee_non_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._major_work_permit_fee_non_traffic_sensitive = major_work_permit_fee_non_traffic_sensitive

    @property
    def standard_works_permit_fee_non_traffic_sensitive(self):
        """Gets the standard_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The standard_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._standard_works_permit_fee_non_traffic_sensitive

    @standard_works_permit_fee_non_traffic_sensitive.setter
    def standard_works_permit_fee_non_traffic_sensitive(self, standard_works_permit_fee_non_traffic_sensitive):
        """Sets the standard_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.


        :param standard_works_permit_fee_non_traffic_sensitive: The standard_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if standard_works_permit_fee_non_traffic_sensitive is None:
            raise ValueError("Invalid value for `standard_works_permit_fee_non_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._standard_works_permit_fee_non_traffic_sensitive = standard_works_permit_fee_non_traffic_sensitive

    @property
    def minor_works_permit_fee_non_traffic_sensitive(self):
        """Gets the minor_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The minor_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._minor_works_permit_fee_non_traffic_sensitive

    @minor_works_permit_fee_non_traffic_sensitive.setter
    def minor_works_permit_fee_non_traffic_sensitive(self, minor_works_permit_fee_non_traffic_sensitive):
        """Sets the minor_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.


        :param minor_works_permit_fee_non_traffic_sensitive: The minor_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if minor_works_permit_fee_non_traffic_sensitive is None:
            raise ValueError("Invalid value for `minor_works_permit_fee_non_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._minor_works_permit_fee_non_traffic_sensitive = minor_works_permit_fee_non_traffic_sensitive

    @property
    def immediate_works_permit_fee_non_traffic_sensitive(self):
        """Gets the immediate_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The immediate_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._immediate_works_permit_fee_non_traffic_sensitive

    @immediate_works_permit_fee_non_traffic_sensitive.setter
    def immediate_works_permit_fee_non_traffic_sensitive(self, immediate_works_permit_fee_non_traffic_sensitive):
        """Sets the immediate_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.


        :param immediate_works_permit_fee_non_traffic_sensitive: The immediate_works_permit_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if immediate_works_permit_fee_non_traffic_sensitive is None:
            raise ValueError("Invalid value for `immediate_works_permit_fee_non_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._immediate_works_permit_fee_non_traffic_sensitive = immediate_works_permit_fee_non_traffic_sensitive

    @property
    def permit_variation_fee_non_traffic_sensitive(self):
        """Gets the permit_variation_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501


        :return: The permit_variation_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :rtype: float
        """
        return self._permit_variation_fee_non_traffic_sensitive

    @permit_variation_fee_non_traffic_sensitive.setter
    def permit_variation_fee_non_traffic_sensitive(self, permit_variation_fee_non_traffic_sensitive):
        """Sets the permit_variation_fee_non_traffic_sensitive of this FeeMatrixResponse.


        :param permit_variation_fee_non_traffic_sensitive: The permit_variation_fee_non_traffic_sensitive of this FeeMatrixResponse.  # noqa: E501
        :type: float
        """
        if permit_variation_fee_non_traffic_sensitive is None:
            raise ValueError("Invalid value for `permit_variation_fee_non_traffic_sensitive`, must not be `None`")  # noqa: E501

        self._permit_variation_fee_non_traffic_sensitive = permit_variation_fee_non_traffic_sensitive

    @property
    def discount_guidance(self):
        """Gets the discount_guidance of this FeeMatrixResponse.  # noqa: E501

        Max length 500 characters  # noqa: E501

        :return: The discount_guidance of this FeeMatrixResponse.  # noqa: E501
        :rtype: str
        """
        return self._discount_guidance

    @discount_guidance.setter
    def discount_guidance(self, discount_guidance):
        """Sets the discount_guidance of this FeeMatrixResponse.

        Max length 500 characters  # noqa: E501

        :param discount_guidance: The discount_guidance of this FeeMatrixResponse.  # noqa: E501
        :type: str
        """
        if discount_guidance is None:
            raise ValueError("Invalid value for `discount_guidance`, must not be `None`")  # noqa: E501

        self._discount_guidance = discount_guidance

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
        if issubclass(FeeMatrixResponse, dict):
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
        if not isinstance(other, FeeMatrixResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
