# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from spicerack.models.metakernels import Metakernels  # noqa: E501
from spicerack.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_metakernel(self):
        """Test case for get_metakernel

        Get a specific kernel
        """
        query_string = [('mission', 'mission_example'),
                        ('year', 'year_example'),
                        ('version', 'latest')]
        response = self.client.open(
            '/v1/metalkernels/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
