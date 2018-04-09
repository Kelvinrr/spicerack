# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metakernels import Metakernels  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetakernelsController(BaseTestCase):
    """MetakernelsController integration test stubs"""

    def test_find_meta_kernels_by_mission(self):
        """Test case for find_meta_kernels_by_mission

        List of available metakernels for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_meta_kernels_by_mission_new(self):
        """Test case for find_meta_kernels_by_mission_new

        List of available metakernels for a given mission, sorted by newest
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/newest'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_meta_kernels_by_mission_year(self):
        """Test case for find_meta_kernels_by_mission_year

        List of available metakernels for a given mission and year
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{year}'.format(mission='mission_example', year=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_meta_kernels_by_mission_year_new(self):
        """Test case for find_meta_kernels_by_mission_year_new

        List of available metakernels for a given mission and year, sorted by newest
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{year}/newest'.format(mission='mission_example', year=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
