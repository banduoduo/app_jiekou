from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.page.base_page import BasePage


class AddMeber(BasePage):
    manual_add = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    add_sucess = (MobileBy.XPATH, "//*[@text='添加成功']")

    def add_meber(self):
        self.find(*self.manual_add).click()

        from excise.app_ium.po.page.eidt_page import EditPage
        return EditPage(self.driver)

    def find_toast(self):
        self.find(*self.add_sucess)
