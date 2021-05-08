from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
"""

class TestLogin:
    def test_Getweb(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(6)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        self.driver.find_element_by_id("menu_contacts").click()
        # print(self.driver.get_cookies())
        cookie = self.driver.get_cookies()
        with open("login.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)
"""

class BasePage:
    def __init__(self, driver: WebElement = None):
        if driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            with open("login.yaml", encoding="UTF-8") as f:
                yaml_login = yaml.safe_load(f)
                #print(yaml_login)
                for cookie in yaml_login:
                    self.driver.add_cookie(cookie)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def find(self, by, ele=None):
        if ele is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def finds(self, by, eles=None):
        if eles is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, eles)
