from appium.webdriver.common.mobileby import MobileBy

from appium_task.page_addmeber.base_page import BasePage
from appium_task.page_addmeber.contact_page import Contact


class MainPage(BasePage):
    def goto_contact(self):
        # 点击click进入到通讯录页
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return Contact(self.driver)
