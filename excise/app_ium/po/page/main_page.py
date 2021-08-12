
from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.page.base_page import BasePage
from excise.app_ium.po.page.contact import Contact


class MainPage(BasePage):
    click_contact = (MobileBy.XPATH, "//*[@text='通讯录']")

    def main_page(self):
        self.find(*self.click_contact).click()
        return Contact(self.driver)
