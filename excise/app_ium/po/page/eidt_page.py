from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.page.add_meber import AddMeber
from excise.app_ium.po.page.base_page import BasePage


class EditPage(BasePage):
    must_write = (MobileBy.XPATH, "//*[@text='必填']")
    phone_number = (MobileBy.XPATH, '//*[contains(@text,"手机")]/..//android.widget.EditText')
    save = (MobileBy.XPATH, "//*[@text='保存']")

    def edit_add_meber(self, name, phonenum):
        self.find(*self.must_write).send_keys(name)
        self.find(*self.phone_number).send_keys(phonenum)
        self.find(*self.save).click()

        return AddMeber(self.driver)
