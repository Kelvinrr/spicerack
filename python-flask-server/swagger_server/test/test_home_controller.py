# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dataframe import Dataframe  # noqa: E501
from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.update import Update  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHomeController(BaseTestCase):
    """HomeController integration test stubs"""

    def test_get_home_dataframe(self):
        """Test case for get_home_dataframe

        Dataframe of the home directory in JSON
        """
        response = self.client.open(
            '/api/1.0/home/dataframe',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_home_endpoints(self):
        """Test case for get_home_endpoints

        List of available endpoints from home directory
        """
        response = self.client.open(
            '/api/1.0/home',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_home_hash(self):
        """Test case for get_home_hash

        Hash of the home dataframe
        """
        response = self.client.open(
            '/api/1.0/home/hash',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_refresh_db(self):
        """Test case for refresh_db

        Refresh database of file info
        """
        response = self.client.open(
            '/api/1.0/home/refresh',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
