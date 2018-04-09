# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.update import Update  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSyncController(BaseTestCase):
    """SyncController integration test stubs"""

    def test_get_public_ssh(self):
        """Test case for get_public_ssh

        Public SSH Key of User
        """
        response = self.client.open(
            '/api/1.0/update/{user}/ssh'.format(user='user_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_nodes(self):
        """Test case for list_nodes

        List of available nodes
        """
        response = self.client.open(
            '/api/1.0/update',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sync_nodes(self):
        """Test case for sync_nodes

        Synchronize data with another node
        """
        response = self.client.open(
            '/api/1.0/update/{user}/sync'.format(user='user_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
