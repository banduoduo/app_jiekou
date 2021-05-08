"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/3 10:37 下午'
"""
from selenium import webdriver


class TestJS:
    def setup(self):
        self.drive = webdriver.Chrome()
        self.drive.implicitly_wait(5)
    def test_js_scroll(self):
        self.drive.get("http://www.baidu.com")
        self.drive.find_element_by_id("kw").send_keys("selenium测试")
        self.drive.execute_script("return document.getElementById('su')")

        self.drive.execute_script("document.documentElement.scrollTop='10000'")
        self.drive.find_element_by_xpath("//*[@id='page_addmeber']/a[10]").click()