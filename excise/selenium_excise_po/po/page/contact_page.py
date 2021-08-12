from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excise.selenium_excise_po.po.page.base_page import BasePage


class ContactPage(BasePage):

    def add_name_List(self):
        # expected_conditions.element_to_be_clickable()
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_title th:nth-child(1)')))
        ele_list = self.driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')
        print(ele_list)
        name_list = []
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list

    def daa_name_list_fail(self):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((By.ID, "username")))
        element = self.driver.find_elements_by_css_selector('.ww_inputWithTips_tips')
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        print(error_list)
        return error_list


