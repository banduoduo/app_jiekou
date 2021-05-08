from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # self.driver.find_element(By.XPATH, '//*[@title="最近几天里创建的主题"]/a').click()
        # self.driver.find_element(By.XPATH, '//*[@title="测试答疑"]').click()
        # sleep(3)
        # print("hello")
        self.driver.find_element(By.LINK_TEXT, "热门").click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "精华帖").click()
        sleep(3)
