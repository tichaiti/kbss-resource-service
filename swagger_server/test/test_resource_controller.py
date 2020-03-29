# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestResourceController(BaseTestCase):
    """ResourceController integration test stubs"""

    def test_api_resource_data_type_get(self):
        """Test case for api_resource_data_type_get

        Gets list of resources
        """
        query_string = [('page', 1),
                        ('per_page', 100)]
        response = self.client.open(
            '/api/resource/{dataType}'.format(data_type='data_type_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_post(self):
        """Test case for api_resource_data_type_post

        Create resource
        """
        body = None
        response = self.client.open(
            '/api/resource/{dataType}'.format(data_type='data_type_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_resource_id_delete(self):
        """Test case for api_resource_data_type_resource_id_delete

        Deletes a specific resource by id
        """
        response = self.client.open(
            '/api/resource/{dataType}/{resourceId}'.format(data_type='data_type_example', resource_id='resource_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_resource_id_get(self):
        """Test case for api_resource_data_type_resource_id_get

        Gets a specific resource by id
        """
        response = self.client.open(
            '/api/resource/{dataType}/{resourceId}'.format(data_type='data_type_example', resource_id='resource_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_resource_id_put(self):
        """Test case for api_resource_data_type_resource_id_put

        Update resource
        """
        body = None
        response = self.client.open(
            '/api/resource/{dataType}/{resourceId}'.format(data_type='data_type_example', resource_id='resource_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
