# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CaseAnnotation(object):
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
        'id': 'int',
        'belongs_to': 'int',
        'label': 'int',
        'value_str': 'str',
        'value_int': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'belongs_to': 'belongs_to',
        'label': 'label',
        'value_str': 'value_str',
        'value_int': 'value_int',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, belongs_to=None, label=None, value_str=None, value_int=None, created_at=None, updated_at=None):  # noqa: E501
        """CaseAnnotation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._belongs_to = None
        self._label = None
        self._value_str = None
        self._value_int = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.belongs_to = belongs_to
        self.label = label
        if value_str is not None:
            self.value_str = value_str
        if value_int is not None:
            self.value_int = value_int
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this CaseAnnotation.  # noqa: E501


        :return: The id of this CaseAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CaseAnnotation.


        :param id: The id of this CaseAnnotation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def belongs_to(self):
        """Gets the belongs_to of this CaseAnnotation.  # noqa: E501


        :return: The belongs_to of this CaseAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._belongs_to

    @belongs_to.setter
    def belongs_to(self, belongs_to):
        """Sets the belongs_to of this CaseAnnotation.


        :param belongs_to: The belongs_to of this CaseAnnotation.  # noqa: E501
        :type: int
        """
        if belongs_to is None:
            raise ValueError("Invalid value for `belongs_to`, must not be `None`")  # noqa: E501

        self._belongs_to = belongs_to

    @property
    def label(self):
        """Gets the label of this CaseAnnotation.  # noqa: E501


        :return: The label of this CaseAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CaseAnnotation.


        :param label: The label of this CaseAnnotation.  # noqa: E501
        :type: int
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def value_str(self):
        """Gets the value_str of this CaseAnnotation.  # noqa: E501


        :return: The value_str of this CaseAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._value_str

    @value_str.setter
    def value_str(self, value_str):
        """Sets the value_str of this CaseAnnotation.


        :param value_str: The value_str of this CaseAnnotation.  # noqa: E501
        :type: str
        """
        if value_str is not None and len(value_str) > 250:
            raise ValueError("Invalid value for `value_str`, length must be less than or equal to `250`")  # noqa: E501

        self._value_str = value_str

    @property
    def value_int(self):
        """Gets the value_int of this CaseAnnotation.  # noqa: E501


        :return: The value_int of this CaseAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._value_int

    @value_int.setter
    def value_int(self, value_int):
        """Sets the value_int of this CaseAnnotation.


        :param value_int: The value_int of this CaseAnnotation.  # noqa: E501
        :type: int
        """
        if value_int is not None and value_int > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `value_int`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if value_int is not None and value_int < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `value_int`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._value_int = value_int

    @property
    def created_at(self):
        """Gets the created_at of this CaseAnnotation.  # noqa: E501

        Entry is created at this date time  # noqa: E501

        :return: The created_at of this CaseAnnotation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CaseAnnotation.

        Entry is created at this date time  # noqa: E501

        :param created_at: The created_at of this CaseAnnotation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CaseAnnotation.  # noqa: E501

        Date time of last change  # noqa: E501

        :return: The updated_at of this CaseAnnotation.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CaseAnnotation.

        Date time of last change  # noqa: E501

        :param updated_at: The updated_at of this CaseAnnotation.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CaseAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
