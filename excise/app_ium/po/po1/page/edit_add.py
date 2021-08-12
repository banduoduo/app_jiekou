from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.po1.page.base_add import BaseAdd


class EditAdd(BaseAdd):
    name_find = (MobileBy.XPATH, "//*[@text='必填']")
    phone_find = (MobileBy.XPATH, '//*[contains(@text,"手机")]/..//android.widget.EditText')
    save_find = (MobileBy.XPATH, "//*[@text='保存']")

    def edit_add(self, name, phone_num):
        self.find(*self.name_find).send_keys(name)
        self.find(*self.phone_find).send_keys(phone_num)
        self.find(*self.save_find).click()

        from excise.app_ium.po.po1.page.meber_add import MeberAdd
        return MeberAdd(self.driver)
