from openapi_server.backend.format_transformers.null_transformer import NullTransformer
from openapi_server.backend.request_transformer import RequestTransformer
from openapi_server.backend.dataaccess.http_access_layer import HTTPAccessLayer
from openapi_server.backend.query_transformers.wfs_query_transformer import WFSQueryTransformer

class WFSRequestTransformer(RequestTransformer):

    def __init__(self, wfsBaseURL: str):
        self.wfsBaseURL = wfsBaseURL
        self.http = HTTPAccessLayer()
        self.queryTransformer = WFSQueryTransformer()
        self.formatTransformer = NullTransformer() #ToDo should be converted from GML3

    
    def getFeatures(self, collectionID: str, limit=None, bbox=None, datetime=None):
        requestParams = {"request": "getFeature", "service" : "WFS", "version": "2.0.0", "outputFormat": "application/json", "typeNames": collectionID}
        
        if limit is not None:
            requestParams.update(self.queryTransformer.transformLimit(limit)) #merge dicts
        
        if bbox is not None:
            requestParams.update(self.queryTransformer.transformBBox(bbox)) #merge dicts

        if datetime is not None:
            requestParams.update(self.queryTransformer.transformDateTime(datetime)) #merge dicts

        backendResp = self.http.get(self.wfsBaseURL, requestParams)
        resp = self.formatTransformer.transform(backendResp)

        return resp

    def getFeature(self, collectionID: str, featureID: str):
        requestParams = {"request": "getFeature", "service" : "WFS", "version": "2.0.0", "outputFormat": "application/json", "typeName": collectionID}
        featureIdParams = self.queryTransformer.transformID(featureID)
        requestParams.update(featureIdParams) #merge dicts 

        backendResp = self.http.get(self.wfsBaseURL, requestParams)
        resp = self.formatTransformer.transform(backendResp)

        return resp