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

class AuditObjectTypeResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PERMIT = "permit"
    REINSTATEMENT = "reinstatement"
    INSPECTION = "inspection"
    FPN = "fpn"
    PAA = "paa"
    WORKSTREAM = "workstream"
    WORK = "work"
    ORGANISATION = "organisation"
    ACTIVITY = "activity"
    FORWARD_PLAN = "forward_plan"
    COMMENT = "comment"
    SCHEDULED_INSPECTION = "scheduled_inspection"
    SECTION_81 = "section_81"
    USER = "user"
    GEOGRAPHICAL_AREA = "geographical_area"
    CHANGE_REQUEST = "change_request"
    APPLICATION = "application"
    SAMPLE_INSPECTION = "sample_inspection"
    SECTION_74 = "section_74"
    SECTION_58 = "section_58"
    SITE = "site"
    SAMPLE_INSPECTION_TARGET = "sample_inspection_target"
    FEE_MATRIX = "fee_matrix"
    NON_COMPLIANCE = "non_compliance"
    PRIVATE_STREET = "private_street"
    EVENT_SUBSCRIPTION = "event_subscription"
    MATERIAL_CLASSIFICATION = "material_classification"
    UPCOMING_ENUM = "upcoming_enum"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """AuditObjectTypeResponse - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(AuditObjectTypeResponse, dict):
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
        if not isinstance(other, AuditObjectTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
