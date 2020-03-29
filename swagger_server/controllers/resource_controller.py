import connexion
import six
from bson import ObjectId
from pymongo import ReturnDocument
from werkzeug.exceptions import UnprocessableEntity, BadRequest

from swagger_server import util
from swagger_server.config import MONGO_DB


def api_resource_data_type_get(data_type, page=None, per_page=None, last_id=None):  # noqa: E501
    """Gets list of resources

    Returns list of resources of DataType # noqa: E501

    :param data_type: The data type ex book.
    :type data_type: str
    :param page: Page value for pagination
    :type page: int
    :param per_page: Number of resources to return per page for pagination
    :type per_page: int
    :param last_id: The last objectId in previous page. Used as pagination state. If used will ignore page parameter.
    :type last_id: str

    :rtype: List[object]
    """
    if data_type not in MONGO_DB.db.list_collection_names():
        raise UnprocessableEntity(f'{data_type} does not exist.')
    if last_id is None:
        # Calculate number of documents to skip
        skips = per_page * (page - 1)
        return list(MONGO_DB.db[data_type].find().skip(skips).limit(per_page))
    else:
        return list(MONGO_DB.db[data_type].find({'_id': {'$gt': last_id}}).limit(per_page))


def api_resource_data_type_post(body, data_type):  # noqa: E501
    """Create resource

    Creates a resource to be stored # noqa: E501

    :param body: The resource to create.
    :type body: dict | bytes
    :param data_type: The data type ex book.
    :type data_type: str

    :rtype: None
    """
    if data_type not in MONGO_DB.db.list_collection_names():
        raise UnprocessableEntity(f'{data_type} does not exist.')
    if not connexion.request.is_json:
        raise BadRequest('Only application/json supported.')
    body = connexion.request.get_json()
    inserted_id = MONGO_DB.db[data_type].insert_one(body).inserted_id
    return api_resource_data_type_resource_id_get(data_type, inserted_id)


def api_resource_data_type_resource_id_delete(data_type, resource_id):  # noqa: E501
    """Deletes a specific resource by id

    Delete a resource of DataType by its id # noqa: E501

    :param data_type: The data type ex book.
    :type data_type: str
    :param resource_id: The resource_id.
    :type resource_id: str

    :rtype: object
    """
    if data_type not in MONGO_DB.db.list_collection_names():
        raise UnprocessableEntity(f'{data_type} does not exist.')
    return MONGO_DB.db[data_type].find_one_and_delete({'_id': ObjectId(resource_id)})


def api_resource_data_type_resource_id_get(data_type, resource_id):  # noqa: E501
    """Gets a specific resource by id

    Retrieves a resource of DataType by its id # noqa: E501

    :param data_type: The data type ex book.
    :type data_type: str
    :param resource_id: The resource_id.
    :type resource_id: str

    :rtype: object
    """
    if data_type not in MONGO_DB.db.list_collection_names():
        raise UnprocessableEntity(f'{data_type} does not exist.')
    return MONGO_DB.db[data_type].find_one_or_404({'_id': ObjectId(resource_id)})


def api_resource_data_type_resource_id_put(body, data_type, resource_id):  # noqa: E501
    """Update resource

    Updates an existing resource # noqa: E501

    :param body: The resource to update.
    :type body: dict | bytes
    :param data_type: The data type ex book.
    :type data_type: str
    :param resource_id: The resource_id.
    :type resource_id: str

    :rtype: None
    """
    if data_type not in MONGO_DB.db.list_collection_names():
        raise connexion.exceptions.UnprocessableEntity(f'{data_type} does not exist.')
    if not connexion.request.is_json:
        raise BadRequest('Only application/json supported.')
    body = connexion.request.get_json()
    return MONGO_DB.db[data_type].find_one_and_replace({'_id': ObjectId(resource_id)}, body,
                                                       return_document=ReturnDocument.AFTER)
