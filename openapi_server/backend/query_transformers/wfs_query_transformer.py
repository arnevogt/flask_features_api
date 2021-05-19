from openapi_server.backend.query_transformers.query_transformer import QueryTransformer

class WFSQueryTransformer(QueryTransformer):

    def transformLimit(self, limit: "int"):
        return {"count": str(limit)}

    def transformBBox(self, bbox: "list[int]"):
        return {"bbox": "{0},{1},{2},{3}".format(bbox[0], bbox[1], bbox[2], bbox[3])}

    def transformID(self, identifier: "str"):
        return {"featureID": identifier}

    def transformDateTime(self, datetime: "str"):
        pass