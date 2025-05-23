# coding: utf-8

"""
    Street Manager GeoJSON API

    See API specification Resource Guide > GeoJSON API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AncillaryInfoResponse(object):
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
        'type': 'FeatureCollectionType',
        'features': 'list[AncillaryInfoFeature]'
    }

    attribute_map = {
        'type': 'type',
        'features': 'features'
    }

    def __init__(self, type=None, features=None):  # noqa: E501
        """AncillaryInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._features = None
        self.discriminator = None
        self.type = type
        self.features = features

    @property
    def type(self):
        """Gets the type of this AncillaryInfoResponse.  # noqa: E501


        :return: The type of this AncillaryInfoResponse.  # noqa: E501
        :rtype: FeatureCollectionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AncillaryInfoResponse.


        :param type: The type of this AncillaryInfoResponse.  # noqa: E501
        :type: FeatureCollectionType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def features(self):
        """Gets the features of this AncillaryInfoResponse.  # noqa: E501


        :return: The features of this AncillaryInfoResponse.  # noqa: E501
        :rtype: list[AncillaryInfoFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this AncillaryInfoResponse.


        :param features: The features of this AncillaryInfoResponse.  # noqa: E501
        :type: list[AncillaryInfoFeature]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

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
        if issubclass(AncillaryInfoResponse, dict):
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
        if not isinstance(other, AncillaryInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
