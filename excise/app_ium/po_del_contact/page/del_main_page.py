from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po_del_contact.page.base_del import DelBasePage
from excise.app_ium.po_del_contact.page.del_contact_page import DelContactPage


class DelMainPage(DelBasePage):
    click_contact = (MobileBy.XPATH, "//*[@text='通讯录']")

    def del_main_page(self):
        # click通讯录
        self.find(*self.click_contact).click()
        return DelContactPage(self.driver)
