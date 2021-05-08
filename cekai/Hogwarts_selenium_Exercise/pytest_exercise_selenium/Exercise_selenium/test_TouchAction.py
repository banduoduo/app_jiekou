from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAc():
    def setup(self):
        op = webdriver.ChromeOptions()
        op.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=op)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

        action_search = TouchActions(self.driver)
        action_search.tap(self.driver.find_element_by_id("su")).perform()
        el = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)

        action.scroll_from_element(el, 10, 10000).perform()
        self.driver.find_element_by_css_selector('#page_addmeber > div > a.n').click()
        sleep(3)



