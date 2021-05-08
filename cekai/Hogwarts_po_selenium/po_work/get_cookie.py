import os
import shelve
import time
from lib2to3.pgen2 import driver
from time import sleep

import yaml
from selenium import webdriver


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