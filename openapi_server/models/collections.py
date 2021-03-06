# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.collection import Collection
from openapi_server.models.link import Link
from openapi_server import util

from openapi_server.models.collection import Collection  # noqa: E501
from openapi_server.models.link import Link  # noqa: E501

class Collections(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, links=None, collections=None):  # noqa: E501
        """Collections - a model defined in OpenAPI

        :param links: The links of this Collections.  # noqa: E501
        :type links: List[Link]
        :param collections: The collections of this Collections.  # noqa: E501
        :type collections: List[Collection]
        """
        self.openapi_types = {
            'links': List[Link],
            'collections': List[Collection]
        }

        self.attribute_map = {
            'links': 'links',
            'collections': 'collections'
        }

        self._links = links
        self._collections = collections

    @classmethod
    def from_dict(cls, dikt) -> 'Collections':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The collections of this Collections.  # noqa: E501
        :rtype: Collections
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self):
        """Gets the links of this Collections.


        :return: The links of this Collections.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Collections.


        :param links: The links of this Collections.
        :type links: List[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def collections(self):
        """Gets the collections of this Collections.


        :return: The collections of this Collections.
        :rtype: List[Collection]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this Collections.


        :param collections: The collections of this Collections.
        :type collections: List[Collection]
        """
        if collections is None:
            raise ValueError("Invalid value for `collections`, must not be `None`")  # noqa: E501

        self._collections = collections
