# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.missions import Missions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMissionsController(BaseTestCase):
    """MissionsController integration test stubs"""

    def test_get_home_naif(self):
        """Test case for get_home_naif

        List of available missions in naif format
        """
        response = self.client.open(
            '/api/1.0/home/naif',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_misc(self):
        """Test case for get_misc

        List of the available misc. files for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/misc'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mission_endpoints(self):
        """Test case for get_mission_endpoints

        List of the available endpoints for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_missions(self):
        """Test case for get_missions

        List of available missions (Human-Readable)
        """
        response = self.client.open(
            '/api/1.0/home/missions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
