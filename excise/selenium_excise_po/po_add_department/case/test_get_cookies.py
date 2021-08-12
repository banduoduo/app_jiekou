from time import sleep

import yaml
from selenium import webdriver


class TestGetCookie:
    def setup_class(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_save_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        cookies = self.driver.get_cookies()
        print(cookies)
        with open('../case/cookies.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookies, f)

    def test_get_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
        with open('../case/cookies.yaml', encoding='utf-8') as f:
            get_cookie = yaml.safe_load(f)
            for cookie in get_cookie:
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)