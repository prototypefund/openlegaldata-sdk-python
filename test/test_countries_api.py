# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: api@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import oldp_client
from oldp_client.api.countries_api import CountriesApi  # noqa: E501
from oldp_client.rest import ApiException


class TestCountriesApi(unittest.TestCase):
    """CountriesApi unit test stubs"""

    def setUp(self):
        self.api = oldp_client.api.countries_api.CountriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_countries_create(self):
        """Test case for countries_create

        """
        pass

    def test_countries_delete(self):
        """Test case for countries_delete

        """
        pass

    def test_countries_list(self):
        """Test case for countries_list

        """
        pass

    def test_countries_partial_update(self):
        """Test case for countries_partial_update

        """
        pass

    def test_countries_read(self):
        """Test case for countries_read

        """
        pass

    def test_countries_update(self):
        """Test case for countries_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
