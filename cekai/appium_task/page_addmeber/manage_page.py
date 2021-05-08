from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_addmeber.base_page import BasePage


class EditMeber(BasePage):
    def edit_meber(self, name, phonenum):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//android.widget.EditText').send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

        from cekai.appium_task.page_addmeber.add_meber_page import AddMeber
        return AddMeber(self.driver)
