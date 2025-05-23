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

class GeographicalAreaCreateResponse(object):
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
        'file_id': 'float',
        'geographical_area_reference_number': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'geographical_area_reference_number': 'geographical_area_reference_number'
    }

    def __init__(self, file_id=None, geographical_area_reference_number=None):  # noqa: E501
        """GeographicalAreaCreateResponse - a model defined in Swagger"""  # noqa: E501
        self._file_id = None
        self._geographical_area_reference_number = None
        self.discriminator = None
        self.file_id = file_id
        self.geographical_area_reference_number = geographical_area_reference_number

    @property
    def file_id(self):
        """Gets the file_id of this GeographicalAreaCreateResponse.  # noqa: E501


        :return: The file_id of this GeographicalAreaCreateResponse.  # noqa: E501
        :rtype: float
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this GeographicalAreaCreateResponse.


        :param file_id: The file_id of this GeographicalAreaCreateResponse.  # noqa: E501
        :type: float
        """
        if file_id is None:
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501

        self._file_id = file_id

    @property
    def geographical_area_reference_number(self):
        """Gets the geographical_area_reference_number of this GeographicalAreaCreateResponse.  # noqa: E501


        :return: The geographical_area_reference_number of this GeographicalAreaCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._geographical_area_reference_number

    @geographical_area_reference_number.setter
    def geographical_area_reference_number(self, geographical_area_reference_number):
        """Sets the geographical_area_reference_number of this GeographicalAreaCreateResponse.


        :param geographical_area_reference_number: The geographical_area_reference_number of this GeographicalAreaCreateResponse.  # noqa: E501
        :type: str
        """
        if geographical_area_reference_number is None:
            raise ValueError("Invalid value for `geographical_area_reference_number`, must not be `None`")  # noqa: E501

        self._geographical_area_reference_number = geographical_area_reference_number

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
        if issubclass(GeographicalAreaCreateResponse, dict):
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
        if not isinstance(other, GeographicalAreaCreateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
