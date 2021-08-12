from time import sleep

import yaml
from selenium import webdriver


class TestContact():

    def setup(self):
        opt = self.driver = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_get_cookies(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_id('menu_contacts').click()
        cookie = self.driver.get_cookies()
        print(cookie)
        with open('login.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookie, f)

    def test_wework_contact(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('login.yaml') as f:
            login_cookie = yaml.safe_load(f)
            for cookie in login_cookie:
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        sleep(3)
        self.driver.find_element_by_link_text('添加成员').click()
        self.driver.find_element_by_id('username').send_keys('哈哈哈哈哈')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('bbb122_')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('18114756672')
        self.driver.find_element_by_link_text('保存').click()
        sleep(3)

