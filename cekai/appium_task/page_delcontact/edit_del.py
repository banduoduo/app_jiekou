"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/5 11:29 下午'
"""
from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_delcontact.base_page import BasePage


class DelEdit(BasePage):
    def edit_del(self):

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()

        from cekai.appium_task.page_delcontact.del_person import DelPerson
        return DelPerson(self.driver)

