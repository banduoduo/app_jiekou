from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.page.add_meber import AddMeber
from excise.app_ium.po.page.base_page import BasePage


class Contact(BasePage):
    def get_namelist(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector().text("添加成员").instance(0));')
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find('添加成员')
        return AddMeber(self.driver)
