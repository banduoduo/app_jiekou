from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


# todo:如果报错为不是w3c的，就加入option参数
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # todo:1.打开百度 在输入框输入selenium测试 2.通过touch点击滑动到底部 3.点击下一页
    def test_scroll(self):
        self.driver.get("https://www.baidu.com/")
        ele_scroll = self.driver.find_element_by_id('kw')
        ele_scroll.send_keys('selenium测试')
        ele_search = self.driver.find_element_by_id('su')
        sleep(3)
        touch = TouchActions(self.driver)
        touch.tap(ele_search)
        touch.perform()
        touch.scroll_from_element(ele_scroll, 0, 10000).perform()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']//a[last()]").click()
        sleep(3)

    # todo:表单
    def test_from(self):
        self.driver.get('http://testerhome.com/account/sign_in')
        self.driver.find_element_by_id('user_login').send_keys('123')
        self.driver.find_element_by_id('user_password').send_keys('username')
        self.driver.find_element_by_css_selector('.custom-control-label').click()
        self.driver.find_element_by_css_selector('.btn-primary').click()
