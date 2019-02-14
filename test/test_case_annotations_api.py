# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: hello@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import oldp_client
from oldp_client.api.case_annotations_api import CaseAnnotationsApi  # noqa: E501
from oldp_client.rest import ApiException


class TestCaseAnnotationsApi(unittest.TestCase):
    """CaseAnnotationsApi unit test stubs"""

    def setUp(self):
        self.api = oldp_client.api.case_annotations_api.CaseAnnotationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_case_annotations_create(self):
        """Test case for case_annotations_create

        """
        pass

    def test_case_annotations_delete(self):
        """Test case for case_annotations_delete

        """
        pass

    def test_case_annotations_list(self):
        """Test case for case_annotations_list

        """
        pass

    def test_case_annotations_partial_update(self):
        """Test case for case_annotations_partial_update

        """
        pass

    def test_case_annotations_read(self):
        """Test case for case_annotations_read

        """
        pass

    def test_case_annotations_update(self):
        """Test case for case_annotations_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
