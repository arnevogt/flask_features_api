import connexion
import six

from openapi_server.models.collection import Collection  # noqa: E501
from openapi_server.models.collections import Collections  # noqa: E501
from openapi_server.models.conf_classes import ConfClasses  # noqa: E501
from openapi_server.models.exception import Exception  # noqa: E501
from openapi_server.models.landing_page import LandingPage  # noqa: E501
from openapi_server.models.link import Link  # noqa: E501
from openapi_server.models.extent import Extent
from openapi_server.models.extent_spatial import ExtentSpatial
from openapi_server.models.extent_temporal import ExtentTemporal
from openapi_server import util
from flask import request


def describe_collection(collection_id):  # noqa: E501
    """describe the feature collection with id &#x60;collectionId&#x60;

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str

    :rtype: Collection
    """
    c = getVegetationCollection(request.url, request.url + "/items")

    return c


def get_collections():  # noqa: E501
    """the feature collections in the dataset

     # noqa: E501


    :rtype: Collections
    """
    selfLink = Link(href=request.url, rel="self",
                    title="describition of all collections in json", type="application/json")
    colls = Collections(links=[selfLink], collections=[getVegetationCollection(
        request.url + "/vegetation", request.url + "/vegetation/items")])
    return colls


def get_conformance_declaration():  # noqa: E501
    """information about specifications that this API conforms to

    A list of all conformance classes specified in a standard that the server conforms to. # noqa: E501


    :rtype: ConfClasses
    """
    return 'do some magic!'


def get_landing_page():  # noqa: E501
    """landing page

    The landing page provides links to the API definition, the conformance statements and to the feature collections in this dataset. # noqa: E501


    :rtype: LandingPage
    """
    collectionsLink = Link(request.url + "collections", rel="data",
                           title="information about the feature collections")
    selfLink = Link(href=request.url, rel="self",
                    type="application/json", title="landing page as json")
    lp = LandingPage("TB-17 Experiments API Python Server",
                     "this is a dummy server", [selfLink, collectionsLink])

    return lp


def getVegetationCollection(selfUrl, itemsUrl):
    selfLink = Link(href=selfUrl, rel="self",
                    title="collection describtion as json", type="application/json")
    itemsLink = Link(href=itemsUrl, rel="items",
                     title="vegetation", type="application/geo+json")
    extentSp = ExtentSpatial(bbox=[[7.01, 50.63, 7.22, 50.78]])
    extentTemp = ExtentTemporal(interval=[["2010-02-15T12:34:56Z", None]])
    extent = Extent(spatial=extentSp, temporal=extentTemp)
    c = Collection(id="vegetation", description="this collection contains vegetation data", links=[
                   selfLink, itemsLink], extent=extent, title="vegetation")

    return c
