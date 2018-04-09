# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.missions import Missions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMissionsController(BaseTestCase):
    """MissionsController integration test stubs"""

    def test_find_missio_endpoints(self):
        """Test case for find_missio_endpoints

        List of the next available endpoints for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_naif_names(self):
        """Test case for get_naif_names

        List of available missions (NAIF technical names)
        """
        response = self.client.open(
            '/api/1.0/home/missions/naif',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
