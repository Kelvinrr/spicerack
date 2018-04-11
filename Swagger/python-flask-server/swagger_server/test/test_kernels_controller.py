# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.hash import Hash  # noqa: E501
from swagger_server.models.kernels import Kernels  # noqa: E501
from swagger_server.test import BaseTestCase


class TestKernelsController(BaseTestCase):
    """KernelsController integration test stubs"""

    def test_get_kernel_endpoints(self):
        """Test case for get_kernel_endpoints

        List of the available endpoints for a given mission/kernel
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}'.format(mission='mission_example', kernel='kernel_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_kernel_hash(self):
        """Test case for get_kernel_hash

        Hash of a kernel for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels/{kernel}/hash'.format(mission='mission_example', kernel='kernel_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_kernels(self):
        """Test case for get_kernels

        List of available kernels for a given mission
        """
        response = self.client.open(
            '/api/1.0/home/missions/{mission}/kernels'.format(mission='mission_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
