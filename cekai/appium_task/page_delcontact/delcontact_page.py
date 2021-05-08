"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/5 5:03 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_delcontact.base_page import BasePage


class DelContact(BasePage):
    def manage_contacts(self):
        ele = self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/cmg"]//android.widget.LinearLayout[2]//android.widget.RelativeLayout[2]')
        ele.click()

        from cekai.appium_task.page_delcontact.deledit_page import ManagePage
        return ManagePage(self.driver)
