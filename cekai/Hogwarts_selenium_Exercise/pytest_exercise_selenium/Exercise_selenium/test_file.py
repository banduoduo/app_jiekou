"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/3 10:53 下午'
"""
from selenium import webdriver


class TestFile:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_file_upload(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='form']/span[1]/span[2]").click()
        self.driver.find_element_by_xpath("//*[@id='form']/div/div[2]/div[2]/input").send_keys("/Users/admin/Desktop/WX20210503-230107@2x.png")


