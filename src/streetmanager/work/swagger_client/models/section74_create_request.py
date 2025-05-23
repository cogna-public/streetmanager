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

class Section74CreateRequest(object):
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
        'permit_reference_number': 'str',
        'location_description': 'str',
        'location_types': 'list[LocationType]',
        'inspection_date': 'datetime',
        'overrun_warning_reasons': 'list[OverrunWarningReason]',
        'overrun_warning_details': 'str',
        'officer_name': 'str',
        'officer_contact_details': 'str',
        'schedule_follow_up_inspection': 'bool',
        'reinspection_date': 'datetime',
        'reinspection_date_time': 'datetime',
        'section_74_evidence': 'bool',
        'file_ids': 'list[float]'
    }

    attribute_map = {
        'internal_user_identifier': 'internal_user_identifier',
        'internal_user_name': 'internal_user_name',
        'permit_reference_number': 'permit_reference_number',
        'location_description': 'location_description',
        'location_types': 'location_types',
        'inspection_date': 'inspection_date',
        'overrun_warning_reasons': 'overrun_warning_reasons',
        'overrun_warning_details': 'overrun_warning_details',
        'officer_name': 'officer_name',
        'officer_contact_details': 'officer_contact_details',
        'schedule_follow_up_inspection': 'schedule_follow_up_inspection',
        'reinspection_date': 'reinspection_date',
        'reinspection_date_time': 'reinspection_date_time',
        'section_74_evidence': 'section_74_evidence',
        'file_ids': 'file_ids'
    }

    def __init__(self, internal_user_identifier=None, internal_user_name=None, permit_reference_number=None, location_description=None, location_types=None, inspection_date=None, overrun_warning_reasons=None, overrun_warning_details=None, officer_name=None, officer_contact_details=None, schedule_follow_up_inspection=None, reinspection_date=None, reinspection_date_time=None, section_74_evidence=None, file_ids=None):  # noqa: E501
        """Section74CreateRequest - a model defined in Swagger"""  # noqa: E501
        self._internal_user_identifier = None
        self._internal_user_name = None
        self._permit_reference_number = None
        self._location_description = None
        self._location_types = None
        self._inspection_date = None
        self._overrun_warning_reasons = None
        self._overrun_warning_details = None
        self._officer_name = None
        self._officer_contact_details = None
        self._schedule_follow_up_inspection = None
        self._reinspection_date = None
        self._reinspection_date_time = None
        self._section_74_evidence = None
        self._file_ids = None
        self.discriminator = None
        if internal_user_identifier is not None:
            self.internal_user_identifier = internal_user_identifier
        if internal_user_name is not None:
            self.internal_user_name = internal_user_name
        self.permit_reference_number = permit_reference_number
        self.location_description = location_description
        self.location_types = location_types
        self.inspection_date = inspection_date
        self.overrun_warning_reasons = overrun_warning_reasons
        self.overrun_warning_details = overrun_warning_details
        self.officer_name = officer_name
        self.officer_contact_details = officer_contact_details
        self.schedule_follow_up_inspection = schedule_follow_up_inspection
        if reinspection_date is not None:
            self.reinspection_date = reinspection_date
        if reinspection_date_time is not None:
            self.reinspection_date_time = reinspection_date_time
        self.section_74_evidence = section_74_evidence
        if file_ids is not None:
            self.file_ids = file_ids

    @property
    def internal_user_identifier(self):
        """Gets the internal_user_identifier of this Section74CreateRequest.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The internal_user_identifier of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_user_identifier

    @internal_user_identifier.setter
    def internal_user_identifier(self, internal_user_identifier):
        """Sets the internal_user_identifier of this Section74CreateRequest.

        Max length 100 characters  # noqa: E501

        :param internal_user_identifier: The internal_user_identifier of this Section74CreateRequest.  # noqa: E501
        :type: str
        """

        self._internal_user_identifier = internal_user_identifier

    @property
    def internal_user_name(self):
        """Gets the internal_user_name of this Section74CreateRequest.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The internal_user_name of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_user_name

    @internal_user_name.setter
    def internal_user_name(self, internal_user_name):
        """Sets the internal_user_name of this Section74CreateRequest.

        Max length 100 characters  # noqa: E501

        :param internal_user_name: The internal_user_name of this Section74CreateRequest.  # noqa: E501
        :type: str
        """

        self._internal_user_name = internal_user_name

    @property
    def permit_reference_number(self):
        """Gets the permit_reference_number of this Section74CreateRequest.  # noqa: E501


        :return: The permit_reference_number of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._permit_reference_number

    @permit_reference_number.setter
    def permit_reference_number(self, permit_reference_number):
        """Sets the permit_reference_number of this Section74CreateRequest.


        :param permit_reference_number: The permit_reference_number of this Section74CreateRequest.  # noqa: E501
        :type: str
        """
        if permit_reference_number is None:
            raise ValueError("Invalid value for `permit_reference_number`, must not be `None`")  # noqa: E501

        self._permit_reference_number = permit_reference_number

    @property
    def location_description(self):
        """Gets the location_description of this Section74CreateRequest.  # noqa: E501

        Max length 500 characters  # noqa: E501

        :return: The location_description of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description):
        """Sets the location_description of this Section74CreateRequest.

        Max length 500 characters  # noqa: E501

        :param location_description: The location_description of this Section74CreateRequest.  # noqa: E501
        :type: str
        """
        if location_description is None:
            raise ValueError("Invalid value for `location_description`, must not be `None`")  # noqa: E501

        self._location_description = location_description

    @property
    def location_types(self):
        """Gets the location_types of this Section74CreateRequest.  # noqa: E501

        Array values must be unique  # noqa: E501

        :return: The location_types of this Section74CreateRequest.  # noqa: E501
        :rtype: list[LocationType]
        """
        return self._location_types

    @location_types.setter
    def location_types(self, location_types):
        """Sets the location_types of this Section74CreateRequest.

        Array values must be unique  # noqa: E501

        :param location_types: The location_types of this Section74CreateRequest.  # noqa: E501
        :type: list[LocationType]
        """
        if location_types is None:
            raise ValueError("Invalid value for `location_types`, must not be `None`")  # noqa: E501

        self._location_types = location_types

    @property
    def inspection_date(self):
        """Gets the inspection_date of this Section74CreateRequest.  # noqa: E501

        Date must be today or a date in the past  # noqa: E501

        :return: The inspection_date of this Section74CreateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._inspection_date

    @inspection_date.setter
    def inspection_date(self, inspection_date):
        """Sets the inspection_date of this Section74CreateRequest.

        Date must be today or a date in the past  # noqa: E501

        :param inspection_date: The inspection_date of this Section74CreateRequest.  # noqa: E501
        :type: datetime
        """
        if inspection_date is None:
            raise ValueError("Invalid value for `inspection_date`, must not be `None`")  # noqa: E501

        self._inspection_date = inspection_date

    @property
    def overrun_warning_reasons(self):
        """Gets the overrun_warning_reasons of this Section74CreateRequest.  # noqa: E501

        Array values must be unique  # noqa: E501

        :return: The overrun_warning_reasons of this Section74CreateRequest.  # noqa: E501
        :rtype: list[OverrunWarningReason]
        """
        return self._overrun_warning_reasons

    @overrun_warning_reasons.setter
    def overrun_warning_reasons(self, overrun_warning_reasons):
        """Sets the overrun_warning_reasons of this Section74CreateRequest.

        Array values must be unique  # noqa: E501

        :param overrun_warning_reasons: The overrun_warning_reasons of this Section74CreateRequest.  # noqa: E501
        :type: list[OverrunWarningReason]
        """
        if overrun_warning_reasons is None:
            raise ValueError("Invalid value for `overrun_warning_reasons`, must not be `None`")  # noqa: E501

        self._overrun_warning_reasons = overrun_warning_reasons

    @property
    def overrun_warning_details(self):
        """Gets the overrun_warning_details of this Section74CreateRequest.  # noqa: E501

        Max length 500 characters  # noqa: E501

        :return: The overrun_warning_details of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._overrun_warning_details

    @overrun_warning_details.setter
    def overrun_warning_details(self, overrun_warning_details):
        """Sets the overrun_warning_details of this Section74CreateRequest.

        Max length 500 characters  # noqa: E501

        :param overrun_warning_details: The overrun_warning_details of this Section74CreateRequest.  # noqa: E501
        :type: str
        """
        if overrun_warning_details is None:
            raise ValueError("Invalid value for `overrun_warning_details`, must not be `None`")  # noqa: E501

        self._overrun_warning_details = overrun_warning_details

    @property
    def officer_name(self):
        """Gets the officer_name of this Section74CreateRequest.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The officer_name of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._officer_name

    @officer_name.setter
    def officer_name(self, officer_name):
        """Sets the officer_name of this Section74CreateRequest.

        Max length 100 characters  # noqa: E501

        :param officer_name: The officer_name of this Section74CreateRequest.  # noqa: E501
        :type: str
        """
        if officer_name is None:
            raise ValueError("Invalid value for `officer_name`, must not be `None`")  # noqa: E501

        self._officer_name = officer_name

    @property
    def officer_contact_details(self):
        """Gets the officer_contact_details of this Section74CreateRequest.  # noqa: E501

        Max length 100 characters  # noqa: E501

        :return: The officer_contact_details of this Section74CreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._officer_contact_details

    @officer_contact_details.setter
    def officer_contact_details(self, officer_contact_details):
        """Sets the officer_contact_details of this Section74CreateRequest.

        Max length 100 characters  # noqa: E501

        :param officer_contact_details: The officer_contact_details of this Section74CreateRequest.  # noqa: E501
        :type: str
        """
        if officer_contact_details is None:
            raise ValueError("Invalid value for `officer_contact_details`, must not be `None`")  # noqa: E501

        self._officer_contact_details = officer_contact_details

    @property
    def schedule_follow_up_inspection(self):
        """Gets the schedule_follow_up_inspection of this Section74CreateRequest.  # noqa: E501


        :return: The schedule_follow_up_inspection of this Section74CreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._schedule_follow_up_inspection

    @schedule_follow_up_inspection.setter
    def schedule_follow_up_inspection(self, schedule_follow_up_inspection):
        """Sets the schedule_follow_up_inspection of this Section74CreateRequest.


        :param schedule_follow_up_inspection: The schedule_follow_up_inspection of this Section74CreateRequest.  # noqa: E501
        :type: bool
        """
        if schedule_follow_up_inspection is None:
            raise ValueError("Invalid value for `schedule_follow_up_inspection`, must not be `None`")  # noqa: E501

        self._schedule_follow_up_inspection = schedule_follow_up_inspection

    @property
    def reinspection_date(self):
        """Gets the reinspection_date of this Section74CreateRequest.  # noqa: E501

        Date must occur today or a date in the future  # noqa: E501

        :return: The reinspection_date of this Section74CreateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._reinspection_date

    @reinspection_date.setter
    def reinspection_date(self, reinspection_date):
        """Sets the reinspection_date of this Section74CreateRequest.

        Date must occur today or a date in the future  # noqa: E501

        :param reinspection_date: The reinspection_date of this Section74CreateRequest.  # noqa: E501
        :type: datetime
        """

        self._reinspection_date = reinspection_date

    @property
    def reinspection_date_time(self):
        """Gets the reinspection_date_time of this Section74CreateRequest.  # noqa: E501

        The date for reinspection_date_time must match the date for reinspection_date Time must occur today or a date in the future  # noqa: E501

        :return: The reinspection_date_time of this Section74CreateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._reinspection_date_time

    @reinspection_date_time.setter
    def reinspection_date_time(self, reinspection_date_time):
        """Sets the reinspection_date_time of this Section74CreateRequest.

        The date for reinspection_date_time must match the date for reinspection_date Time must occur today or a date in the future  # noqa: E501

        :param reinspection_date_time: The reinspection_date_time of this Section74CreateRequest.  # noqa: E501
        :type: datetime
        """

        self._reinspection_date_time = reinspection_date_time

    @property
    def section_74_evidence(self):
        """Gets the section_74_evidence of this Section74CreateRequest.  # noqa: E501


        :return: The section_74_evidence of this Section74CreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._section_74_evidence

    @section_74_evidence.setter
    def section_74_evidence(self, section_74_evidence):
        """Sets the section_74_evidence of this Section74CreateRequest.


        :param section_74_evidence: The section_74_evidence of this Section74CreateRequest.  # noqa: E501
        :type: bool
        """
        if section_74_evidence is None:
            raise ValueError("Invalid value for `section_74_evidence`, must not be `None`")  # noqa: E501

        self._section_74_evidence = section_74_evidence

    @property
    def file_ids(self):
        """Gets the file_ids of this Section74CreateRequest.  # noqa: E501

        Required if section_74_evidence = true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide > Works API > File upload for more information  # noqa: E501

        :return: The file_ids of this Section74CreateRequest.  # noqa: E501
        :rtype: list[float]
        """
        return self._file_ids

    @file_ids.setter
    def file_ids(self, file_ids):
        """Sets the file_ids of this Section74CreateRequest.

        Required if section_74_evidence = true Array values must be unique Must not contain null or undefined values A file_id can only be associated with one section of Street Manager See API specification Resource Guide > Works API > File upload for more information  # noqa: E501

        :param file_ids: The file_ids of this Section74CreateRequest.  # noqa: E501
        :type: list[float]
        """

        self._file_ids = file_ids

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
        if issubclass(Section74CreateRequest, dict):
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
        if not isinstance(other, Section74CreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
