# coding: utf-8

"""
    Street Manager Data Export API

    See API specification Resource Guide > Data Export API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FeesCSVExportRequest(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'swa_code': 'str',
        'fee_report_format': 'AllOfFeesCSVExportRequestFeeReportFormat',
        'swa_code_filter': 'str',
        'export_description': 'str'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'swa_code': 'swa_code',
        'fee_report_format': 'fee_report_format',
        'swa_code_filter': 'swa_code_filter',
        'export_description': 'export_description'
    }

    def __init__(self, start_date=None, end_date=None, swa_code=None, fee_report_format=None, swa_code_filter=None, export_description=None):  # noqa: E501
        """FeesCSVExportRequest - a model defined in Swagger"""  # noqa: E501
        self._start_date = None
        self._end_date = None
        self._swa_code = None
        self._fee_report_format = None
        self._swa_code_filter = None
        self._export_description = None
        self.discriminator = None
        self.start_date = start_date
        self.end_date = end_date
        if swa_code is not None:
            self.swa_code = swa_code
        self.fee_report_format = fee_report_format
        if swa_code_filter is not None:
            self.swa_code_filter = swa_code_filter
        if export_description is not None:
            self.export_description = export_description

    @property
    def start_date(self):
        """Gets the start_date of this FeesCSVExportRequest.  # noqa: E501

        Must be within 30 days of provided end_date Must be provided if end_date is provided  # noqa: E501

        :return: The start_date of this FeesCSVExportRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FeesCSVExportRequest.

        Must be within 30 days of provided end_date Must be provided if end_date is provided  # noqa: E501

        :param start_date: The start_date of this FeesCSVExportRequest.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this FeesCSVExportRequest.  # noqa: E501

        Must occur on or after the provided start_date  # noqa: E501

        :return: The end_date of this FeesCSVExportRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this FeesCSVExportRequest.

        Must occur on or after the provided start_date  # noqa: E501

        :param end_date: The end_date of this FeesCSVExportRequest.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def swa_code(self):
        """Gets the swa_code of this FeesCSVExportRequest.  # noqa: E501

        Must be provided if user is a contractor Max length 4 characters  # noqa: E501

        :return: The swa_code of this FeesCSVExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._swa_code

    @swa_code.setter
    def swa_code(self, swa_code):
        """Sets the swa_code of this FeesCSVExportRequest.

        Must be provided if user is a contractor Max length 4 characters  # noqa: E501

        :param swa_code: The swa_code of this FeesCSVExportRequest.  # noqa: E501
        :type: str
        """

        self._swa_code = swa_code

    @property
    def fee_report_format(self):
        """Gets the fee_report_format of this FeesCSVExportRequest.  # noqa: E501


        :return: The fee_report_format of this FeesCSVExportRequest.  # noqa: E501
        :rtype: AllOfFeesCSVExportRequestFeeReportFormat
        """
        return self._fee_report_format

    @fee_report_format.setter
    def fee_report_format(self, fee_report_format):
        """Sets the fee_report_format of this FeesCSVExportRequest.


        :param fee_report_format: The fee_report_format of this FeesCSVExportRequest.  # noqa: E501
        :type: AllOfFeesCSVExportRequestFeeReportFormat
        """
        if fee_report_format is None:
            raise ValueError("Invalid value for `fee_report_format`, must not be `None`")  # noqa: E501

        self._fee_report_format = fee_report_format

    @property
    def swa_code_filter(self):
        """Gets the swa_code_filter of this FeesCSVExportRequest.  # noqa: E501

        Required if fee_report_format = single_org_one_csv Max length 4 characters  # noqa: E501

        :return: The swa_code_filter of this FeesCSVExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._swa_code_filter

    @swa_code_filter.setter
    def swa_code_filter(self, swa_code_filter):
        """Sets the swa_code_filter of this FeesCSVExportRequest.

        Required if fee_report_format = single_org_one_csv Max length 4 characters  # noqa: E501

        :param swa_code_filter: The swa_code_filter of this FeesCSVExportRequest.  # noqa: E501
        :type: str
        """

        self._swa_code_filter = swa_code_filter

    @property
    def export_description(self):
        """Gets the export_description of this FeesCSVExportRequest.  # noqa: E501


        :return: The export_description of this FeesCSVExportRequest.  # noqa: E501
        :rtype: str
        """
        return self._export_description

    @export_description.setter
    def export_description(self, export_description):
        """Sets the export_description of this FeesCSVExportRequest.


        :param export_description: The export_description of this FeesCSVExportRequest.  # noqa: E501
        :type: str
        """

        self._export_description = export_description

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
        if issubclass(FeesCSVExportRequest, dict):
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
        if not isinstance(other, FeesCSVExportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
