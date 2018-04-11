# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.raw import Raw  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetakernelsController(BaseTestCase):
    """MetakernelsController integration test stubs"""

    def test_get_metakernels(self):
        """Test case for get_metakernels

        List of available metakernels for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mk_hash(self):
        """Test case for get_mk_hash

        Hashed contents of a given metakernel file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{file}/hash'.format(mission='mission_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mk_newest(self):
        """Test case for get_mk_newest

        Newest metakernels for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/newest'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mk_path(self):
        """Test case for get_mk_path

        Filepath of a given metakernel file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{file}/path'.format(mission='mission_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mk_raw(self):
        """Test case for get_mk_raw

        Raw contents of a given metakernel file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{file}/raw'.format(mission='mission_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mk_year(self):
        """Test case for get_mk_year

        List of available metakernels for a given mission and year
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{year}'.format(mission='mission_example', year=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mk_year_newest(self):
        """Test case for get_mk_year_newest

        Newest metakernels for a given mission and year
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/metakernels/{year}/newest'.format(mission='mission_example', year=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
