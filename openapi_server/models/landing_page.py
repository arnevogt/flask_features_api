# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.link import Link
from openapi_server import util

from openapi_server.models.link import Link  # noqa: E501

class LandingPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title=None, description=None, links=None):  # noqa: E501
        """LandingPage - a model defined in OpenAPI

        :param title: The title of this LandingPage.  # noqa: E501
        :type title: str
        :param description: The description of this LandingPage.  # noqa: E501
        :type description: str
        :param links: The links of this LandingPage.  # noqa: E501
        :type links: List[Link]
        """
        self.openapi_types = {
            'title': str,
            'description': str,
            'links': List[Link]
        }

        self.attribute_map = {
            'title': 'title',
            'description': 'description',
            'links': 'links'
        }

        self._title = title
        self._description = description
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'LandingPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The landingPage of this LandingPage.  # noqa: E501
        :rtype: LandingPage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self):
        """Gets the title of this LandingPage.


        :return: The title of this LandingPage.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LandingPage.


        :param title: The title of this LandingPage.
        :type title: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this LandingPage.


        :return: The description of this LandingPage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LandingPage.


        :param description: The description of this LandingPage.
        :type description: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this LandingPage.


        :return: The links of this LandingPage.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LandingPage.


        :param links: The links of this LandingPage.
        :type links: List[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links
