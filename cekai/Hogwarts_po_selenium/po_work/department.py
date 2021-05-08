from selenium.webdriver.common.by import By

from Hogwarts_po1.po_work.base_page import BasePage
from Hogwarts_po1.po_work.getlist import ContactPage


class Department(BasePage):
    __ele_name = (By.CSS_SELECTOR, '.ww_inputText:nth-child(2)')
    __choose_department = (By.CSS_SELECTOR, '.js_parent_party_name')
    __add_makesure = (By.CSS_SELECTOR, '.js_party_list_container')

    def add_department_name(self, name):
        self.find(self.__ele_name).send_keys('快乐星球')
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_party_list_container').click()
        self.driver.find_element(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        return ContactPage(self.driver)

    def add_department_name_fail(self, name):
        self.driver.find_element(*self.__ele_name).send_keys('快乐星球')
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_party_list_container').click()
        self.driver.find_element(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        error = self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft')
        error_list = []
        for ele in error:
            error_list.append(ele.txt)
            return error_list
