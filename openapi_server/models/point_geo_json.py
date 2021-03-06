# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PointGeoJSON(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, coordinates=None):  # noqa: E501
        """PointGeoJSON - a model defined in OpenAPI

        :param type: The type of this PointGeoJSON.  # noqa: E501
        :type type: str
        :param coordinates: The coordinates of this PointGeoJSON.  # noqa: E501
        :type coordinates: List[float]
        """
        self.openapi_types = {
            'type': str,
            'coordinates': List[float]
        }

        self.attribute_map = {
            'type': 'type',
            'coordinates': 'coordinates'
        }

        self._type = type
        self._coordinates = coordinates

    @classmethod
    def from_dict(cls, dikt) -> 'PointGeoJSON':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The pointGeoJSON of this PointGeoJSON.  # noqa: E501
        :rtype: PointGeoJSON
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this PointGeoJSON.


        :return: The type of this PointGeoJSON.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PointGeoJSON.


        :param type: The type of this PointGeoJSON.
        :type type: str
        """
        allowed_values = ["Point"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def coordinates(self):
        """Gets the coordinates of this PointGeoJSON.


        :return: The coordinates of this PointGeoJSON.
        :rtype: List[float]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this PointGeoJSON.


        :param coordinates: The coordinates of this PointGeoJSON.
        :type coordinates: List[float]
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501
        if coordinates is not None and len(coordinates) < 2:
            raise ValueError("Invalid value for `coordinates`, number of items must be greater than or equal to `2`")  # noqa: E501

        self._coordinates = coordinates
