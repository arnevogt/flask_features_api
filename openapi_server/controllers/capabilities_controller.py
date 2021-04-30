import connexion
import six

from openapi_server.models.collection import Collection  # noqa: E501
from openapi_server.models.collections import Collections  # noqa: E501
from openapi_server.models.conf_classes import ConfClasses  # noqa: E501
from openapi_server.models.exception import Exception  # noqa: E501
from openapi_server.models.landing_page import LandingPage  # noqa: E501
from openapi_server.models.link import Link  # noqa: E501
from openapi_server import util
from flask import request


def describe_collection(collection_id):  # noqa: E501
    """describe the feature collection with id &#x60;collectionId&#x60;

     # noqa: E501

    :param collection_id: local identifier of a collection
    :type collection_id: str

    :rtype: Collection
    """
    selfLink = Link(href=request.url, rel="self")
    itemsLink = Link(href=request.url + "/items", rel="items")
    c = Collection(id=collection_id, description="welcome to " +
                   collection_id + " collection", links=[selfLink, itemsLink])

    return c


def get_collections():  # noqa: E501
    """the feature collections in the dataset

     # noqa: E501


    :rtype: Collections
    """
    collectionLink1 = Link(href=request.url + "/helloworld", rel="collection")
    selfLink = Link(href=request.url, rel="self")
    colls = Collections(links=[selfLink, collectionLink1])

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
    collectionsLink = Link(request.url + "/collections", rel="collections")
    selfLink = Link(href=request.url, rel="self")
    lp = LandingPage("TB-17 Experiments API Python Server",
                     "this is a dummy server", [selfLink, collectionsLink])

    return lp
