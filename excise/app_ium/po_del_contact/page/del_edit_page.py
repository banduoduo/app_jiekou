from excise.app_ium.po_del_contact.page.base_del import DelBasePage
from excise.app_ium.po_del_contact.page.del_meber_page import DelMeberPage


class DelEditPage(DelBasePage):
    def del_edit_page(self):
        # 向下滑动找到删除成员,自己封装一个删除成员
        self.find_del_swipe('删除成员')
        return DelMeberPage(self.driver)
