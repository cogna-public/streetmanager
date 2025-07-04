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

class CommentSummaryResponse(object):
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
        'topic': 'CommentTopicResponse',
        'topic_string': 'str',
        'author_email_address': 'str',
        'author_organisation_reference': 'str',
        'detail': 'str',
        'date_created': 'datetime',
        'comment_reference_number': 'str',
        'is_read': 'bool',
        'read_on': 'datetime',
        'read_by': 'str',
        'is_internal': 'bool'
    }

    attribute_map = {
        'work_reference_number': 'work_reference_number',
        'topic': 'topic',
        'topic_string': 'topic_string',
        'author_email_address': 'author_email_address',
        'author_organisation_reference': 'author_organisation_reference',
        'detail': 'detail',
        'date_created': 'date_created',
        'comment_reference_number': 'comment_reference_number',
        'is_read': 'is_read',
        'read_on': 'read_on',
        'read_by': 'read_by',
        'is_internal': 'is_internal'
    }

    def __init__(self, work_reference_number=None, topic=None, topic_string=None, author_email_address=None, author_organisation_reference=None, detail=None, date_created=None, comment_reference_number=None, is_read=None, read_on=None, read_by=None, is_internal=None):  # noqa: E501
        """CommentSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._work_reference_number = None
        self._topic = None
        self._topic_string = None
        self._author_email_address = None
        self._author_organisation_reference = None
        self._detail = None
        self._date_created = None
        self._comment_reference_number = None
        self._is_read = None
        self._read_on = None
        self._read_by = None
        self._is_internal = None
        self.discriminator = None
        self.work_reference_number = work_reference_number
        self.topic = topic
        self.topic_string = topic_string
        self.author_email_address = author_email_address
        self.author_organisation_reference = author_organisation_reference
        self.detail = detail
        self.date_created = date_created
        self.comment_reference_number = comment_reference_number
        self.is_read = is_read
        if read_on is not None:
            self.read_on = read_on
        if read_by is not None:
            self.read_by = read_by
        self.is_internal = is_internal

    @property
    def work_reference_number(self):
        """Gets the work_reference_number of this CommentSummaryResponse.  # noqa: E501


        :return: The work_reference_number of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._work_reference_number

    @work_reference_number.setter
    def work_reference_number(self, work_reference_number):
        """Sets the work_reference_number of this CommentSummaryResponse.


        :param work_reference_number: The work_reference_number of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """
        if work_reference_number is None:
            raise ValueError("Invalid value for `work_reference_number`, must not be `None`")  # noqa: E501

        self._work_reference_number = work_reference_number

    @property
    def topic(self):
        """Gets the topic of this CommentSummaryResponse.  # noqa: E501


        :return: The topic of this CommentSummaryResponse.  # noqa: E501
        :rtype: CommentTopicResponse
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this CommentSummaryResponse.


        :param topic: The topic of this CommentSummaryResponse.  # noqa: E501
        :type: CommentTopicResponse
        """
        if topic is None:
            raise ValueError("Invalid value for `topic`, must not be `None`")  # noqa: E501

        self._topic = topic

    @property
    def topic_string(self):
        """Gets the topic_string of this CommentSummaryResponse.  # noqa: E501


        :return: The topic_string of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._topic_string

    @topic_string.setter
    def topic_string(self, topic_string):
        """Sets the topic_string of this CommentSummaryResponse.


        :param topic_string: The topic_string of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """
        if topic_string is None:
            raise ValueError("Invalid value for `topic_string`, must not be `None`")  # noqa: E501

        self._topic_string = topic_string

    @property
    def author_email_address(self):
        """Gets the author_email_address of this CommentSummaryResponse.  # noqa: E501


        :return: The author_email_address of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._author_email_address

    @author_email_address.setter
    def author_email_address(self, author_email_address):
        """Sets the author_email_address of this CommentSummaryResponse.


        :param author_email_address: The author_email_address of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """
        if author_email_address is None:
            raise ValueError("Invalid value for `author_email_address`, must not be `None`")  # noqa: E501

        self._author_email_address = author_email_address

    @property
    def author_organisation_reference(self):
        """Gets the author_organisation_reference of this CommentSummaryResponse.  # noqa: E501


        :return: The author_organisation_reference of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._author_organisation_reference

    @author_organisation_reference.setter
    def author_organisation_reference(self, author_organisation_reference):
        """Sets the author_organisation_reference of this CommentSummaryResponse.


        :param author_organisation_reference: The author_organisation_reference of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """
        if author_organisation_reference is None:
            raise ValueError("Invalid value for `author_organisation_reference`, must not be `None`")  # noqa: E501

        self._author_organisation_reference = author_organisation_reference

    @property
    def detail(self):
        """Gets the detail of this CommentSummaryResponse.  # noqa: E501


        :return: The detail of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CommentSummaryResponse.


        :param detail: The detail of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def date_created(self):
        """Gets the date_created of this CommentSummaryResponse.  # noqa: E501


        :return: The date_created of this CommentSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this CommentSummaryResponse.


        :param date_created: The date_created of this CommentSummaryResponse.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def comment_reference_number(self):
        """Gets the comment_reference_number of this CommentSummaryResponse.  # noqa: E501


        :return: The comment_reference_number of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._comment_reference_number

    @comment_reference_number.setter
    def comment_reference_number(self, comment_reference_number):
        """Sets the comment_reference_number of this CommentSummaryResponse.


        :param comment_reference_number: The comment_reference_number of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """
        if comment_reference_number is None:
            raise ValueError("Invalid value for `comment_reference_number`, must not be `None`")  # noqa: E501

        self._comment_reference_number = comment_reference_number

    @property
    def is_read(self):
        """Gets the is_read of this CommentSummaryResponse.  # noqa: E501


        :return: The is_read of this CommentSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this CommentSummaryResponse.


        :param is_read: The is_read of this CommentSummaryResponse.  # noqa: E501
        :type: bool
        """
        if is_read is None:
            raise ValueError("Invalid value for `is_read`, must not be `None`")  # noqa: E501

        self._is_read = is_read

    @property
    def read_on(self):
        """Gets the read_on of this CommentSummaryResponse.  # noqa: E501


        :return: The read_on of this CommentSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._read_on

    @read_on.setter
    def read_on(self, read_on):
        """Sets the read_on of this CommentSummaryResponse.


        :param read_on: The read_on of this CommentSummaryResponse.  # noqa: E501
        :type: datetime
        """

        self._read_on = read_on

    @property
    def read_by(self):
        """Gets the read_by of this CommentSummaryResponse.  # noqa: E501


        :return: The read_by of this CommentSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._read_by

    @read_by.setter
    def read_by(self, read_by):
        """Sets the read_by of this CommentSummaryResponse.


        :param read_by: The read_by of this CommentSummaryResponse.  # noqa: E501
        :type: str
        """

        self._read_by = read_by

    @property
    def is_internal(self):
        """Gets the is_internal of this CommentSummaryResponse.  # noqa: E501


        :return: The is_internal of this CommentSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this CommentSummaryResponse.


        :param is_internal: The is_internal of this CommentSummaryResponse.  # noqa: E501
        :type: bool
        """
        if is_internal is None:
            raise ValueError("Invalid value for `is_internal`, must not be `None`")  # noqa: E501

        self._is_internal = is_internal

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
        if issubclass(CommentSummaryResponse, dict):
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
        if not isinstance(other, CommentSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
