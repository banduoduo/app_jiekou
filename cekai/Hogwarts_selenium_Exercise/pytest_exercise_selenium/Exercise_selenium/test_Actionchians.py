from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.keys import Keys


class TestAch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        ele_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        ele_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        ele_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_rightclick)
        action.double_click(ele_doubleclick)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoe(self):
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        eles = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(eles)
        action.perform()
        sleep(3)

    def test_dargdrop(self):
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_ele = self.driver.find_element_by_xpath('/html/body/div[2]')
        drop_ele_v1 = self.driver.find_element_by_xpath('/html/body/div[3]')
        drop_ele_v2 = self.driver.find_element_by_xpath('/html/body/div[4]')
        drop_ele_v3 = self.driver.find_element_by_xpath('/html/body/div[5]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele).perform()
        sleep(1)
        action.click_and_hold(drag_ele).release(drop_ele_v1).perform()
        sleep(1)
        action.drag_and_drop(drag_ele, drop_ele_v2).perform()
        sleep(1)
        action.click_and_hold(drag_ele).move_to_element(drop_ele_v3).release().perform()
        sleep(3)


    def test_keys(self):
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)





    if __name__ == '__main__':
        pytest.main(['-v', '-s', 'test_Anctionchians.py'])
        sleep(3)
