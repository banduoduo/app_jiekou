from excise.app_ium.po.po1.page.base_add import BaseAdd
from excise.app_ium.po.po1.page.meber_add import MeberAdd


class ContactAdd(BaseAdd):
    def contact_add(self):
        self.swipe_find_add('添加成员')
        return MeberAdd(self.driver)
