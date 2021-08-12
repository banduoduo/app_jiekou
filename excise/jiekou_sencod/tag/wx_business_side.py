import json

import jsonpath as jsonpath
import requests

from excise.jiekou_sencod.tag.base_wx import BaseApi


class Tag(BaseApi):
    def get_token(self):
        # r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        #                  params=
        #                  {
        #                      "corpid": "ww8788130b14eaf876",
        #                      "corpsecret": "epZ2W2yWLMQjPOcVR8vTDLN4Mkv5Hsvsmz6nWQgRvVA"
        #                  }
        #
        #                  )

        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'method': 'get',
            'params': {
                "corpid": "ww8788130b14eaf876",
                "corpsecret": "epZ2W2yWLMQjPOcVR8vTDLN4Mkv5Hsvsmz6nWQgRvVA"
            }
        }
        r = self.request(data)
        self.token = r.json()['access_token']
        assert r.json()["errcode"] == 0

    def search(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?',
            'method': 'post',
            'params': {"access_token": self.token},
            'json': {}
        }
        return self.request(data)

    def add(self, group_name, tag_name):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?',
            'method': 'post',
            'params': {"access_token": self.token},
            'json': {
                "group_name": group_name,
                "tag": [
                    {
                        "name": tag_name,
                    }
                ]
            }
        }
        return self.request(data)

    def delete(self, tag_id):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?',
            'method': 'post',
            'params': {"access_token": self.token},
            'json': {"tag_id": tag_id}
        }
        return self.request(data)

    def clear(self):
        r = self.search()
        tag_id_list = [tag['id'] for group in r.json()["tag_group"] for tag in group["tag"]]
        # tag_id_list = jsonpath.jsonpath(r.json(), '$..tag[*].id')
        r = self.delete(tag_id_list)
        return r
