# coding: utf-8

"""
    Street Manager Event API

    See API specification Resource Guide > Event API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkUpdateResponse(object):
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
        'rows': 'list[WorkUpdateSummaryResponse]',
        'next_update': 'float'
    }

    attribute_map = {
        'rows': 'rows',
        'next_update': 'next_update'
    }

    def __init__(self, rows=None, next_update=None):  # noqa: E501
        """WorkUpdateResponse - a model defined in Swagger"""  # noqa: E501
        self._rows = None
        self._next_update = None
        self.discriminator = None
        self.rows = rows
        if next_update is not None:
            self.next_update = next_update

    @property
    def rows(self):
        """Gets the rows of this WorkUpdateResponse.  # noqa: E501


        :return: The rows of this WorkUpdateResponse.  # noqa: E501
        :rtype: list[WorkUpdateSummaryResponse]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this WorkUpdateResponse.


        :param rows: The rows of this WorkUpdateResponse.  # noqa: E501
        :type: list[WorkUpdateSummaryResponse]
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

    @property
    def next_update(self):
        """Gets the next_update of this WorkUpdateResponse.  # noqa: E501


        :return: The next_update of this WorkUpdateResponse.  # noqa: E501
        :rtype: float
        """
        return self._next_update

    @next_update.setter
    def next_update(self, next_update):
        """Sets the next_update of this WorkUpdateResponse.


        :param next_update: The next_update of this WorkUpdateResponse.  # noqa: E501
        :type: float
        """

        self._next_update = next_update

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
        if issubclass(WorkUpdateResponse, dict):
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
        if not isinstance(other, WorkUpdateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
