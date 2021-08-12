from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po_del_contact.page.angage_contact_page import AngageContactPage
from excise.app_ium.po_del_contact.page.base_del import DelBasePage


class DelMeberPage(DelBasePage):
    del_sucess = (MobileBy.XPATH,
                  '//*[@resource-id="android:id/content"]//android.widget.RelativeLayout[3]//android.widget.TextView[2]')

    def del_meber_page(self):
        # 删除成功回到管理成员页
        self.find(*self.del_sucess).click()
        return AngageContactPage(self.driver)
