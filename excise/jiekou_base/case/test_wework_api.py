import json

from excise.jiekou_base.api.seriver import TestWX


class TestWeWork:
    def setup_class(self):
        self.wework = TestWX()
        self.wework.get_token()

    def test_search_api(self):
        r = self.wework.test_search()
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errmsg"] == "ok"

    def test_add_api(self):
        r = self.wework.test_add(group_name='duoduo', tag_name='0233')
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200

    def test_delet_api(self):
        r = self.wework.test_delet(tag_id="etdtdiCQAA0ZjzL-9VwbdeJpC9LEatBg")
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errcode"] == 0
