import pytest

from cekai.appium_task.wework_interface.manage_firm_tag import TestTag


class TestManage:
    def setup_class(self):
        self.manage = TestTag()
        self.manage.get_token()

    def test_get_tag(self):
        r = self.manage.get_tag()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize('group_name, tag_name', [['work_app0522', '0525']], ids=
    ['添加企业客户标签'])
    def test_add_tag(self, group_name, tag_name):
        r = self.manage.add_tag('group_name', 'tag_name')
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize('tag_id, tag_name', [['etdtdiCQAAi-D1yp4vkW5DL9tVJwuxkw', '标签组333']], ids=['编辑企业客户标签'])
    def test_edit_tag(self, tag_id, tag_name):
        r = self.manage.edit_tag('tag_id', 'tag_name')
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_del_tag(self):
        r = self.manage.del_tag(group_name='xxxx', tag_name='xxxx')
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
