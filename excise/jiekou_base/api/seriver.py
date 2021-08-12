import json

import requests


class TestWX:
    def get_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params=
                         {
                             "corpid": "ww8788130b14eaf876",
                             "corpsecret": "epZ2W2yWLMQjPOcVR8vTDLN4Mkv5Hsvsmz6nWQgRvVA"
                         }

                         )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        print(r.json())
        self.token = r.json()['access_token']
        assert r.json()["errcode"] == 0

    def test_search(self):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?',
                          params={"access_token": self.token},
                          json={}
                          )
        return r

    def test_add(self, group_name, tag_name):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?',
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name,
                              "tag": [
                                  {
                                      "name": tag_name,
                                  }
                              ]
                          }
                          )
        return r

    def test_delet(self, tag_id):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag?",
                          params={"access_token": self.token},
                          json={
                              "tag_id": tag_id
                          }
                          )
        return r
