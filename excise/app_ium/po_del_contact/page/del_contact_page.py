from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po_del_contact.page.angage_contact_page import AngageContactPage
from excise.app_ium.po_del_contact.page.base_del import DelBasePage


class DelContactPage(DelBasePage):
    image = (MobileBy.XPATH, "//*[@text='多多保障']/../../../../..//android.widget.RelativeLayout[2]")

    def del_contact_page(self):
        # click 右上角图标
        self.find(*self.image).click()
        return AngageContactPage(self.driver)
