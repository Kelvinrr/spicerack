# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

java.io.File  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFilesController(BaseTestCase):
    """FilesController integration test stubs"""

    def test_get_file_by_year(self):
        """Test case for get_file_by_year

        Newest file for a given year
        """
        response = self.client.open(
            '/api/1.0/missions/{mission}/kernels/{kernel}/files/{file}/year/newest'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_hash(self):
        """Test case for get_file_hash

        Hash of file for a given mission/kernel
        """
        response = self.client.open(
            '/api/1.0/missions/{mission}/kernels/{kernel}/files/{file}/hash'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_path(self):
        """Test case for get_file_path

        Filepath of a given file
        """
        response = self.client.open(
            '/api/1.0/missions/{mission}/kernels/{kernel}/files/{file}/filepath'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_raw(self):
        """Test case for get_file_raw

        Raw contents of file for a given mission/kernel
        """
        response = self.client.open(
            '/api/1.0/missions/{mission}/kernels/{kernel}/files/{file}'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_year(self):
        """Test case for get_file_year

        Year for the given file
        """
        response = self.client.open(
            '/api/1.0/missions/{mission}/kernels/{kernel}/files/{file}/year'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_kernel_files(self):
        """Test case for get_kernel_files

        List of available files for a given mission/kernel
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files'.format(mission='mission_example', kernel='kernel_example', file='file_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
