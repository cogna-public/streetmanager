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

class Section81Response(object):
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
        'section_81_reference_number': 'str',
        'date_created': 'datetime',
        'location_description': 'str',
        'section_81_severity': 'Section81SeverityResponse',
        'section_81_severity_string': 'str',
        'section_81_status': 'Section81StatusResponse',
        'section_81_status_string': 'str',
        'section_81_type': 'Section81TypeResponse',
        'section_81_type_string': 'str',
        'work_reference_number': 'str',
        'usrn': 'float',
        'street_name': 'str',
        'town': 'str',
        'area': 'str',
        'road_category': 'float',
        'works_coordinates': 'object',
        'highway_authority': 'str',
        'highway_authority_swa_code': 'str',
        'promoter_organisation': 'str',
        'promoter_swa_code': 'str',
        'workstream_prefix': 'str',
        'location_types': 'list[LocationTypeResponse]',
        'location_types_string': 'list[str]',
        'inspection_date': 'datetime',
        'other_type_details': 'str',
        'made_safe_by_ha': 'bool',
        'inspector_name': 'str',
        'inspector_contact_number': 'str',
        'additional_details': 'str',
        'status_changed_date': 'datetime',
        'promoter_response': 'str',
        'section_81_work_type': 'AllOfSection81ResponseSection81WorkType',
        'section_81_work_type_string': 'str',
        'promoter_status': 'AllOfSection81ResponsePromoterStatus',
        'promoter_status_string': 'str',
        'promoter_status_changed_date': 'datetime',
        'linked_permit': 'AllOfSection81ResponseLinkedPermit',
        'files': 'list[FileSummaryResponse]'
    }

    attribute_map = {
        'section_81_reference_number': 'section_81_reference_number',
        'date_created': 'date_created',
        'location_description': 'location_description',
        'section_81_severity': 'section_81_severity',
        'section_81_severity_string': 'section_81_severity_string',
        'section_81_status': 'section_81_status',
        'section_81_status_string': 'section_81_status_string',
        'section_81_type': 'section_81_type',
        'section_81_type_string': 'section_81_type_string',
        'work_reference_number': 'work_reference_number',
        'usrn': 'usrn',
        'street_name': 'street_name',
        'town': 'town',
        'area': 'area',
        'road_category': 'road_category',
        'works_coordinates': 'works_coordinates',
        'highway_authority': 'highway_authority',
        'highway_authority_swa_code': 'highway_authority_swa_code',
        'promoter_organisation': 'promoter_organisation',
        'promoter_swa_code': 'promoter_swa_code',
        'workstream_prefix': 'workstream_prefix',
        'location_types': 'location_types',
        'location_types_string': 'location_types_string',
        'inspection_date': 'inspection_date',
        'other_type_details': 'other_type_details',
        'made_safe_by_ha': 'made_safe_by_ha',
        'inspector_name': 'inspector_name',
        'inspector_contact_number': 'inspector_contact_number',
        'additional_details': 'additional_details',
        'status_changed_date': 'status_changed_date',
        'promoter_response': 'promoter_response',
        'section_81_work_type': 'section_81_work_type',
        'section_81_work_type_string': 'section_81_work_type_string',
        'promoter_status': 'promoter_status',
        'promoter_status_string': 'promoter_status_string',
        'promoter_status_changed_date': 'promoter_status_changed_date',
        'linked_permit': 'linked_permit',
        'files': 'files'
    }

    def __init__(self, section_81_reference_number=None, date_created=None, location_description=None, section_81_severity=None, section_81_severity_string=None, section_81_status=None, section_81_status_string=None, section_81_type=None, section_81_type_string=None, work_reference_number=None, usrn=None, street_name=None, town=None, area=None, road_category=None, works_coordinates=None, highway_authority=None, highway_authority_swa_code=None, promoter_organisation=None, promoter_swa_code=None, workstream_prefix=None, location_types=None, location_types_string=None, inspection_date=None, other_type_details=None, made_safe_by_ha=None, inspector_name=None, inspector_contact_number=None, additional_details=None, status_changed_date=None, promoter_response=None, section_81_work_type=None, section_81_work_type_string=None, promoter_status=None, promoter_status_string=None, promoter_status_changed_date=None, linked_permit=None, files=None):  # noqa: E501
        """Section81Response - a model defined in Swagger"""  # noqa: E501
        self._section_81_reference_number = None
        self._date_created = None
        self._location_description = None
        self._section_81_severity = None
        self._section_81_severity_string = None
        self._section_81_status = None
        self._section_81_status_string = None
        self._section_81_type = None
        self._section_81_type_string = None
        self._work_reference_number = None
        self._usrn = None
        self._street_name = None
        self._town = None
        self._area = None
        self._road_category = None
        self._works_coordinates = None
        self._highway_authority = None
        self._highway_authority_swa_code = None
        self._promoter_organisation = None
        self._promoter_swa_code = None
        self._workstream_prefix = None
        self._location_types = None
        self._location_types_string = None
        self._inspection_date = None
        self._other_type_details = None
        self._made_safe_by_ha = None
        self._inspector_name = None
        self._inspector_contact_number = None
        self._additional_details = None
        self._status_changed_date = None
        self._promoter_response = None
        self._section_81_work_type = None
        self._section_81_work_type_string = None
        self._promoter_status = None
        self._promoter_status_string = None
        self._promoter_status_changed_date = None
        self._linked_permit = None
        self._files = None
        self.discriminator = None
        self.section_81_reference_number = section_81_reference_number
        self.date_created = date_created
        self.location_description = location_description
        if section_81_severity is not None:
            self.section_81_severity = section_81_severity
        if section_81_severity_string is not None:
            self.section_81_severity_string = section_81_severity_string
        self.section_81_status = section_81_status
        self.section_81_status_string = section_81_status_string
        self.section_81_type = section_81_type
        self.section_81_type_string = section_81_type_string
        self.work_reference_number = work_reference_number
        self.usrn = usrn
        self.street_name = street_name
        if town is not None:
            self.town = town
        if area is not None:
            self.area = area
        self.road_category = road_category
        self.works_coordinates = works_coordinates
        self.highway_authority = highway_authority
        self.highway_authority_swa_code = highway_authority_swa_code
        self.promoter_organisation = promoter_organisation
        self.promoter_swa_code = promoter_swa_code
        self.workstream_prefix = workstream_prefix
        self.location_types = location_types
        self.location_types_string = location_types_string
        self.inspection_date = inspection_date
        if other_type_details is not None:
            self.other_type_details = other_type_details
        if made_safe_by_ha is not None:
            self.made_safe_by_ha = made_safe_by_ha
        if inspector_name is not None:
            self.inspector_name = inspector_name
        if inspector_contact_number is not None:
            self.inspector_contact_number = inspector_contact_number
        self.additional_details = additional_details
        self.status_changed_date = status_changed_date
        if promoter_response is not None:
            self.promoter_response = promoter_response
        if section_81_work_type is not None:
            self.section_81_work_type = section_81_work_type
        if section_81_work_type_string is not None:
            self.section_81_work_type_string = section_81_work_type_string
        if promoter_status is not None:
            self.promoter_status = promoter_status
        if promoter_status_string is not None:
            self.promoter_status_string = promoter_status_string
        if promoter_status_changed_date is not None:
            self.promoter_status_changed_date = promoter_status_changed_date
        if linked_permit is not None:
            self.linked_permit = linked_permit
        if files is not None:
            self.files = files

    @property
    def section_81_reference_number(self):
        """Gets the section_81_reference_number of this Section81Response.  # noqa: E501


        :return: The section_81_reference_number of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._section_81_reference_number

    @section_81_reference_number.setter
    def section_81_reference_number(self, section_81_reference_number):
        """Sets the section_81_reference_number of this Section81Response.


        :param section_81_reference_number: The section_81_reference_number of this Section81Response.  # noqa: E501
        :type: str
        """
        if section_81_reference_number is None:
            raise ValueError("Invalid value for `section_81_reference_number`, must not be `None`")  # noqa: E501

        self._section_81_reference_number = section_81_reference_number

    @property
    def date_created(self):
        """Gets the date_created of this Section81Response.  # noqa: E501


        :return: The date_created of this Section81Response.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Section81Response.


        :param date_created: The date_created of this Section81Response.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def location_description(self):
        """Gets the location_description of this Section81Response.  # noqa: E501


        :return: The location_description of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description):
        """Sets the location_description of this Section81Response.


        :param location_description: The location_description of this Section81Response.  # noqa: E501
        :type: str
        """
        if location_description is None:
            raise ValueError("Invalid value for `location_description`, must not be `None`")  # noqa: E501

        self._location_description = location_description

    @property
    def section_81_severity(self):
        """Gets the section_81_severity of this Section81Response.  # noqa: E501


        :return: The section_81_severity of this Section81Response.  # noqa: E501
        :rtype: Section81SeverityResponse
        """
        return self._section_81_severity

    @section_81_severity.setter
    def section_81_severity(self, section_81_severity):
        """Sets the section_81_severity of this Section81Response.


        :param section_81_severity: The section_81_severity of this Section81Response.  # noqa: E501
        :type: Section81SeverityResponse
        """

        self._section_81_severity = section_81_severity

    @property
    def section_81_severity_string(self):
        """Gets the section_81_severity_string of this Section81Response.  # noqa: E501


        :return: The section_81_severity_string of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._section_81_severity_string

    @section_81_severity_string.setter
    def section_81_severity_string(self, section_81_severity_string):
        """Sets the section_81_severity_string of this Section81Response.


        :param section_81_severity_string: The section_81_severity_string of this Section81Response.  # noqa: E501
        :type: str
        """

        self._section_81_severity_string = section_81_severity_string

    @property
    def section_81_status(self):
        """Gets the section_81_status of this Section81Response.  # noqa: E501


        :return: The section_81_status of this Section81Response.  # noqa: E501
        :rtype: Section81StatusResponse
        """
        return self._section_81_status

    @section_81_status.setter
    def section_81_status(self, section_81_status):
        """Sets the section_81_status of this Section81Response.


        :param section_81_status: The section_81_status of this Section81Response.  # noqa: E501
        :type: Section81StatusResponse
        """
        if section_81_status is None:
            raise ValueError("Invalid value for `section_81_status`, must not be `None`")  # noqa: E501

        self._section_81_status = section_81_status

    @property
    def section_81_status_string(self):
        """Gets the section_81_status_string of this Section81Response.  # noqa: E501


        :return: The section_81_status_string of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._section_81_status_string

    @section_81_status_string.setter
    def section_81_status_string(self, section_81_status_string):
        """Sets the section_81_status_string of this Section81Response.


        :param section_81_status_string: The section_81_status_string of this Section81Response.  # noqa: E501
        :type: str
        """
        if section_81_status_string is None:
            raise ValueError("Invalid value for `section_81_status_string`, must not be `None`")  # noqa: E501

        self._section_81_status_string = section_81_status_string

    @property
    def section_81_type(self):
        """Gets the section_81_type of this Section81Response.  # noqa: E501


        :return: The section_81_type of this Section81Response.  # noqa: E501
        :rtype: Section81TypeResponse
        """
        return self._section_81_type

    @section_81_type.setter
    def section_81_type(self, section_81_type):
        """Sets the section_81_type of this Section81Response.


        :param section_81_type: The section_81_type of this Section81Response.  # noqa: E501
        :type: Section81TypeResponse
        """
        if section_81_type is None:
            raise ValueError("Invalid value for `section_81_type`, must not be `None`")  # noqa: E501

        self._section_81_type = section_81_type

    @property
    def section_81_type_string(self):
        """Gets the section_81_type_string of this Section81Response.  # noqa: E501


        :return: The section_81_type_string of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._section_81_type_string

    @section_81_type_string.setter
    def section_81_type_string(self, section_81_type_string):
        """Sets the section_81_type_string of this Section81Response.


        :param section_81_type_string: The section_81_type_string of this Section81Response.  # noqa: E501
        :type: str
        """
        if section_81_type_string is None:
            raise ValueError("Invalid value for `section_81_type_string`, must not be `None`")  # noqa: E501

        self._section_81_type_string = section_81_type_string

    @property
    def work_reference_number(self):
        """Gets the work_reference_number of this Section81Response.  # noqa: E501


        :return: The work_reference_number of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._work_reference_number

    @work_reference_number.setter
    def work_reference_number(self, work_reference_number):
        """Sets the work_reference_number of this Section81Response.


        :param work_reference_number: The work_reference_number of this Section81Response.  # noqa: E501
        :type: str
        """
        if work_reference_number is None:
            raise ValueError("Invalid value for `work_reference_number`, must not be `None`")  # noqa: E501

        self._work_reference_number = work_reference_number

    @property
    def usrn(self):
        """Gets the usrn of this Section81Response.  # noqa: E501


        :return: The usrn of this Section81Response.  # noqa: E501
        :rtype: float
        """
        return self._usrn

    @usrn.setter
    def usrn(self, usrn):
        """Sets the usrn of this Section81Response.


        :param usrn: The usrn of this Section81Response.  # noqa: E501
        :type: float
        """
        if usrn is None:
            raise ValueError("Invalid value for `usrn`, must not be `None`")  # noqa: E501

        self._usrn = usrn

    @property
    def street_name(self):
        """Gets the street_name of this Section81Response.  # noqa: E501


        :return: The street_name of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this Section81Response.


        :param street_name: The street_name of this Section81Response.  # noqa: E501
        :type: str
        """
        if street_name is None:
            raise ValueError("Invalid value for `street_name`, must not be `None`")  # noqa: E501

        self._street_name = street_name

    @property
    def town(self):
        """Gets the town of this Section81Response.  # noqa: E501


        :return: The town of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._town

    @town.setter
    def town(self, town):
        """Sets the town of this Section81Response.


        :param town: The town of this Section81Response.  # noqa: E501
        :type: str
        """

        self._town = town

    @property
    def area(self):
        """Gets the area of this Section81Response.  # noqa: E501


        :return: The area of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Section81Response.


        :param area: The area of this Section81Response.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def road_category(self):
        """Gets the road_category of this Section81Response.  # noqa: E501


        :return: The road_category of this Section81Response.  # noqa: E501
        :rtype: float
        """
        return self._road_category

    @road_category.setter
    def road_category(self, road_category):
        """Sets the road_category of this Section81Response.


        :param road_category: The road_category of this Section81Response.  # noqa: E501
        :type: float
        """
        if road_category is None:
            raise ValueError("Invalid value for `road_category`, must not be `None`")  # noqa: E501

        self._road_category = road_category

    @property
    def works_coordinates(self):
        """Gets the works_coordinates of this Section81Response.  # noqa: E501


        :return: The works_coordinates of this Section81Response.  # noqa: E501
        :rtype: object
        """
        return self._works_coordinates

    @works_coordinates.setter
    def works_coordinates(self, works_coordinates):
        """Sets the works_coordinates of this Section81Response.


        :param works_coordinates: The works_coordinates of this Section81Response.  # noqa: E501
        :type: object
        """
        if works_coordinates is None:
            raise ValueError("Invalid value for `works_coordinates`, must not be `None`")  # noqa: E501

        self._works_coordinates = works_coordinates

    @property
    def highway_authority(self):
        """Gets the highway_authority of this Section81Response.  # noqa: E501


        :return: The highway_authority of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._highway_authority

    @highway_authority.setter
    def highway_authority(self, highway_authority):
        """Sets the highway_authority of this Section81Response.


        :param highway_authority: The highway_authority of this Section81Response.  # noqa: E501
        :type: str
        """
        if highway_authority is None:
            raise ValueError("Invalid value for `highway_authority`, must not be `None`")  # noqa: E501

        self._highway_authority = highway_authority

    @property
    def highway_authority_swa_code(self):
        """Gets the highway_authority_swa_code of this Section81Response.  # noqa: E501


        :return: The highway_authority_swa_code of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._highway_authority_swa_code

    @highway_authority_swa_code.setter
    def highway_authority_swa_code(self, highway_authority_swa_code):
        """Sets the highway_authority_swa_code of this Section81Response.


        :param highway_authority_swa_code: The highway_authority_swa_code of this Section81Response.  # noqa: E501
        :type: str
        """
        if highway_authority_swa_code is None:
            raise ValueError("Invalid value for `highway_authority_swa_code`, must not be `None`")  # noqa: E501

        self._highway_authority_swa_code = highway_authority_swa_code

    @property
    def promoter_organisation(self):
        """Gets the promoter_organisation of this Section81Response.  # noqa: E501


        :return: The promoter_organisation of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._promoter_organisation

    @promoter_organisation.setter
    def promoter_organisation(self, promoter_organisation):
        """Sets the promoter_organisation of this Section81Response.


        :param promoter_organisation: The promoter_organisation of this Section81Response.  # noqa: E501
        :type: str
        """
        if promoter_organisation is None:
            raise ValueError("Invalid value for `promoter_organisation`, must not be `None`")  # noqa: E501

        self._promoter_organisation = promoter_organisation

    @property
    def promoter_swa_code(self):
        """Gets the promoter_swa_code of this Section81Response.  # noqa: E501


        :return: The promoter_swa_code of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._promoter_swa_code

    @promoter_swa_code.setter
    def promoter_swa_code(self, promoter_swa_code):
        """Sets the promoter_swa_code of this Section81Response.


        :param promoter_swa_code: The promoter_swa_code of this Section81Response.  # noqa: E501
        :type: str
        """
        if promoter_swa_code is None:
            raise ValueError("Invalid value for `promoter_swa_code`, must not be `None`")  # noqa: E501

        self._promoter_swa_code = promoter_swa_code

    @property
    def workstream_prefix(self):
        """Gets the workstream_prefix of this Section81Response.  # noqa: E501


        :return: The workstream_prefix of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._workstream_prefix

    @workstream_prefix.setter
    def workstream_prefix(self, workstream_prefix):
        """Sets the workstream_prefix of this Section81Response.


        :param workstream_prefix: The workstream_prefix of this Section81Response.  # noqa: E501
        :type: str
        """
        if workstream_prefix is None:
            raise ValueError("Invalid value for `workstream_prefix`, must not be `None`")  # noqa: E501

        self._workstream_prefix = workstream_prefix

    @property
    def location_types(self):
        """Gets the location_types of this Section81Response.  # noqa: E501


        :return: The location_types of this Section81Response.  # noqa: E501
        :rtype: list[LocationTypeResponse]
        """
        return self._location_types

    @location_types.setter
    def location_types(self, location_types):
        """Sets the location_types of this Section81Response.


        :param location_types: The location_types of this Section81Response.  # noqa: E501
        :type: list[LocationTypeResponse]
        """
        if location_types is None:
            raise ValueError("Invalid value for `location_types`, must not be `None`")  # noqa: E501

        self._location_types = location_types

    @property
    def location_types_string(self):
        """Gets the location_types_string of this Section81Response.  # noqa: E501


        :return: The location_types_string of this Section81Response.  # noqa: E501
        :rtype: list[str]
        """
        return self._location_types_string

    @location_types_string.setter
    def location_types_string(self, location_types_string):
        """Sets the location_types_string of this Section81Response.


        :param location_types_string: The location_types_string of this Section81Response.  # noqa: E501
        :type: list[str]
        """
        if location_types_string is None:
            raise ValueError("Invalid value for `location_types_string`, must not be `None`")  # noqa: E501

        self._location_types_string = location_types_string

    @property
    def inspection_date(self):
        """Gets the inspection_date of this Section81Response.  # noqa: E501


        :return: The inspection_date of this Section81Response.  # noqa: E501
        :rtype: datetime
        """
        return self._inspection_date

    @inspection_date.setter
    def inspection_date(self, inspection_date):
        """Sets the inspection_date of this Section81Response.


        :param inspection_date: The inspection_date of this Section81Response.  # noqa: E501
        :type: datetime
        """
        if inspection_date is None:
            raise ValueError("Invalid value for `inspection_date`, must not be `None`")  # noqa: E501

        self._inspection_date = inspection_date

    @property
    def other_type_details(self):
        """Gets the other_type_details of this Section81Response.  # noqa: E501


        :return: The other_type_details of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._other_type_details

    @other_type_details.setter
    def other_type_details(self, other_type_details):
        """Sets the other_type_details of this Section81Response.


        :param other_type_details: The other_type_details of this Section81Response.  # noqa: E501
        :type: str
        """

        self._other_type_details = other_type_details

    @property
    def made_safe_by_ha(self):
        """Gets the made_safe_by_ha of this Section81Response.  # noqa: E501


        :return: The made_safe_by_ha of this Section81Response.  # noqa: E501
        :rtype: bool
        """
        return self._made_safe_by_ha

    @made_safe_by_ha.setter
    def made_safe_by_ha(self, made_safe_by_ha):
        """Sets the made_safe_by_ha of this Section81Response.


        :param made_safe_by_ha: The made_safe_by_ha of this Section81Response.  # noqa: E501
        :type: bool
        """

        self._made_safe_by_ha = made_safe_by_ha

    @property
    def inspector_name(self):
        """Gets the inspector_name of this Section81Response.  # noqa: E501


        :return: The inspector_name of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._inspector_name

    @inspector_name.setter
    def inspector_name(self, inspector_name):
        """Sets the inspector_name of this Section81Response.


        :param inspector_name: The inspector_name of this Section81Response.  # noqa: E501
        :type: str
        """

        self._inspector_name = inspector_name

    @property
    def inspector_contact_number(self):
        """Gets the inspector_contact_number of this Section81Response.  # noqa: E501


        :return: The inspector_contact_number of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._inspector_contact_number

    @inspector_contact_number.setter
    def inspector_contact_number(self, inspector_contact_number):
        """Sets the inspector_contact_number of this Section81Response.


        :param inspector_contact_number: The inspector_contact_number of this Section81Response.  # noqa: E501
        :type: str
        """

        self._inspector_contact_number = inspector_contact_number

    @property
    def additional_details(self):
        """Gets the additional_details of this Section81Response.  # noqa: E501


        :return: The additional_details of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this Section81Response.


        :param additional_details: The additional_details of this Section81Response.  # noqa: E501
        :type: str
        """
        if additional_details is None:
            raise ValueError("Invalid value for `additional_details`, must not be `None`")  # noqa: E501

        self._additional_details = additional_details

    @property
    def status_changed_date(self):
        """Gets the status_changed_date of this Section81Response.  # noqa: E501


        :return: The status_changed_date of this Section81Response.  # noqa: E501
        :rtype: datetime
        """
        return self._status_changed_date

    @status_changed_date.setter
    def status_changed_date(self, status_changed_date):
        """Sets the status_changed_date of this Section81Response.


        :param status_changed_date: The status_changed_date of this Section81Response.  # noqa: E501
        :type: datetime
        """
        if status_changed_date is None:
            raise ValueError("Invalid value for `status_changed_date`, must not be `None`")  # noqa: E501

        self._status_changed_date = status_changed_date

    @property
    def promoter_response(self):
        """Gets the promoter_response of this Section81Response.  # noqa: E501


        :return: The promoter_response of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._promoter_response

    @promoter_response.setter
    def promoter_response(self, promoter_response):
        """Sets the promoter_response of this Section81Response.


        :param promoter_response: The promoter_response of this Section81Response.  # noqa: E501
        :type: str
        """

        self._promoter_response = promoter_response

    @property
    def section_81_work_type(self):
        """Gets the section_81_work_type of this Section81Response.  # noqa: E501


        :return: The section_81_work_type of this Section81Response.  # noqa: E501
        :rtype: AllOfSection81ResponseSection81WorkType
        """
        return self._section_81_work_type

    @section_81_work_type.setter
    def section_81_work_type(self, section_81_work_type):
        """Sets the section_81_work_type of this Section81Response.


        :param section_81_work_type: The section_81_work_type of this Section81Response.  # noqa: E501
        :type: AllOfSection81ResponseSection81WorkType
        """

        self._section_81_work_type = section_81_work_type

    @property
    def section_81_work_type_string(self):
        """Gets the section_81_work_type_string of this Section81Response.  # noqa: E501


        :return: The section_81_work_type_string of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._section_81_work_type_string

    @section_81_work_type_string.setter
    def section_81_work_type_string(self, section_81_work_type_string):
        """Sets the section_81_work_type_string of this Section81Response.


        :param section_81_work_type_string: The section_81_work_type_string of this Section81Response.  # noqa: E501
        :type: str
        """

        self._section_81_work_type_string = section_81_work_type_string

    @property
    def promoter_status(self):
        """Gets the promoter_status of this Section81Response.  # noqa: E501


        :return: The promoter_status of this Section81Response.  # noqa: E501
        :rtype: AllOfSection81ResponsePromoterStatus
        """
        return self._promoter_status

    @promoter_status.setter
    def promoter_status(self, promoter_status):
        """Sets the promoter_status of this Section81Response.


        :param promoter_status: The promoter_status of this Section81Response.  # noqa: E501
        :type: AllOfSection81ResponsePromoterStatus
        """

        self._promoter_status = promoter_status

    @property
    def promoter_status_string(self):
        """Gets the promoter_status_string of this Section81Response.  # noqa: E501


        :return: The promoter_status_string of this Section81Response.  # noqa: E501
        :rtype: str
        """
        return self._promoter_status_string

    @promoter_status_string.setter
    def promoter_status_string(self, promoter_status_string):
        """Sets the promoter_status_string of this Section81Response.


        :param promoter_status_string: The promoter_status_string of this Section81Response.  # noqa: E501
        :type: str
        """

        self._promoter_status_string = promoter_status_string

    @property
    def promoter_status_changed_date(self):
        """Gets the promoter_status_changed_date of this Section81Response.  # noqa: E501


        :return: The promoter_status_changed_date of this Section81Response.  # noqa: E501
        :rtype: datetime
        """
        return self._promoter_status_changed_date

    @promoter_status_changed_date.setter
    def promoter_status_changed_date(self, promoter_status_changed_date):
        """Sets the promoter_status_changed_date of this Section81Response.


        :param promoter_status_changed_date: The promoter_status_changed_date of this Section81Response.  # noqa: E501
        :type: datetime
        """

        self._promoter_status_changed_date = promoter_status_changed_date

    @property
    def linked_permit(self):
        """Gets the linked_permit of this Section81Response.  # noqa: E501


        :return: The linked_permit of this Section81Response.  # noqa: E501
        :rtype: AllOfSection81ResponseLinkedPermit
        """
        return self._linked_permit

    @linked_permit.setter
    def linked_permit(self, linked_permit):
        """Sets the linked_permit of this Section81Response.


        :param linked_permit: The linked_permit of this Section81Response.  # noqa: E501
        :type: AllOfSection81ResponseLinkedPermit
        """

        self._linked_permit = linked_permit

    @property
    def files(self):
        """Gets the files of this Section81Response.  # noqa: E501


        :return: The files of this Section81Response.  # noqa: E501
        :rtype: list[FileSummaryResponse]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Section81Response.


        :param files: The files of this Section81Response.  # noqa: E501
        :type: list[FileSummaryResponse]
        """

        self._files = files

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
        if issubclass(Section81Response, dict):
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
        if not isinstance(other, Section81Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
