from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestQw:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


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

    def test_Qw(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("login.yaml", encoding="UTF-8") as f:
            yaml_login = yaml.safe_load(f)
            for cookie in yaml_login:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(2)
        self.driver.find_element_by_link_text('添加成员').click()
        sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("陈晨")
        self.driver.find_element_by_id("username").send_keys("陈晨")
        sleep(2)
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("晨晨")
        sleep(2)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("banduo123__")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@name="gender" and @value="2"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@name="mobile"]').send_keys("17717063599")
        sleep(2)
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("00-22223")
        sleep(2)
        self.driver.find_element_by_id("memberAdd_mail").send_keys("2501071923@qq.com")
        sleep(2)
        self.driver.find_element_by_id("memberEdit_address").send_keys("上海市杨浦区")
        sleep(2)
        self.driver.find_element_by_id("memberAdd_title").send_keys("普通员工")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@name="identity_stat" and @value="1"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@name="extern_position_set" and @value="custom"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@name="extern_position"]').send_keys("快乐担当")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@name="sendInvite"]').click()
        sleep(2)
        self.driver.find_element_by_link_text("保存").click()
