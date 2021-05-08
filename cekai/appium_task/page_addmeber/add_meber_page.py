from appium.webdriver.common.mobileby import MobileBy

from cekai.appium_task.page_addmeber.base_page import BasePage
from cekai.appium_task.page_addmeber.manage_page import EditMeber


class AddMeber(BasePage):
    # 手动输入添加到编辑页面
    def manual_input(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        return EditMeber(self.driver)

    def find_toast(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')
        # return True
