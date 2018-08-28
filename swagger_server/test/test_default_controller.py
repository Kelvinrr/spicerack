# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metakernal import Metakernal  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_metakernel(self):
        """Test case for get_metakernel

        Returns Kernels from query params
        """
        query_string = [('year', 'year_example'),
                        ('version', 'latest')]
        response = self.client.open(
            '/v1/missions/{mission}/metakernals/'.format(mission='mission_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
