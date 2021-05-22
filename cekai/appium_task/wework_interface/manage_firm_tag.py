import json

import pytest
import requests


class TestTag:
    token = None

    # 需要获取企业微信的token
    def get_token(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                          params={
                              "corpid": "ww8788130b14eaf876",
                              "corpsecret": "epZ2W2yWLMQjPOcVR8vTDLN4Mkv5Hsvsmz6nWQgRvVA"
                          })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        self.token = r.json()['access_token']

    def get_tag(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={
                              "access_token": self.token

                          })
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add_tag(self, group_name, tag_name):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.token},
                          json={
                              "group_name": group_name,
                              "tag": [{
                                  "name": tag_name
                              }]
                          }
                          )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def edit_tag(self, tag_id, tag_name):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                          params={"access_token": self.token},
                          json={
                            "id": tag_id,
                            "name": tag_name,
                        })
        print(r.json())
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def del_tag(self, group_name, tag_name):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name,
                              "tag": [{
                                  "name": tag_name
                              }
                              ]
                          }
                          )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r
