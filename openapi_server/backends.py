from openapi_server.backend.data_backend import BackendType, DataBackend


cubewerxWFSConfig = {"baseURL": "https://test.cubewerx.com/cubewerx/cubeserv/demo?datastore=Daraa"}
cubewerxWFSCollections = {"Agriculture": "AgricultureSrf", "Vegetation": "VegetationSrf"}
cubewerxWFS = DataBackend(BackendType.WFS, cubewerxWFSCollections, cubewerxWFSConfig)


availableBackends = [cubewerxWFS]




def getDataBackendForCollection(collectionID: str):
    for backend in availableBackends:
        if collectionID in backend.availableCollections:
            return backend

    return None