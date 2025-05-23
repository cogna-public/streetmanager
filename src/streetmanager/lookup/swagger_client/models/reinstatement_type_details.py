# coding: utf-8

"""
    Street Manager Street Lookup API

    See API specification Resource Guide > Street Lookup API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReinstatementTypeDetails(object):
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
        'reinstatement_type_code': 'ReinstatementTypeCodeResponse',
        'reinstatement_type_code_string': 'str',
        'reinstatement_type_location_text': 'str'
    }

    attribute_map = {
        'reinstatement_type_code': 'reinstatement_type_code',
        'reinstatement_type_code_string': 'reinstatement_type_code_string',
        'reinstatement_type_location_text': 'reinstatement_type_location_text'
    }

    def __init__(self, reinstatement_type_code=None, reinstatement_type_code_string=None, reinstatement_type_location_text=None):  # noqa: E501
        """ReinstatementTypeDetails - a model defined in Swagger"""  # noqa: E501
        self._reinstatement_type_code = None
        self._reinstatement_type_code_string = None
        self._reinstatement_type_location_text = None
        self.discriminator = None
        self.reinstatement_type_code = reinstatement_type_code
        self.reinstatement_type_code_string = reinstatement_type_code_string
        if reinstatement_type_location_text is not None:
            self.reinstatement_type_location_text = reinstatement_type_location_text

    @property
    def reinstatement_type_code(self):
        """Gets the reinstatement_type_code of this ReinstatementTypeDetails.  # noqa: E501


        :return: The reinstatement_type_code of this ReinstatementTypeDetails.  # noqa: E501
        :rtype: ReinstatementTypeCodeResponse
        """
        return self._reinstatement_type_code

    @reinstatement_type_code.setter
    def reinstatement_type_code(self, reinstatement_type_code):
        """Sets the reinstatement_type_code of this ReinstatementTypeDetails.


        :param reinstatement_type_code: The reinstatement_type_code of this ReinstatementTypeDetails.  # noqa: E501
        :type: ReinstatementTypeCodeResponse
        """
        if reinstatement_type_code is None:
            raise ValueError("Invalid value for `reinstatement_type_code`, must not be `None`")  # noqa: E501

        self._reinstatement_type_code = reinstatement_type_code

    @property
    def reinstatement_type_code_string(self):
        """Gets the reinstatement_type_code_string of this ReinstatementTypeDetails.  # noqa: E501


        :return: The reinstatement_type_code_string of this ReinstatementTypeDetails.  # noqa: E501
        :rtype: str
        """
        return self._reinstatement_type_code_string

    @reinstatement_type_code_string.setter
    def reinstatement_type_code_string(self, reinstatement_type_code_string):
        """Sets the reinstatement_type_code_string of this ReinstatementTypeDetails.


        :param reinstatement_type_code_string: The reinstatement_type_code_string of this ReinstatementTypeDetails.  # noqa: E501
        :type: str
        """
        if reinstatement_type_code_string is None:
            raise ValueError("Invalid value for `reinstatement_type_code_string`, must not be `None`")  # noqa: E501

        self._reinstatement_type_code_string = reinstatement_type_code_string

    @property
    def reinstatement_type_location_text(self):
        """Gets the reinstatement_type_location_text of this ReinstatementTypeDetails.  # noqa: E501


        :return: The reinstatement_type_location_text of this ReinstatementTypeDetails.  # noqa: E501
        :rtype: str
        """
        return self._reinstatement_type_location_text

    @reinstatement_type_location_text.setter
    def reinstatement_type_location_text(self, reinstatement_type_location_text):
        """Sets the reinstatement_type_location_text of this ReinstatementTypeDetails.


        :param reinstatement_type_location_text: The reinstatement_type_location_text of this ReinstatementTypeDetails.  # noqa: E501
        :type: str
        """

        self._reinstatement_type_location_text = reinstatement_type_location_text

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
        if issubclass(ReinstatementTypeDetails, dict):
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
        if not isinstance(other, ReinstatementTypeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
