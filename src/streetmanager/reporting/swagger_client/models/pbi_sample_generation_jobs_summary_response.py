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

class PbiSampleGenerationJobsSummaryResponse(object):
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
        'date_created': 'datetime',
        'async_job_status': 'AsyncJobStatusResponse',
        'async_job_status_string': 'str',
        'username': 'str'
    }

    attribute_map = {
        'date_created': 'date_created',
        'async_job_status': 'async_job_status',
        'async_job_status_string': 'async_job_status_string',
        'username': 'username'
    }

    def __init__(self, date_created=None, async_job_status=None, async_job_status_string=None, username=None):  # noqa: E501
        """PbiSampleGenerationJobsSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._date_created = None
        self._async_job_status = None
        self._async_job_status_string = None
        self._username = None
        self.discriminator = None
        self.date_created = date_created
        self.async_job_status = async_job_status
        self.async_job_status_string = async_job_status_string
        self.username = username

    @property
    def date_created(self):
        """Gets the date_created of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501


        :return: The date_created of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this PbiSampleGenerationJobsSummaryResponse.


        :param date_created: The date_created of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def async_job_status(self):
        """Gets the async_job_status of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501


        :return: The async_job_status of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :rtype: AsyncJobStatusResponse
        """
        return self._async_job_status

    @async_job_status.setter
    def async_job_status(self, async_job_status):
        """Sets the async_job_status of this PbiSampleGenerationJobsSummaryResponse.


        :param async_job_status: The async_job_status of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :type: AsyncJobStatusResponse
        """
        if async_job_status is None:
            raise ValueError("Invalid value for `async_job_status`, must not be `None`")  # noqa: E501

        self._async_job_status = async_job_status

    @property
    def async_job_status_string(self):
        """Gets the async_job_status_string of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501


        :return: The async_job_status_string of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._async_job_status_string

    @async_job_status_string.setter
    def async_job_status_string(self, async_job_status_string):
        """Sets the async_job_status_string of this PbiSampleGenerationJobsSummaryResponse.


        :param async_job_status_string: The async_job_status_string of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :type: str
        """
        if async_job_status_string is None:
            raise ValueError("Invalid value for `async_job_status_string`, must not be `None`")  # noqa: E501

        self._async_job_status_string = async_job_status_string

    @property
    def username(self):
        """Gets the username of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501


        :return: The username of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PbiSampleGenerationJobsSummaryResponse.


        :param username: The username of this PbiSampleGenerationJobsSummaryResponse.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(PbiSampleGenerationJobsSummaryResponse, dict):
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
        if not isinstance(other, PbiSampleGenerationJobsSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
