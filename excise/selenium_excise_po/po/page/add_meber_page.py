from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excise.selenium_excise_po.po.page.base_page import BasePage
from excise.selenium_excise_po.po.page.contact_page import ContactPage


class AddMeber(BasePage):
    __ele_username = (By.ID, "username")
    __ele_accid = (By.ID, "memberAdd_acctid")
    __ele_phone = (By.ID, "memberAdd_phone")

    def add_meber(self, username, accid, phone):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((By.ID, "username")))
        self.find(self.__ele_username).send_keys(username)
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((By.ID, "memberAdd_acctid")))

        self.find(self.__ele_accid).send_keys(accid)
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((By.ID, "memberAdd_phone")))

        self.find(self.__ele_phone).send_keys(phone)
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".js_btn_save")))

        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_meber_fail(self, username, accid, phone):
        sleep(3)
        self.find(self.__ele_username).send_keys(username)
        sleep(3)
        self.find(self.__ele_accid).send_keys(accid)
        sleep(3)
        self.find(self.__ele_phone).send_keys(phone)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)
