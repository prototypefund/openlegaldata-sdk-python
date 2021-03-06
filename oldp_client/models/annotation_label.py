# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website. https://openlegaldata.io/  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AnnotationLabel(object):
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
        'owner': 'str',
        'trusted': 'str',
        'name': 'str',
        'slug': 'str',
        'private': 'bool',
        'many_annotations_per_label': 'bool',
        'use_marker': 'bool',
        'annotation_value_type': 'str',
        'color': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'trusted': 'trusted',
        'name': 'name',
        'slug': 'slug',
        'private': 'private',
        'many_annotations_per_label': 'many_annotations_per_label',
        'use_marker': 'use_marker',
        'annotation_value_type': 'annotation_value_type',
        'color': 'color',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, owner=None, trusted=None, name=None, slug=None, private=None, many_annotations_per_label=None, use_marker=None, annotation_value_type=None, color=None, created_at=None, updated_at=None):  # noqa: E501
        """AnnotationLabel - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._owner = None
        self._trusted = None
        self._name = None
        self._slug = None
        self._private = None
        self._many_annotations_per_label = None
        self._use_marker = None
        self._annotation_value_type = None
        self._color = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if trusted is not None:
            self.trusted = trusted
        self.name = name
        self.slug = slug
        if private is not None:
            self.private = private
        if many_annotations_per_label is not None:
            self.many_annotations_per_label = many_annotations_per_label
        if use_marker is not None:
            self.use_marker = use_marker
        if annotation_value_type is not None:
            self.annotation_value_type = annotation_value_type
        if color is not None:
            self.color = color
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this AnnotationLabel.  # noqa: E501


        :return: The id of this AnnotationLabel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnnotationLabel.


        :param id: The id of this AnnotationLabel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this AnnotationLabel.  # noqa: E501


        :return: The owner of this AnnotationLabel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AnnotationLabel.


        :param owner: The owner of this AnnotationLabel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def trusted(self):
        """Gets the trusted of this AnnotationLabel.  # noqa: E501


        :return: The trusted of this AnnotationLabel.  # noqa: E501
        :rtype: str
        """
        return self._trusted

    @trusted.setter
    def trusted(self, trusted):
        """Sets the trusted of this AnnotationLabel.


        :param trusted: The trusted of this AnnotationLabel.  # noqa: E501
        :type: str
        """

        self._trusted = trusted

    @property
    def name(self):
        """Gets the name of this AnnotationLabel.  # noqa: E501

        Verbose name, e.g. This Awesome annotation  # noqa: E501

        :return: The name of this AnnotationLabel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnnotationLabel.

        Verbose name, e.g. This Awesome annotation  # noqa: E501

        :param name: The name of this AnnotationLabel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this AnnotationLabel.  # noqa: E501

        Identifier, e.g. this-awesome-annotation  # noqa: E501

        :return: The slug of this AnnotationLabel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this AnnotationLabel.

        Identifier, e.g. this-awesome-annotation  # noqa: E501

        :param slug: The slug of this AnnotationLabel.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and len(slug) > 100:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `100`")  # noqa: E501
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def private(self):
        """Gets the private of this AnnotationLabel.  # noqa: E501

        Private annotations are only visible to its author  # noqa: E501

        :return: The private of this AnnotationLabel.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this AnnotationLabel.

        Private annotations are only visible to its author  # noqa: E501

        :param private: The private of this AnnotationLabel.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def many_annotations_per_label(self):
        """Gets the many_annotations_per_label of this AnnotationLabel.  # noqa: E501

        A content object can have more than one annotation per label  # noqa: E501

        :return: The many_annotations_per_label of this AnnotationLabel.  # noqa: E501
        :rtype: bool
        """
        return self._many_annotations_per_label

    @many_annotations_per_label.setter
    def many_annotations_per_label(self, many_annotations_per_label):
        """Sets the many_annotations_per_label of this AnnotationLabel.

        A content object can have more than one annotation per label  # noqa: E501

        :param many_annotations_per_label: The many_annotations_per_label of this AnnotationLabel.  # noqa: E501
        :type: bool
        """

        self._many_annotations_per_label = many_annotations_per_label

    @property
    def use_marker(self):
        """Gets the use_marker of this AnnotationLabel.  # noqa: E501

        Marker annotations are extracted from the text content and have a position in the text  # noqa: E501

        :return: The use_marker of this AnnotationLabel.  # noqa: E501
        :rtype: bool
        """
        return self._use_marker

    @use_marker.setter
    def use_marker(self, use_marker):
        """Sets the use_marker of this AnnotationLabel.

        Marker annotations are extracted from the text content and have a position in the text  # noqa: E501

        :param use_marker: The use_marker of this AnnotationLabel.  # noqa: E501
        :type: bool
        """

        self._use_marker = use_marker

    @property
    def annotation_value_type(self):
        """Gets the annotation_value_type of this AnnotationLabel.  # noqa: E501

        Annotation values must be in this data type  # noqa: E501

        :return: The annotation_value_type of this AnnotationLabel.  # noqa: E501
        :rtype: str
        """
        return self._annotation_value_type

    @annotation_value_type.setter
    def annotation_value_type(self, annotation_value_type):
        """Sets the annotation_value_type of this AnnotationLabel.

        Annotation values must be in this data type  # noqa: E501

        :param annotation_value_type: The annotation_value_type of this AnnotationLabel.  # noqa: E501
        :type: str
        """
        allowed_values = ["str", "int"]  # noqa: E501
        if annotation_value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `annotation_value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(annotation_value_type, allowed_values)
            )

        self._annotation_value_type = annotation_value_type

    @property
    def color(self):
        """Gets the color of this AnnotationLabel.  # noqa: E501


        :return: The color of this AnnotationLabel.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AnnotationLabel.


        :param color: The color of this AnnotationLabel.  # noqa: E501
        :type: str
        """
        if color is not None and len(color) > 18:
            raise ValueError("Invalid value for `color`, length must be less than or equal to `18`")  # noqa: E501
        if color is not None and not re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', color):  # noqa: E501
            raise ValueError(r"Invalid value for `color`, must be a follow pattern or equal to `/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/`")  # noqa: E501

        self._color = color

    @property
    def created_at(self):
        """Gets the created_at of this AnnotationLabel.  # noqa: E501

        Entry is created at this date time  # noqa: E501

        :return: The created_at of this AnnotationLabel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AnnotationLabel.

        Entry is created at this date time  # noqa: E501

        :param created_at: The created_at of this AnnotationLabel.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AnnotationLabel.  # noqa: E501

        Date time of last change  # noqa: E501

        :return: The updated_at of this AnnotationLabel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AnnotationLabel.

        Date time of last change  # noqa: E501

        :param updated_at: The updated_at of this AnnotationLabel.  # noqa: E501
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
        if issubclass(AnnotationLabel, dict):
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
        if not isinstance(other, AnnotationLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
