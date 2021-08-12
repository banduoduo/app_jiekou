from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.po1.page.base_add import BaseAdd
from excise.app_ium.po.po1.page.contact_add import ContactAdd


class MainAdd(BaseAdd):
    contact_find = (MobileBy.XPATH, "//*[@text='通讯录']")

    def main_add(self):
        self.find(*self.contact_find).click()
        return ContactAdd(self.driver)
