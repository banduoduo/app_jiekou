from time import sleep

import yaml
from selenium import webdriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            with open('data.yaml', encoding='utf-8') as f:
                yaml_login = yaml.safe_load(f)
                for cookie in yaml_login:
                    self.driver.add_cookie(cookie)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        else:
            self.driver = base_driver

    def find(self, by, ele=None):
        if ele is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)
