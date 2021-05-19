import urllib3
from urllib.parse import urlparse, parse_qs

class HTTPAccessLayer:

    def get(self, baseURL: "str", urlParams: "dict[str, str]"):
        http = urllib3.PoolManager()

        #handle if baseURL already contains request params
        parsedURL = urlparse(baseURL)
        print(parsedURL)
        url = parsedURL.scheme + "://" + parsedURL.netloc + parsedURL.path
        if parsedURL.query:
            existingQueryParams = parse_qs(parsedURL.query) #dict[str, list[str]]
            seperator = ","
            for key in existingQueryParams:
                existingQueryParams[key] = seperator.join(existingQueryParams[key]) #join list
            urlParams.update(dict(existingQueryParams)) #merge dicts

        r = http.request('GET', url, fields=urlParams)
        print(r)
        print(r.status)

        return r.data.decode("utf8")
