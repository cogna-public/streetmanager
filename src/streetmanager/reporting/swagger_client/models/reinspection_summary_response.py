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

class ReinspectionSummaryResponse(object):
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
        'inspection_date': 'datetime',
        'work_reference_number': 'str',
        'location_description': 'str',
        'street': 'str',
        'town': 'str',
        'area': 'str',
        'inspection_type': 'InspectionTypeResponse',
        'inspection_type_string': 'str',
        'inspection_category': 'AllOfReinspectionSummaryResponseInspectionCategory',
        'inspection_category_string': 'str',
        'highway_authority': 'str',
        'promoter_organisation': 'str',
        'date_modified': 'datetime'
    }

    attribute_map = {
        'inspection_date': 'inspection_date',
        'work_reference_number': 'work_reference_number',
        'location_description': 'location_description',
        'street': 'street',
        'town': 'town',
        'area': 'area',
        'inspection_type': 'inspection_type',
        'inspection_type_string': 'inspection_type_string',
        'inspection_category': 'inspection_category',
        'inspection_category_string': 'inspection_category_string',
        'highway_authority': 'highway_authority',
        'promoter_organisation': 'promoter_organisation',
        'date_modified': 'date_modified'
    }

    def __init__(self, inspection_date=None, work_reference_number=None, location_description=None, street=None, town=None, area=None, inspection_type=None, inspection_type_string=None, inspection_category=None, inspection_category_string=None, highway_authority=None, promoter_organisation=None, date_modified=None):  # noqa: E501
        """ReinspectionSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._inspection_date = None
        self._work_reference_number = None
        self._location_description = None
        self._street = None
        self._town = None
        self._area = None
        self._inspection_type = None
        self._inspection_type_string = None
        self._inspection_category = None
        self._inspection_category_string = None
        self._highway_authority = None
        self._promoter_organisation = None
        self._date_modified = None
        self.discriminator = None
        self.inspection_date = inspection_date
        self.work_reference_number = work_reference_number
        self.location_description = location_description
        self.street = street
        self.town = town
        self.area = area
        self.inspection_type = inspection_type
        self.inspection_type_string = inspection_type_string
        if inspection_category is not None:
            self.inspection_category = inspection_category
        if inspection_category_string is not None:
            self.inspection_category_string = inspection_category_string
        self.highway_authority = highway_authority
        self.promoter_organisation = promoter_organisation
        self.date_modified = date_modified

    @property
    def inspection_date(self):
        """Gets the inspection_date of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The inspection_date of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._inspection_date

    @inspection_date.setter
    def inspection_date(self, inspection_date):
        """Sets the inspection_date of this ReinspectionSummaryResponse.


        :param inspection_date: The inspection_date of this ReinspectionSummaryResponse.  # noqa: E501
        :type: datetime
        """
        if inspection_date is None:
            raise ValueError("Invalid value for `inspection_date`, must not be `None`")  # noqa: E501

        self._inspection_date = inspection_date

    @property
    def work_reference_number(self):
        """Gets the work_reference_number of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The work_reference_number of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._work_reference_number

    @work_reference_number.setter
    def work_reference_number(self, work_reference_number):
        """Sets the work_reference_number of this ReinspectionSummaryResponse.


        :param work_reference_number: The work_reference_number of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if work_reference_number is None:
            raise ValueError("Invalid value for `work_reference_number`, must not be `None`")  # noqa: E501

        self._work_reference_number = work_reference_number

    @property
    def location_description(self):
        """Gets the location_description of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The location_description of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description):
        """Sets the location_description of this ReinspectionSummaryResponse.


        :param location_description: The location_description of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if location_description is None:
            raise ValueError("Invalid value for `location_description`, must not be `None`")  # noqa: E501

        self._location_description = location_description

    @property
    def street(self):
        """Gets the street of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The street of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this ReinspectionSummaryResponse.


        :param street: The street of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if street is None:
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def town(self):
        """Gets the town of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The town of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """Sets the town of this ReinspectionSummaryResponse.


        :param town: The town of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if town is None:
            raise ValueError("Invalid value for `town`, must not be `None`")  # noqa: E501

        self._town = town

    @property
    def area(self):
        """Gets the area of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The area of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ReinspectionSummaryResponse.


        :param area: The area of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if area is None:
            raise ValueError("Invalid value for `area`, must not be `None`")  # noqa: E501

        self._area = area

    @property
    def inspection_type(self):
        """Gets the inspection_type of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The inspection_type of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: InspectionTypeResponse
        """
        return self._inspection_type

    @inspection_type.setter
    def inspection_type(self, inspection_type):
        """Sets the inspection_type of this ReinspectionSummaryResponse.


        :param inspection_type: The inspection_type of this ReinspectionSummaryResponse.  # noqa: E501
        :type: InspectionTypeResponse
        """
        if inspection_type is None:
            raise ValueError("Invalid value for `inspection_type`, must not be `None`")  # noqa: E501

        self._inspection_type = inspection_type

    @property
    def inspection_type_string(self):
        """Gets the inspection_type_string of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The inspection_type_string of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._inspection_type_string

    @inspection_type_string.setter
    def inspection_type_string(self, inspection_type_string):
        """Sets the inspection_type_string of this ReinspectionSummaryResponse.


        :param inspection_type_string: The inspection_type_string of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if inspection_type_string is None:
            raise ValueError("Invalid value for `inspection_type_string`, must not be `None`")  # noqa: E501

        self._inspection_type_string = inspection_type_string

    @property
    def inspection_category(self):
        """Gets the inspection_category of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The inspection_category of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: AllOfReinspectionSummaryResponseInspectionCategory
        """
        return self._inspection_category

    @inspection_category.setter
    def inspection_category(self, inspection_category):
        """Sets the inspection_category of this ReinspectionSummaryResponse.


        :param inspection_category: The inspection_category of this ReinspectionSummaryResponse.  # noqa: E501
        :type: AllOfReinspectionSummaryResponseInspectionCategory
        """

        self._inspection_category = inspection_category

    @property
    def inspection_category_string(self):
        """Gets the inspection_category_string of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The inspection_category_string of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._inspection_category_string

    @inspection_category_string.setter
    def inspection_category_string(self, inspection_category_string):
        """Sets the inspection_category_string of this ReinspectionSummaryResponse.


        :param inspection_category_string: The inspection_category_string of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """

        self._inspection_category_string = inspection_category_string

    @property
    def highway_authority(self):
        """Gets the highway_authority of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The highway_authority of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._highway_authority

    @highway_authority.setter
    def highway_authority(self, highway_authority):
        """Sets the highway_authority of this ReinspectionSummaryResponse.


        :param highway_authority: The highway_authority of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if highway_authority is None:
            raise ValueError("Invalid value for `highway_authority`, must not be `None`")  # noqa: E501

        self._highway_authority = highway_authority

    @property
    def promoter_organisation(self):
        """Gets the promoter_organisation of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The promoter_organisation of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._promoter_organisation

    @promoter_organisation.setter
    def promoter_organisation(self, promoter_organisation):
        """Sets the promoter_organisation of this ReinspectionSummaryResponse.


        :param promoter_organisation: The promoter_organisation of this ReinspectionSummaryResponse.  # noqa: E501
        :type: str
        """
        if promoter_organisation is None:
            raise ValueError("Invalid value for `promoter_organisation`, must not be `None`")  # noqa: E501

        self._promoter_organisation = promoter_organisation

    @property
    def date_modified(self):
        """Gets the date_modified of this ReinspectionSummaryResponse.  # noqa: E501


        :return: The date_modified of this ReinspectionSummaryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ReinspectionSummaryResponse.


        :param date_modified: The date_modified of this ReinspectionSummaryResponse.  # noqa: E501
        :type: datetime
        """
        if date_modified is None:
            raise ValueError("Invalid value for `date_modified`, must not be `None`")  # noqa: E501

        self._date_modified = date_modified

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
        if issubclass(ReinspectionSummaryResponse, dict):
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
        if not isinstance(other, ReinspectionSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
