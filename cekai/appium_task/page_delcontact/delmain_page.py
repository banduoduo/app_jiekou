"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/5 5:02 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_delcontact.base_page import BasePage
from cekai.appium_task.page_delcontact.delcontact_page import DelContact


class DelMainPage(BasePage):
    def goto_delcontact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return DelContact(self.driver)