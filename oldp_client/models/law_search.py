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


class LawSearch(object):
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
        'title': 'str',
        'book_code': 'str',
        'text': 'str',
        'id': 'str'
    }

    attribute_map = {
        'title': 'title',
        'book_code': 'book_code',
        'text': 'text',
        'id': 'id'
    }

    def __init__(self, title=None, book_code=None, text=None, id=None):  # noqa: E501
        """LawSearch - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._book_code = None
        self._text = None
        self._id = None
        self.discriminator = None

        if title is not None:
            self.title = title
        self.book_code = book_code
        self.text = text
        if id is not None:
            self.id = id

    @property
    def title(self):
        """Gets the title of this LawSearch.  # noqa: E501

        Verbose title of law  # noqa: E501

        :return: The title of this LawSearch.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LawSearch.

        Verbose title of law  # noqa: E501

        :param title: The title of this LawSearch.  # noqa: E501
        :type: str
        """
        if title is not None and len(title) > 200:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `200`")  # noqa: E501

        self._title = title

    @property
    def book_code(self):
        """Gets the book_code of this LawSearch.  # noqa: E501


        :return: The book_code of this LawSearch.  # noqa: E501
        :rtype: str
        """
        return self._book_code

    @book_code.setter
    def book_code(self, book_code):
        """Sets the book_code of this LawSearch.


        :param book_code: The book_code of this LawSearch.  # noqa: E501
        :type: str
        """
        if book_code is None:
            raise ValueError("Invalid value for `book_code`, must not be `None`")  # noqa: E501

        self._book_code = book_code

    @property
    def text(self):
        """Gets the text of this LawSearch.  # noqa: E501


        :return: The text of this LawSearch.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this LawSearch.


        :param text: The text of this LawSearch.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def id(self):
        """Gets the id of this LawSearch.  # noqa: E501


        :return: The id of this LawSearch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LawSearch.


        :param id: The id of this LawSearch.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(LawSearch, dict):
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
        if not isinstance(other, LawSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
