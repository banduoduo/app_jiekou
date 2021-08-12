from time import sleep

import yaml
from selenium import webdriver


class TestCookie:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        cookies = self.driver.get_cookies()
        # print(cookies)
        with open('data.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookies, f)

    def test_cookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
        with open('data.yaml', encoding='utf-8') as f:
            yaml_login = yaml.safe_load(f)
            for cookie in yaml_login:
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        sleep(3)



