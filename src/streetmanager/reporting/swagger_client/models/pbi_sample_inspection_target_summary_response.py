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

class PbiSampleInspectionTargetSummaryResponse(object):
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
        'pbi_sample_inspection_target_reference_number': 'str',
        'organisation_name': 'str',
        'org_ref': 'str',
        'inspection_units': 'float',
        'inspection_rate': 'float',
        'target_a': 'float',
        'target_b': 'float',
        'target_c': 'float',
        'completed_a': 'float',
        'completed_b': 'float',
        'completed_c': 'float',
        'generated_b': 'float',
        'generated_c': 'float',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'is_inspection_rate_auto_updated': 'bool'
    }

    attribute_map = {
        'pbi_sample_inspection_target_reference_number': 'pbi_sample_inspection_target_reference_number',
        'organisation_name': 'organisation_name',
        'org_ref': 'org_ref',
        'inspection_units': 'inspection_units',
        'inspection_rate': 'inspection_rate',
        'target_a': 'target_a',
        'target_b': 'target_b',
        'target_c': 'target_c',
        'completed_a': 'completed_a',
        'completed_b': 'completed_b',
        'completed_c': 'completed_c',
        'generated_b': 'generated_b',
        'generated_c': 'generated_c',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'is_inspection_rate_auto_updated': 'is_inspection_rate_auto_updated'
    }

    def __init__(self, pbi_sample_inspection_target_reference_number=None, organisation_name=None, org_ref=None, inspection_units=None, inspection_rate=None, target_a=None, target_b=None, target_c=None, completed_a=None, completed_b=None, completed_c=None, generated_b=None, generated_c=None, start_date=None, end_date=None, is_inspection_rate_auto_updated=None):  # noqa: E501
        """PbiSampleInspectionTargetSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._pbi_sample_inspection_target_reference_number = None
        self._organisation_name = None
        self._org_ref = None
        self._inspection_units = None
        self._inspection_rate = None
        self._target_a = None
        self._target_b = None
        self._target_c = None
        self._completed_a = None
        self._completed_b = None
        self._completed_c = None
        self._generated_b = None
        self._generated_c = None
        self._start_date = None
        self._end_date = None
        self._is_inspection_rate_auto_updated = None
        self.discriminator = None
        self.pbi_sample_inspection_target_reference_number = pbi_sample_inspection_target_reference_number
        self.organisation_name = organisation_name
        self.org_ref = org_ref
        self.inspection_units = inspection_units
        self.inspection_rate = inspection_rate
        self.target_a = target_a
        self.target_b = target_b
        self.target_c = target_c
        self.completed_a = completed_a
        self.completed_b = completed_b
        self.completed_c = completed_c
        self.generated_b = generated_b
        self.generated_c = generated_c
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        self.is_inspection_rate_auto_updated = is_inspection_rate_auto_updated

    @property
    def pbi_sample_inspection_target_reference_number(self):
        """Gets the pbi_sample_inspection_target_reference_number of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The pbi_sample_inspection_target_reference_number of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._pbi_sample_inspection_target_reference_number

    @pbi_sample_inspection_target_reference_number.setter
    def pbi_sample_inspection_target_reference_number(self, pbi_sample_inspection_target_reference_number):
        """Sets the pbi_sample_inspection_target_reference_number of this PbiSampleInspectionTargetSummaryResponse.


        :param pbi_sample_inspection_target_reference_number: The pbi_sample_inspection_target_reference_number of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: str
        """
        if pbi_sample_inspection_target_reference_number is None:
            raise ValueError("Invalid value for `pbi_sample_inspection_target_reference_number`, must not be `None`")  # noqa: E501

        self._pbi_sample_inspection_target_reference_number = pbi_sample_inspection_target_reference_number

    @property
    def organisation_name(self):
        """Gets the organisation_name of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The organisation_name of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this PbiSampleInspectionTargetSummaryResponse.


        :param organisation_name: The organisation_name of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: str
        """
        if organisation_name is None:
            raise ValueError("Invalid value for `organisation_name`, must not be `None`")  # noqa: E501

        self._organisation_name = organisation_name

    @property
    def org_ref(self):
        """Gets the org_ref of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The org_ref of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._org_ref

    @org_ref.setter
    def org_ref(self, org_ref):
        """Sets the org_ref of this PbiSampleInspectionTargetSummaryResponse.


        :param org_ref: The org_ref of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: str
        """
        if org_ref is None:
            raise ValueError("Invalid value for `org_ref`, must not be `None`")  # noqa: E501

        self._org_ref = org_ref

    @property
    def inspection_units(self):
        """Gets the inspection_units of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The inspection_units of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._inspection_units

    @inspection_units.setter
    def inspection_units(self, inspection_units):
        """Sets the inspection_units of this PbiSampleInspectionTargetSummaryResponse.


        :param inspection_units: The inspection_units of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if inspection_units is None:
            raise ValueError("Invalid value for `inspection_units`, must not be `None`")  # noqa: E501

        self._inspection_units = inspection_units

    @property
    def inspection_rate(self):
        """Gets the inspection_rate of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The inspection_rate of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._inspection_rate

    @inspection_rate.setter
    def inspection_rate(self, inspection_rate):
        """Sets the inspection_rate of this PbiSampleInspectionTargetSummaryResponse.


        :param inspection_rate: The inspection_rate of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if inspection_rate is None:
            raise ValueError("Invalid value for `inspection_rate`, must not be `None`")  # noqa: E501

        self._inspection_rate = inspection_rate

    @property
    def target_a(self):
        """Gets the target_a of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The target_a of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._target_a

    @target_a.setter
    def target_a(self, target_a):
        """Sets the target_a of this PbiSampleInspectionTargetSummaryResponse.


        :param target_a: The target_a of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if target_a is None:
            raise ValueError("Invalid value for `target_a`, must not be `None`")  # noqa: E501

        self._target_a = target_a

    @property
    def target_b(self):
        """Gets the target_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The target_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._target_b

    @target_b.setter
    def target_b(self, target_b):
        """Sets the target_b of this PbiSampleInspectionTargetSummaryResponse.


        :param target_b: The target_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if target_b is None:
            raise ValueError("Invalid value for `target_b`, must not be `None`")  # noqa: E501

        self._target_b = target_b

    @property
    def target_c(self):
        """Gets the target_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The target_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._target_c

    @target_c.setter
    def target_c(self, target_c):
        """Sets the target_c of this PbiSampleInspectionTargetSummaryResponse.


        :param target_c: The target_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if target_c is None:
            raise ValueError("Invalid value for `target_c`, must not be `None`")  # noqa: E501

        self._target_c = target_c

    @property
    def completed_a(self):
        """Gets the completed_a of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The completed_a of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._completed_a

    @completed_a.setter
    def completed_a(self, completed_a):
        """Sets the completed_a of this PbiSampleInspectionTargetSummaryResponse.


        :param completed_a: The completed_a of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if completed_a is None:
            raise ValueError("Invalid value for `completed_a`, must not be `None`")  # noqa: E501

        self._completed_a = completed_a

    @property
    def completed_b(self):
        """Gets the completed_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The completed_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._completed_b

    @completed_b.setter
    def completed_b(self, completed_b):
        """Sets the completed_b of this PbiSampleInspectionTargetSummaryResponse.


        :param completed_b: The completed_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if completed_b is None:
            raise ValueError("Invalid value for `completed_b`, must not be `None`")  # noqa: E501

        self._completed_b = completed_b

    @property
    def completed_c(self):
        """Gets the completed_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The completed_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._completed_c

    @completed_c.setter
    def completed_c(self, completed_c):
        """Sets the completed_c of this PbiSampleInspectionTargetSummaryResponse.


        :param completed_c: The completed_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if completed_c is None:
            raise ValueError("Invalid value for `completed_c`, must not be `None`")  # noqa: E501

        self._completed_c = completed_c

    @property
    def generated_b(self):
        """Gets the generated_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The generated_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._generated_b

    @generated_b.setter
    def generated_b(self, generated_b):
        """Sets the generated_b of this PbiSampleInspectionTargetSummaryResponse.


        :param generated_b: The generated_b of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if generated_b is None:
            raise ValueError("Invalid value for `generated_b`, must not be `None`")  # noqa: E501

        self._generated_b = generated_b

    @property
    def generated_c(self):
        """Gets the generated_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The generated_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._generated_c

    @generated_c.setter
    def generated_c(self, generated_c):
        """Sets the generated_c of this PbiSampleInspectionTargetSummaryResponse.


        :param generated_c: The generated_c of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: float
        """
        if generated_c is None:
            raise ValueError("Invalid value for `generated_c`, must not be `None`")  # noqa: E501

        self._generated_c = generated_c

    @property
    def start_date(self):
        """Gets the start_date of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The start_date of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PbiSampleInspectionTargetSummaryResponse.


        :param start_date: The start_date of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The end_date of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PbiSampleInspectionTargetSummaryResponse.


        :param end_date: The end_date of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def is_inspection_rate_auto_updated(self):
        """Gets the is_inspection_rate_auto_updated of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501


        :return: The is_inspection_rate_auto_updated of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_inspection_rate_auto_updated

    @is_inspection_rate_auto_updated.setter
    def is_inspection_rate_auto_updated(self, is_inspection_rate_auto_updated):
        """Sets the is_inspection_rate_auto_updated of this PbiSampleInspectionTargetSummaryResponse.


        :param is_inspection_rate_auto_updated: The is_inspection_rate_auto_updated of this PbiSampleInspectionTargetSummaryResponse.  # noqa: E501
        :type: bool
        """
        if is_inspection_rate_auto_updated is None:
            raise ValueError("Invalid value for `is_inspection_rate_auto_updated`, must not be `None`")  # noqa: E501

        self._is_inspection_rate_auto_updated = is_inspection_rate_auto_updated

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
        if issubclass(PbiSampleInspectionTargetSummaryResponse, dict):
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
        if not isinstance(other, PbiSampleInspectionTargetSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
