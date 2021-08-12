from time import sleep

import allure
from selenium import webdriver
from selenium.webdriver import TouchActions


@allure.title('touchaction方法')
class TestTouch:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @allure.step('1.打开百度 在输入框输入selenium测试,2.通过touch点击滑动到底部,3.点击下一页')
    def test_scrool_bottom(self):
        self.driver.get('https://www.baidu.com/')
        enter = self.driver.find_element_by_id('kw')
        search = self.driver.find_element_by_id('su')
        enter.send_keys('selenium测试')
        touch = TouchActions(self.driver)
        touch.tap(search).perform()
        touch.scroll_from_element(enter, 0, 10000).perform()
        self.driver.find_element_by_xpath("//*[@id='page']//a[last()]").click()
        sleep(4)
