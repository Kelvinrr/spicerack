# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFilesNameVersionedController(BaseTestCase):
    """FilesNameVersionedController integration test stubs"""

    def test_get_file_endpoints(self):
        """Test case for get_file_endpoints

        List of available endpoints for a given versioned file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{file}'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_hash(self):
        """Test case for get_file_hash

        Hashed contents of a given versioned file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{file}/hash'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_path(self):
        """Test case for get_file_path

        Filepath of a given versioned file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{file}/path'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_raw(self):
        """Test case for get_file_raw

        Raw contents of a given versioned file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{file}/raw'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_files(self):
        """Test case for get_files

        List of available files for a given mission/kernel
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files'.format(mission='mission_example', kernel='kernel_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_kernels_newest(self):
        """Test case for get_kernels_newest

        Newest files for a given mission/kernel
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/newest'.format(mission='mission_example', kernel='kernel_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
