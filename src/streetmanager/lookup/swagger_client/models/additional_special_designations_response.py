# coding: utf-8

"""
    Street Manager Street Lookup API

    See API specification Resource Guide > Street Lookup API for more information on endpoints NOTE: Swagger Editor/UI does not display all description text for enumerations and child elements, check swagger.json for full description text  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdditionalSpecialDesignationsResponse(object):
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
        'street_special_desig_code': 'AdditionalSpecialDesignationCodeResponse',
        'street_special_desig_code_string': 'str',
        'special_desig_location_text': 'str',
        'special_desig_description': 'str',
        'special_desig_start_time': 'float',
        'special_desig_end_time': 'float',
        'special_desig_periodicity_code': 'AllOfAdditionalSpecialDesignationsResponseSpecialDesigPeriodicityCode',
        'special_desig_periodicity_code_string': 'str',
        'asd_coordinate_geometry': 'AllOfAdditionalSpecialDesignationsResponseAsdCoordinateGeometry',
        'whole_road': 'bool',
        'special_desig_start_date': 'datetime',
        'special_desig_end_date': 'datetime'
    }

    attribute_map = {
        'street_special_desig_code': 'street_special_desig_code',
        'street_special_desig_code_string': 'street_special_desig_code_string',
        'special_desig_location_text': 'special_desig_location_text',
        'special_desig_description': 'special_desig_description',
        'special_desig_start_time': 'special_desig_start_time',
        'special_desig_end_time': 'special_desig_end_time',
        'special_desig_periodicity_code': 'special_desig_periodicity_code',
        'special_desig_periodicity_code_string': 'special_desig_periodicity_code_string',
        'asd_coordinate_geometry': 'asd_coordinate_geometry',
        'whole_road': 'whole_road',
        'special_desig_start_date': 'special_desig_start_date',
        'special_desig_end_date': 'special_desig_end_date'
    }

    def __init__(self, street_special_desig_code=None, street_special_desig_code_string=None, special_desig_location_text=None, special_desig_description=None, special_desig_start_time=None, special_desig_end_time=None, special_desig_periodicity_code=None, special_desig_periodicity_code_string=None, asd_coordinate_geometry=None, whole_road=None, special_desig_start_date=None, special_desig_end_date=None):  # noqa: E501
        """AdditionalSpecialDesignationsResponse - a model defined in Swagger"""  # noqa: E501
        self._street_special_desig_code = None
        self._street_special_desig_code_string = None
        self._special_desig_location_text = None
        self._special_desig_description = None
        self._special_desig_start_time = None
        self._special_desig_end_time = None
        self._special_desig_periodicity_code = None
        self._special_desig_periodicity_code_string = None
        self._asd_coordinate_geometry = None
        self._whole_road = None
        self._special_desig_start_date = None
        self._special_desig_end_date = None
        self.discriminator = None
        self.street_special_desig_code = street_special_desig_code
        if street_special_desig_code_string is not None:
            self.street_special_desig_code_string = street_special_desig_code_string
        if special_desig_location_text is not None:
            self.special_desig_location_text = special_desig_location_text
        if special_desig_description is not None:
            self.special_desig_description = special_desig_description
        if special_desig_start_time is not None:
            self.special_desig_start_time = special_desig_start_time
        if special_desig_end_time is not None:
            self.special_desig_end_time = special_desig_end_time
        if special_desig_periodicity_code is not None:
            self.special_desig_periodicity_code = special_desig_periodicity_code
        if special_desig_periodicity_code_string is not None:
            self.special_desig_periodicity_code_string = special_desig_periodicity_code_string
        if asd_coordinate_geometry is not None:
            self.asd_coordinate_geometry = asd_coordinate_geometry
        if whole_road is not None:
            self.whole_road = whole_road
        if special_desig_start_date is not None:
            self.special_desig_start_date = special_desig_start_date
        if special_desig_end_date is not None:
            self.special_desig_end_date = special_desig_end_date

    @property
    def street_special_desig_code(self):
        """Gets the street_special_desig_code of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The street_special_desig_code of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: AdditionalSpecialDesignationCodeResponse
        """
        return self._street_special_desig_code

    @street_special_desig_code.setter
    def street_special_desig_code(self, street_special_desig_code):
        """Sets the street_special_desig_code of this AdditionalSpecialDesignationsResponse.


        :param street_special_desig_code: The street_special_desig_code of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: AdditionalSpecialDesignationCodeResponse
        """
        if street_special_desig_code is None:
            raise ValueError("Invalid value for `street_special_desig_code`, must not be `None`")  # noqa: E501

        self._street_special_desig_code = street_special_desig_code

    @property
    def street_special_desig_code_string(self):
        """Gets the street_special_desig_code_string of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The street_special_desig_code_string of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: str
        """
        return self._street_special_desig_code_string

    @street_special_desig_code_string.setter
    def street_special_desig_code_string(self, street_special_desig_code_string):
        """Sets the street_special_desig_code_string of this AdditionalSpecialDesignationsResponse.


        :param street_special_desig_code_string: The street_special_desig_code_string of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: str
        """

        self._street_special_desig_code_string = street_special_desig_code_string

    @property
    def special_desig_location_text(self):
        """Gets the special_desig_location_text of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_location_text of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: str
        """
        return self._special_desig_location_text

    @special_desig_location_text.setter
    def special_desig_location_text(self, special_desig_location_text):
        """Sets the special_desig_location_text of this AdditionalSpecialDesignationsResponse.


        :param special_desig_location_text: The special_desig_location_text of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: str
        """

        self._special_desig_location_text = special_desig_location_text

    @property
    def special_desig_description(self):
        """Gets the special_desig_description of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_description of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: str
        """
        return self._special_desig_description

    @special_desig_description.setter
    def special_desig_description(self, special_desig_description):
        """Sets the special_desig_description of this AdditionalSpecialDesignationsResponse.


        :param special_desig_description: The special_desig_description of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: str
        """

        self._special_desig_description = special_desig_description

    @property
    def special_desig_start_time(self):
        """Gets the special_desig_start_time of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_start_time of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: float
        """
        return self._special_desig_start_time

    @special_desig_start_time.setter
    def special_desig_start_time(self, special_desig_start_time):
        """Sets the special_desig_start_time of this AdditionalSpecialDesignationsResponse.


        :param special_desig_start_time: The special_desig_start_time of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: float
        """

        self._special_desig_start_time = special_desig_start_time

    @property
    def special_desig_end_time(self):
        """Gets the special_desig_end_time of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_end_time of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: float
        """
        return self._special_desig_end_time

    @special_desig_end_time.setter
    def special_desig_end_time(self, special_desig_end_time):
        """Sets the special_desig_end_time of this AdditionalSpecialDesignationsResponse.


        :param special_desig_end_time: The special_desig_end_time of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: float
        """

        self._special_desig_end_time = special_desig_end_time

    @property
    def special_desig_periodicity_code(self):
        """Gets the special_desig_periodicity_code of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_periodicity_code of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: AllOfAdditionalSpecialDesignationsResponseSpecialDesigPeriodicityCode
        """
        return self._special_desig_periodicity_code

    @special_desig_periodicity_code.setter
    def special_desig_periodicity_code(self, special_desig_periodicity_code):
        """Sets the special_desig_periodicity_code of this AdditionalSpecialDesignationsResponse.


        :param special_desig_periodicity_code: The special_desig_periodicity_code of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: AllOfAdditionalSpecialDesignationsResponseSpecialDesigPeriodicityCode
        """

        self._special_desig_periodicity_code = special_desig_periodicity_code

    @property
    def special_desig_periodicity_code_string(self):
        """Gets the special_desig_periodicity_code_string of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_periodicity_code_string of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: str
        """
        return self._special_desig_periodicity_code_string

    @special_desig_periodicity_code_string.setter
    def special_desig_periodicity_code_string(self, special_desig_periodicity_code_string):
        """Sets the special_desig_periodicity_code_string of this AdditionalSpecialDesignationsResponse.


        :param special_desig_periodicity_code_string: The special_desig_periodicity_code_string of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: str
        """

        self._special_desig_periodicity_code_string = special_desig_periodicity_code_string

    @property
    def asd_coordinate_geometry(self):
        """Gets the asd_coordinate_geometry of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The asd_coordinate_geometry of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: AllOfAdditionalSpecialDesignationsResponseAsdCoordinateGeometry
        """
        return self._asd_coordinate_geometry

    @asd_coordinate_geometry.setter
    def asd_coordinate_geometry(self, asd_coordinate_geometry):
        """Sets the asd_coordinate_geometry of this AdditionalSpecialDesignationsResponse.


        :param asd_coordinate_geometry: The asd_coordinate_geometry of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: AllOfAdditionalSpecialDesignationsResponseAsdCoordinateGeometry
        """

        self._asd_coordinate_geometry = asd_coordinate_geometry

    @property
    def whole_road(self):
        """Gets the whole_road of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The whole_road of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._whole_road

    @whole_road.setter
    def whole_road(self, whole_road):
        """Sets the whole_road of this AdditionalSpecialDesignationsResponse.


        :param whole_road: The whole_road of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: bool
        """

        self._whole_road = whole_road

    @property
    def special_desig_start_date(self):
        """Gets the special_desig_start_date of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_start_date of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._special_desig_start_date

    @special_desig_start_date.setter
    def special_desig_start_date(self, special_desig_start_date):
        """Sets the special_desig_start_date of this AdditionalSpecialDesignationsResponse.


        :param special_desig_start_date: The special_desig_start_date of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: datetime
        """

        self._special_desig_start_date = special_desig_start_date

    @property
    def special_desig_end_date(self):
        """Gets the special_desig_end_date of this AdditionalSpecialDesignationsResponse.  # noqa: E501


        :return: The special_desig_end_date of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._special_desig_end_date

    @special_desig_end_date.setter
    def special_desig_end_date(self, special_desig_end_date):
        """Sets the special_desig_end_date of this AdditionalSpecialDesignationsResponse.


        :param special_desig_end_date: The special_desig_end_date of this AdditionalSpecialDesignationsResponse.  # noqa: E501
        :type: datetime
        """

        self._special_desig_end_date = special_desig_end_date

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
        if issubclass(AdditionalSpecialDesignationsResponse, dict):
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
        if not isinstance(other, AdditionalSpecialDesignationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
