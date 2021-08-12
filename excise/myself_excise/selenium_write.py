from selenium.webdriver.common.by import By

from excise.myself_excise.base import Base


class TestWrite(Base):

    def click_summary(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        click_me = self.driver.find_element(By.XPATH, "//*[@value='click me']")

