import os

from selenium import webdriver


class TestBrowwer():
    def setup(self):
        browser = os.getenv("broswer")
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS
        else:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

