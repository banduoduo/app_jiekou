from appium.webdriver.common.mobileby import MobileBy

from appium_task.page_addmeber.base_page import BasePage


class Contact(BasePage):
    def goto_add_meber(self):
        #点击进入到添加成员页
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        from appium_task.page_addmeber.add_meber_page import AddMeber
        return AddMeber(self.driver)