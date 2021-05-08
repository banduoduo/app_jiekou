from selenium.webdriver.common.by import By

from Hogwarts_po1.po_work.base_page import BasePage
from Hogwarts_po1.po_work.department import Department


class Contact(BasePage):

    def add_department(self):
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_dropdown').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()
        return Department(self.driver)

"""
    def get_list(self):
        ele_list = self.driver.find_element_by_css_selector('.member_colLeft')
        print(ele_list)
        name_list = []
        for ele in ele_list:
            name_list.append(ele.txt)
        print(name_list)
        return name_list
"""