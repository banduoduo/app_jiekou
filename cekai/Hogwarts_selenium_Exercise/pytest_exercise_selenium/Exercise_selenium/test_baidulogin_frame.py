import os
from time import sleep

import pytest
from selenium import webdriver


class TestFrame():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_baidulogin(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id("s-top-loginbtn").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('18217676671')
        sleep(3)
        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('18217676671')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('12345')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)
