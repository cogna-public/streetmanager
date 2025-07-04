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

class ReinstatementSummaryResponse(object):
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
        'site_reference_number': 'str',
        'work_reference_number': 'str',
        'reinstatement_reference_number': 'str',
        'promoter_organisation': 'str',
        'highway_authority': 'str',
        'street_name': 'str',
        'town': 'str',
        'area_name': 'str',
        'location_description': 'str',
        'registration_date': 'datetime',
        'reinstatement_date': 'datetime',
        'reinstatement_type': 'ReinstatementTypeResponse',
        'reinstatement_type_string': 'str',
        'reinstatement_status': 'ReinstatementStatusResponse',
        'reinstatement_status_string': 'str',
        'end_date': 'datetime',
        'is_active_reinstatement': 'bool',
        'is_subsumed': 'bool'
    }

    attribute_map = {
        'site_reference_number': 'site_reference_number',
        'work_reference_number': 'work_reference_number',
        'reinstatement_reference_number': 'reinstatement_reference_number',
        'promoter_organisation': 'promoter_organisation',
        'highway_authority': 'highway_authority',
        'street_name': 'street_name',
        'town': 'town',
        'area_name': 'area_name',
        'location_description': 'location_description',
        'registration_date': 'registration_date',
        'reinstatement_date': 'reinstatement_date',
        'reinstatement_type': 'reinstatement_type',
        'reinstatement_type_string': 'reinstatement_type_string',
        'reinstatement_status': 'reinstatement_status',
        'reinstatement_status_string': 'reinstatement_status_string',
        'end_date': 'end_date',
        'is_active_reinstatement': 'is_active_reinstatement',
        'is_subsumed': 'is_subsumed'
    }

    def __init__(self, site_reference_number=None, work_reference_number=None, reinstatement_reference_number=None, promoter_organisation=None, highway_authority=None, street_name=None, town=None, area_name=None, location_description=None, registration_date=None, reinstatement_date=None, reinstatement_type=None, reinstatement_type_string=None, reinstatement_status=None, reinstatement_status_string=None, end_date=None, is_active_reinstatement=None, is_subsumed=None):  # noqa: E501
        """ReinstatementSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._site_reference_number = None
        self._work_reference_number = None
        self._reinstatement_reference_number = None
        self._promoter_organisation = None
        self._highway_authority = None
        self._street_name = None
        self._town = None
        self._area_name = None
        self._location_description = None
        self._registration_date = None
        self._reinstatement_date = None
        self._reinstatement_type = None
        self._reinstatement_type_string = None
        self._reinstatement_status = None
        self._reinstatement_status_string = None
        self._end_date = None
        self._is_active_reinstatement = None
        self._is_subsumed = None
        self.discriminator = None
        self.site_reference_number = site_reference_number
        self.work_reference_number = work_reference_number
        self.reinstatement_reference_number = reinstatement_reference_number
        self.promoter_organisation = promoter_organisation
        self.highway_authority = highway_authority
        self.street_name = street_name
        if town is not None:
            self.town = town
        if area_name is not None:
            self.area_name = area_name
        self.location_description = location_description
        self.registration_date = registration_date
        if reinstatement_date is not None:
            self.reinstatement_date = reinstatement_date
        self.reinstatement_type = reinstatement_type
        self.reinstatement_type_string = reinstatement_type_string
        self.reinstatement_status = reinstatement_status
        self.reinstatement_status_string = reinstatement_status_string
        if end_date is not None:
            self.end_date = end_date
        self.is_active_reinstatement = is_active_reinstatement
        self.is_subsumed = is_subsumed

    @property
    def site_reference_number(self):
        """Gets the site_reference_number of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The site_reference_number of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._site_reference_number

    @site_reference_number.setter
    def site_reference_number(self, site_reference_number):
        """Sets the site_reference_number of this ReinstatementSummaryResponse.


        :param site_reference_number: The site_reference_number of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if site_reference_number is None:
            raise ValueError("Invalid value for `site_reference_number`, must not be `None`")  # noqa: E501

        self._site_reference_number = site_reference_number

    @property
    def work_reference_number(self):
        """Gets the work_reference_number of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The work_reference_number of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._work_reference_number

    @work_reference_number.setter
    def work_reference_number(self, work_reference_number):
        """Sets the work_reference_number of this ReinstatementSummaryResponse.


        :param work_reference_number: The work_reference_number of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if work_reference_number is None:
            raise ValueError("Invalid value for `work_reference_number`, must not be `None`")  # noqa: E501

        self._work_reference_number = work_reference_number

    @property
    def reinstatement_reference_number(self):
        """Gets the reinstatement_reference_number of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The reinstatement_reference_number of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._reinstatement_reference_number

    @reinstatement_reference_number.setter
    def reinstatement_reference_number(self, reinstatement_reference_number):
        """Sets the reinstatement_reference_number of this ReinstatementSummaryResponse.


        :param reinstatement_reference_number: The reinstatement_reference_number of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if reinstatement_reference_number is None:
            raise ValueError("Invalid value for `reinstatement_reference_number`, must not be `None`")  # noqa: E501

        self._reinstatement_reference_number = reinstatement_reference_number

    @property
    def promoter_organisation(self):
        """Gets the promoter_organisation of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The promoter_organisation of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._promoter_organisation

    @promoter_organisation.setter
    def promoter_organisation(self, promoter_organisation):
        """Sets the promoter_organisation of this ReinstatementSummaryResponse.


        :param promoter_organisation: The promoter_organisation of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if promoter_organisation is None:
            raise ValueError("Invalid value for `promoter_organisation`, must not be `None`")  # noqa: E501

        self._promoter_organisation = promoter_organisation

    @property
    def highway_authority(self):
        """Gets the highway_authority of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The highway_authority of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._highway_authority

    @highway_authority.setter
    def highway_authority(self, highway_authority):
        """Sets the highway_authority of this ReinstatementSummaryResponse.


        :param highway_authority: The highway_authority of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if highway_authority is None:
            raise ValueError("Invalid value for `highway_authority`, must not be `None`")  # noqa: E501

        self._highway_authority = highway_authority

    @property
    def street_name(self):
        """Gets the street_name of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The street_name of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this ReinstatementSummaryResponse.


        :param street_name: The street_name of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if street_name is None:
            raise ValueError("Invalid value for `street_name`, must not be `None`")  # noqa: E501

        self._street_name = street_name

    @property
    def town(self):
        """Gets the town of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The town of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """Sets the town of this ReinstatementSummaryResponse.


        :param town: The town of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """

        self._town = town

    @property
    def area_name(self):
        """Gets the area_name of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The area_name of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name):
        """Sets the area_name of this ReinstatementSummaryResponse.


        :param area_name: The area_name of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """

        self._area_name = area_name

    @property
    def location_description(self):
        """Gets the location_description of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The location_description of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description):
        """Sets the location_description of this ReinstatementSummaryResponse.


        :param location_description: The location_description of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if location_description is None:
            raise ValueError("Invalid value for `location_description`, must not be `None`")  # noqa: E501

        self._location_description = location_description

    @property
    def registration_date(self):
        """Gets the registration_date of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The registration_date of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this ReinstatementSummaryResponse.


        :param registration_date: The registration_date of this ReinstatementSummaryResponse.  # noqa: E501
        :type: datetime
        """
        if registration_date is None:
            raise ValueError("Invalid value for `registration_date`, must not be `None`")  # noqa: E501

        self._registration_date = registration_date

    @property
    def reinstatement_date(self):
        """Gets the reinstatement_date of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The reinstatement_date of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._reinstatement_date

    @reinstatement_date.setter
    def reinstatement_date(self, reinstatement_date):
        """Sets the reinstatement_date of this ReinstatementSummaryResponse.


        :param reinstatement_date: The reinstatement_date of this ReinstatementSummaryResponse.  # noqa: E501
        :type: datetime
        """

        self._reinstatement_date = reinstatement_date

    @property
    def reinstatement_type(self):
        """Gets the reinstatement_type of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The reinstatement_type of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: ReinstatementTypeResponse
        """
        return self._reinstatement_type

    @reinstatement_type.setter
    def reinstatement_type(self, reinstatement_type):
        """Sets the reinstatement_type of this ReinstatementSummaryResponse.


        :param reinstatement_type: The reinstatement_type of this ReinstatementSummaryResponse.  # noqa: E501
        :type: ReinstatementTypeResponse
        """
        if reinstatement_type is None:
            raise ValueError("Invalid value for `reinstatement_type`, must not be `None`")  # noqa: E501

        self._reinstatement_type = reinstatement_type

    @property
    def reinstatement_type_string(self):
        """Gets the reinstatement_type_string of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The reinstatement_type_string of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._reinstatement_type_string

    @reinstatement_type_string.setter
    def reinstatement_type_string(self, reinstatement_type_string):
        """Sets the reinstatement_type_string of this ReinstatementSummaryResponse.


        :param reinstatement_type_string: The reinstatement_type_string of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if reinstatement_type_string is None:
            raise ValueError("Invalid value for `reinstatement_type_string`, must not be `None`")  # noqa: E501

        self._reinstatement_type_string = reinstatement_type_string

    @property
    def reinstatement_status(self):
        """Gets the reinstatement_status of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The reinstatement_status of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: ReinstatementStatusResponse
        """
        return self._reinstatement_status

    @reinstatement_status.setter
    def reinstatement_status(self, reinstatement_status):
        """Sets the reinstatement_status of this ReinstatementSummaryResponse.


        :param reinstatement_status: The reinstatement_status of this ReinstatementSummaryResponse.  # noqa: E501
        :type: ReinstatementStatusResponse
        """
        if reinstatement_status is None:
            raise ValueError("Invalid value for `reinstatement_status`, must not be `None`")  # noqa: E501

        self._reinstatement_status = reinstatement_status

    @property
    def reinstatement_status_string(self):
        """Gets the reinstatement_status_string of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The reinstatement_status_string of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._reinstatement_status_string

    @reinstatement_status_string.setter
    def reinstatement_status_string(self, reinstatement_status_string):
        """Sets the reinstatement_status_string of this ReinstatementSummaryResponse.


        :param reinstatement_status_string: The reinstatement_status_string of this ReinstatementSummaryResponse.  # noqa: E501
        :type: str
        """
        if reinstatement_status_string is None:
            raise ValueError("Invalid value for `reinstatement_status_string`, must not be `None`")  # noqa: E501

        self._reinstatement_status_string = reinstatement_status_string

    @property
    def end_date(self):
        """Gets the end_date of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The end_date of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReinstatementSummaryResponse.


        :param end_date: The end_date of this ReinstatementSummaryResponse.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def is_active_reinstatement(self):
        """Gets the is_active_reinstatement of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The is_active_reinstatement of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_active_reinstatement

    @is_active_reinstatement.setter
    def is_active_reinstatement(self, is_active_reinstatement):
        """Sets the is_active_reinstatement of this ReinstatementSummaryResponse.


        :param is_active_reinstatement: The is_active_reinstatement of this ReinstatementSummaryResponse.  # noqa: E501
        :type: bool
        """
        if is_active_reinstatement is None:
            raise ValueError("Invalid value for `is_active_reinstatement`, must not be `None`")  # noqa: E501

        self._is_active_reinstatement = is_active_reinstatement

    @property
    def is_subsumed(self):
        """Gets the is_subsumed of this ReinstatementSummaryResponse.  # noqa: E501


        :return: The is_subsumed of this ReinstatementSummaryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_subsumed

    @is_subsumed.setter
    def is_subsumed(self, is_subsumed):
        """Sets the is_subsumed of this ReinstatementSummaryResponse.


        :param is_subsumed: The is_subsumed of this ReinstatementSummaryResponse.  # noqa: E501
        :type: bool
        """
        if is_subsumed is None:
            raise ValueError("Invalid value for `is_subsumed`, must not be `None`")  # noqa: E501

        self._is_subsumed = is_subsumed

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
        if issubclass(ReinstatementSummaryResponse, dict):
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
        if not isinstance(other, ReinstatementSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
