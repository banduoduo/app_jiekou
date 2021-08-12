from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excise.selenium_excise_po.po_add_department.page.base_page import BasePage


class TestContact(BasePage):
    __click_add = (By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap')
    __click_into = (By.CSS_SELECTOR, '.js_create_party')

    def add_department(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.member_colLeft_top_addBtnWrap')))

        self.find(self.__click_add).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_create_party')))

        self.find(self.__click_into).click()
        from excise.selenium_excise_po.po_add_department.page.department_edit_page import TestEdit
        return TestEdit(self.driver)


