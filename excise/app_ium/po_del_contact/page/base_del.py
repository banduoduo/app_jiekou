import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)


class DelBasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        logging.info(by)
        logging.info(value)
        element = self.driver.find_element(by, value)
        return element

    def find_del_swipe(self, text, num=5):
        self.driver.implicitly_wait(3)
        for i in range(0, num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{text}"]').click()
                return ele
            except NoSuchElementException:
                print('滑动五次未找到')

                self.driver.implicitly_wait(3)
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size['width']
                height = size['height']
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                self.driver.implicitly_wait(3)
                raise NoSuchElementException(f'找了{i}次未找到')
