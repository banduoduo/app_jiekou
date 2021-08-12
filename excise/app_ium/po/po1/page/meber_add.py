from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po.po1.page.base_add import BaseAdd
from excise.app_ium.po.po1.page.edit_add import EditAdd


class MeberAdd(BaseAdd):
    manmul_find = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    add_find = (MobileBy.XPATH, "//*[@text='添加成功']")

    def meber_add(self):
        self.find(*self.manmul_find).click()
        return EditAdd(self.driver)

    def find_toast(self):
        self.find(*self.add_find)
