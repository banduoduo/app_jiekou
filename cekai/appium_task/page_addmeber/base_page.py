import logging

from appium.webdriver.webdriver import WebDriver

logging.basicConfig(level=logging.INFO)


class BasePage:
    def __init__(self, driver: WebDriver = None):
        # 初始化driver
        self.driver = driver

    def find_log(self, by, value):
        logging.info(by)
        logging.info(value)

        return self.driver.find_element(by, value)
