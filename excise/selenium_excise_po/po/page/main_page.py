from excise.selenium_excise_po.po.page.add_meber_page import AddMeber
from excise.selenium_excise_po.po.page.base_page import BasePage


class MainPage(BasePage):
    def goto_add_meber(self):
        self.driver.find_element_by_css_selector('.ww_indexImg_AddMember').click()
        return AddMeber(self.driver)

    def goto_contact(self):
        pass


