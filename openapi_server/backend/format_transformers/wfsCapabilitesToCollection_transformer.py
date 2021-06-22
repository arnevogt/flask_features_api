from openapi_server.backend.format_transformers.format_transformer import FormatTransformer
from openapi_server.models.collection import Collection
from openapi_server.models.extent_spatial import ExtentSpatial
import xml.etree.ElementTree as ET

class WFSCapabilitiesToCollectionTransformer(FormatTransformer):

    def transform(self, input: str):
        """
            expects FeatureType xml node from WFS capabilites document as input
        """
        featureTypeXML = ET.fromstring(input)
        collection = self.parseFeatureType(featureTypeXML)

        output = input
        return output


    
    def parseFeatureType(self, featureTypeXML):
        id = featureTypeXML.find("Name").text
        title = featureTypeXML.find("Title").text
        description = featureTypeXML.find("Abstract").text
        extent = self.parseBBox(featureTypeXML.find("WGS84BoundingBox"))

        return Collection(id=id, title=title, description=description, extent= extent)

    def parseBBox(self, bboxXML):
        lower = bboxXML.find("LowerCorner").text
        upper = bboxXML.find("UpperCorner").text

        lowerSplit = lower.split(" ");
        upperSplit = upper.split(" ");
        extent = [lowerSplit.extend(upperSplit)]

        return ExtentSpatial(bbox= extent)
