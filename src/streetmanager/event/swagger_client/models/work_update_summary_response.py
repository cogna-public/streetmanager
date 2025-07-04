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

class WorkUpdateSummaryResponse(object):
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
        'work_reference_number': 'str',
        'update_date_time': 'datetime',
        'update_id': 'float',
        'event_type': 'AuditEventType',
        'event_type_string': 'str',
        'object_type': 'AuditObjectTypeResponse',
        'object_type_string': 'str'
    }

    attribute_map = {
        'work_reference_number': 'work_reference_number',
        'update_date_time': 'update_date_time',
        'update_id': 'update_id',
        'event_type': 'event_type',
        'event_type_string': 'event_type_string',
        'object_type': 'object_type',
        'object_type_string': 'object_type_string'
    }

    def __init__(self, work_reference_number=None, update_date_time=None, update_id=None, event_type=None, event_type_string=None, object_type=None, object_type_string=None):  # noqa: E501
        """WorkUpdateSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._work_reference_number = None
        self._update_date_time = None
        self._update_id = None
        self._event_type = None
        self._event_type_string = None
        self._object_type = None
        self._object_type_string = None
        self.discriminator = None
        self.work_reference_number = work_reference_number
        self.update_date_time = update_date_time
        self.update_id = update_id
        self.event_type = event_type
        self.event_type_string = event_type_string
        self.object_type = object_type
        self.object_type_string = object_type_string

    @property
    def work_reference_number(self):
        """Gets the work_reference_number of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The work_reference_number of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._work_reference_number

    @work_reference_number.setter
    def work_reference_number(self, work_reference_number):
        """Sets the work_reference_number of this WorkUpdateSummaryResponse.


        :param work_reference_number: The work_reference_number of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: str
        """
        if work_reference_number is None:
            raise ValueError("Invalid value for `work_reference_number`, must not be `None`")  # noqa: E501

        self._work_reference_number = work_reference_number

    @property
    def update_date_time(self):
        """Gets the update_date_time of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The update_date_time of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date_time

    @update_date_time.setter
    def update_date_time(self, update_date_time):
        """Sets the update_date_time of this WorkUpdateSummaryResponse.


        :param update_date_time: The update_date_time of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: datetime
        """
        if update_date_time is None:
            raise ValueError("Invalid value for `update_date_time`, must not be `None`")  # noqa: E501

        self._update_date_time = update_date_time

    @property
    def update_id(self):
        """Gets the update_id of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The update_id of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: float
        """
        return self._update_id

    @update_id.setter
    def update_id(self, update_id):
        """Sets the update_id of this WorkUpdateSummaryResponse.


        :param update_id: The update_id of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: float
        """
        if update_id is None:
            raise ValueError("Invalid value for `update_id`, must not be `None`")  # noqa: E501

        self._update_id = update_id

    @property
    def event_type(self):
        """Gets the event_type of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The event_type of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: AuditEventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this WorkUpdateSummaryResponse.


        :param event_type: The event_type of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: AuditEventType
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def event_type_string(self):
        """Gets the event_type_string of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The event_type_string of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._event_type_string

    @event_type_string.setter
    def event_type_string(self, event_type_string):
        """Sets the event_type_string of this WorkUpdateSummaryResponse.


        :param event_type_string: The event_type_string of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: str
        """
        if event_type_string is None:
            raise ValueError("Invalid value for `event_type_string`, must not be `None`")  # noqa: E501

        self._event_type_string = event_type_string

    @property
    def object_type(self):
        """Gets the object_type of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The object_type of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: AuditObjectTypeResponse
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this WorkUpdateSummaryResponse.


        :param object_type: The object_type of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: AuditObjectTypeResponse
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501

        self._object_type = object_type

    @property
    def object_type_string(self):
        """Gets the object_type_string of this WorkUpdateSummaryResponse.  # noqa: E501


        :return: The object_type_string of this WorkUpdateSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._object_type_string

    @object_type_string.setter
    def object_type_string(self, object_type_string):
        """Sets the object_type_string of this WorkUpdateSummaryResponse.


        :param object_type_string: The object_type_string of this WorkUpdateSummaryResponse.  # noqa: E501
        :type: str
        """
        if object_type_string is None:
            raise ValueError("Invalid value for `object_type_string`, must not be `None`")  # noqa: E501

        self._object_type_string = object_type_string

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
        if issubclass(WorkUpdateSummaryResponse, dict):
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
        if not isinstance(other, WorkUpdateSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
