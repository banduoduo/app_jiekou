import json

import requests


class BaseApi:
    def request(self, request: dict):
        if 'url' in request:
            return self.http_request(request)
        if 'rpc' == request.get("protocol"):
            return self.http_request(request)

    def http_request(self, request):
        # request = {
        #     "url": '',
        #     "method": 'get',
        #     "json": {},
        #     "params": {}
        #
        # }
        r = requests.request(**request)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r
