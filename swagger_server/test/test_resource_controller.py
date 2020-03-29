# coding: utf-8

from __future__ import absolute_import

from bson import ObjectId
from flask import json
from six import BytesIO

from swagger_server.config import MONGO_DB
from swagger_server.test import BaseTestCase
from unittest.mock import MagicMock


class TestResourceController(BaseTestCase):
    """ResourceController integration test stubs"""

    def setUp(self):
        MONGO_DB.db = MagicMock()
        MONGO_DB.db.list_collection_names = MagicMock(return_value=['book'])
        MONGO_DB.db['book'].find_one_or_404 = MagicMock(return_value={})
        MONGO_DB.db['book'].find_one_and_delete = MagicMock(return_value={})
        MONGO_DB.db['book'].find_one_and_replace = MagicMock(return_value={})
        fake_cursor = MagicMock()
        fake_cursor.skip = fake_cursor
        fake_cursor.limit = MagicMock(return_value=[])
        MONGO_DB.db['book'].find = MagicMock(return_value=fake_cursor)
        fake_object = MagicMock()
        fake_object.inserted_id = ObjectId('5e80fa3205a436d9f9da019e')
        MONGO_DB.db['book'].insert_one = MagicMock(return_value=fake_object)

    def test_api_resource_data_type_get(self):
        """Test case for api_resource_data_type_get

        Gets list of resources
        """
        query_string = [('page', 1),
                        ('per_page', 100)]
        response = self.client.open(
            '/api/resource/{data_type}'.format(data_type='book'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_post(self):
        """Test case for api_resource_data_type_post

        Create resource
        """
        body = {}
        response = self.client.open(
            '/api/resource/{data_type}'.format(data_type='book'),
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
            '/api/resource/{data_type}/{resource_id}'.format(data_type='book', resource_id='5e80fa3205a436d9f9da019e'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_resource_id_get(self):
        """Test case for api_resource_data_type_resource_id_get

        Gets a specific resource by id
        """
        response = self.client.open(
            '/api/resource/{data_type}/{resource_id}'.format(data_type='book', resource_id='5e80fa3205a436d9f9da019e'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_resource_data_type_resource_id_put(self):
        """Test case for api_resource_data_type_resource_id_put

        Update resource
        """
        body = {}
        response = self.client.open(
            '/api/resource/{data_type}/{resource_id}'.format(data_type='book', resource_id='5e80fa3205a436d9f9da019e'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
