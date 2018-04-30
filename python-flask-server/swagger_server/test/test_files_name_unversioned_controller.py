# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFilesNameUnversionedController(BaseTestCase):
    """FilesNameUnversionedController integration test stubs"""

    def test_get_fn_newest(self):
        """Test case for get_fn_newest

        Newest version of a given file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{name}/newest'.format(mission='mission_example', kernel='kernel_example', name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fn_year(self):
        """Test case for get_fn_year

        Newest version of a given file
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{name}/{year}'.format(mission='mission_example', kernel='kernel_example', name='name_example', year=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fn_year_newest(self):
        """Test case for get_fn_year_newest

        Newest file for a given year
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/files/{name}/{year}/newest'.format(mission='mission_example', kernel='kernel_example', name='name_example', year=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
