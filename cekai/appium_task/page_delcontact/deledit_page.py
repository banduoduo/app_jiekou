"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/5 5:04 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_delcontact.base_page import BasePage


class ManagePage(BasePage):
    def editpage(self):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@class='android.widget.ListView']//android.widget.RelativeLayout[3]").click()

        from cekai.appium_task.page_delcontact.edit_del import DelEdit
        return DelEdit(self.driver)
