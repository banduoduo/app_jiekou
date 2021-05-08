from Hogwarts_po1.po_work.base_page import BasePage
from Hogwarts_po1.po_work.contact import Contact
from selenium import webdriver


class MainPage(BasePage):
    def goto_contact(self):
        pass
        return Contact(self.driver)
