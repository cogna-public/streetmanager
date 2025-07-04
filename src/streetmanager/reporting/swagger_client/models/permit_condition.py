# coding: utf-8

"""
    Street Manager Reporting API

    See API specification Resource Guide > Reporting API for more information on paging and endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PermitCondition(object):
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
        'condition': 'PermitConditionTypeResponse',
        'condition_string': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'condition_string': 'condition_string',
        'comment': 'comment'
    }

    def __init__(self, condition=None, condition_string=None, comment=None):  # noqa: E501
        """PermitCondition - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._condition_string = None
        self._comment = None
        self.discriminator = None
        self.condition = condition
        self.condition_string = condition_string
        if comment is not None:
            self.comment = comment

    @property
    def condition(self):
        """Gets the condition of this PermitCondition.  # noqa: E501


        :return: The condition of this PermitCondition.  # noqa: E501
        :rtype: PermitConditionTypeResponse
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this PermitCondition.


        :param condition: The condition of this PermitCondition.  # noqa: E501
        :type: PermitConditionTypeResponse
        """
        if condition is None:
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition

    @property
    def condition_string(self):
        """Gets the condition_string of this PermitCondition.  # noqa: E501


        :return: The condition_string of this PermitCondition.  # noqa: E501
        :rtype: str
        """
        return self._condition_string

    @condition_string.setter
    def condition_string(self, condition_string):
        """Sets the condition_string of this PermitCondition.


        :param condition_string: The condition_string of this PermitCondition.  # noqa: E501
        :type: str
        """
        if condition_string is None:
            raise ValueError("Invalid value for `condition_string`, must not be `None`")  # noqa: E501

        self._condition_string = condition_string

    @property
    def comment(self):
        """Gets the comment of this PermitCondition.  # noqa: E501


        :return: The comment of this PermitCondition.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PermitCondition.


        :param comment: The comment of this PermitCondition.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(PermitCondition, dict):
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
        if not isinstance(other, PermitCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
