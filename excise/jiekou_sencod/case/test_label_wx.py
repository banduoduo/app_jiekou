import json

from excise.jiekou_sencod.tag.wx_business_side import Tag


class TestWeWork:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        self.tag.clear()

    def test_search_api(self):
        r = self.tag.search()
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errmsg"] == "ok"
        assert len(r.json()["tag_group"]) == 0

    def test_add_api(self):
        r = self.tag.add(group_name='duoduo', tag_name='0233')
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200

    def test_delet_api(self):
        r = self.tag.delete(tag_id="etdtdiCQAAj7KwL_eEcOy6vqkMnP14RQ")
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()["errcode"] == 0
