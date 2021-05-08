"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/5 11:36 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_delcontact.base_page import BasePage
from cekai.appium_task.page_delcontact.deledit_page import ManagePage


class DelPerson(BasePage):
    def del_person(self):
        del_Button = self.driver.find_element(MobileBy.XPATH,
                                              '//*[@resource-id="android:id/content"]//android.widget.RelativeLayout[3]//android.widget.TextView[2]')
        del_Button.click()
        return ManagePage(self.driver)
