from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excise.selenium_excise_po.po_add_department.page.base_page import BasePage
from excise.selenium_excise_po.po_add_department.page.contact_page import TestContact


class MainPage(BasePage):
    __contact_click = (By.ID, "menu_contacts")

    def goto_contact(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_contacts')))
        self.find(self.__contact_click).click()
        return TestContact(self.driver)
