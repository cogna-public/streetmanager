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

class FinalReinstatementUpdateRequest(object):
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
        'final_reinstatement': 'bool'
    }

    attribute_map = {
        'internal_user_identifier': 'internal_user_identifier',
        'internal_user_name': 'internal_user_name',
        'final_reinstatement': 'final_reinstatement'
    }

    def __init__(self, internal_user_identifier=None, internal_user_name=None, final_reinstatement=None):  # noqa: E501
        """FinalReinstatementUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._internal_user_identifier = None
        self._internal_user_name = None
        self._final_reinstatement = None
        self.discriminator = None
        if internal_user_identifier is not None:
            self.internal_user_identifier = internal_user_identifier
        if internal_user_name is not None:
            self.internal_user_name = internal_user_name
        self.final_reinstatement = final_reinstatement

    @property
    def internal_user_identifier(self):
        """Gets the internal_user_identifier of this FinalReinstatementUpdateRequest.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The internal_user_identifier of this FinalReinstatementUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_user_identifier

    @internal_user_identifier.setter
    def internal_user_identifier(self, internal_user_identifier):
        """Sets the internal_user_identifier of this FinalReinstatementUpdateRequest.

        Max length 100 characters  # noqa: E501

        :param internal_user_identifier: The internal_user_identifier of this FinalReinstatementUpdateRequest.  # noqa: E501
        :type: str
        """

        self._internal_user_identifier = internal_user_identifier

    @property
    def internal_user_name(self):
        """Gets the internal_user_name of this FinalReinstatementUpdateRequest.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The internal_user_name of this FinalReinstatementUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_user_name

    @internal_user_name.setter
    def internal_user_name(self, internal_user_name):
        """Sets the internal_user_name of this FinalReinstatementUpdateRequest.

        Max length 100 characters  # noqa: E501

        :param internal_user_name: The internal_user_name of this FinalReinstatementUpdateRequest.  # noqa: E501
        :type: str
        """

        self._internal_user_name = internal_user_name

    @property
    def final_reinstatement(self):
        """Gets the final_reinstatement of this FinalReinstatementUpdateRequest.  # noqa: E501

        Whether it is a final reinstatement Can only add final_reinstatement if there is an Excavation Site  # noqa: E501

        :return: The final_reinstatement of this FinalReinstatementUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._final_reinstatement

    @final_reinstatement.setter
    def final_reinstatement(self, final_reinstatement):
        """Sets the final_reinstatement of this FinalReinstatementUpdateRequest.

        Whether it is a final reinstatement Can only add final_reinstatement if there is an Excavation Site  # noqa: E501

        :param final_reinstatement: The final_reinstatement of this FinalReinstatementUpdateRequest.  # noqa: E501
        :type: bool
        """
        if final_reinstatement is None:
            raise ValueError("Invalid value for `final_reinstatement`, must not be `None`")  # noqa: E501

        self._final_reinstatement = final_reinstatement

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
        if issubclass(FinalReinstatementUpdateRequest, dict):
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
        if not isinstance(other, FinalReinstatementUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
