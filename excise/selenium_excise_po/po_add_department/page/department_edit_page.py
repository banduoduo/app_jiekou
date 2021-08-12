from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excise.selenium_excise_po.po_add_department.page.base_page import BasePage
from excise.selenium_excise_po.po_add_department.page.contact_page import TestContact


class TestEdit(BasePage):
    __add_edit = (By.CSS_SELECTOR, '.ww_inputText:nth-child(2)')
    __add_depart = (By.CSS_SELECTOR, '.js_parent_party_name')
    __click_make = (By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688850133091538_anchor"]')
    __make_sure = (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot a:nth-child(1)')

    def edit_department(self, department):
        sleep(3)
        self.find(self.__add_edit).send_keys(department)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, '.js_parent_party_name')))
        self.find(self.__add_depart).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688850133091538_anchor"]')))
        self.find(self.__click_make).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, '.qui_dialog_foot.ww_dialog_foot a:nth-child(1)')))
        self.find(self.__make_sure).click()
        return TestContact(self.driver)
