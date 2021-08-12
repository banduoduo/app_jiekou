from appium.webdriver.common.mobileby import MobileBy

from excise.app_ium.po_del_contact.page.base_del import DelBasePage


class AngageContactPage(DelBasePage):
    click_meber = (MobileBy.XPATH, "//*[@text='成d']/../../../..//android.widget.RelativeLayout")

    def angage_contact_page(self):
        # 点击成员
        self.find(*self.click_meber).click()

        from excise.app_ium.po_del_contact.page.del_edit_page import DelEditPage
        return DelEditPage(self.driver)

    def get_name_list(self):
        pass
