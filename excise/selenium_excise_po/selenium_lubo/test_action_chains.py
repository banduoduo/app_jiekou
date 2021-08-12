# todo:点击右键，s双击操作
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from excise.selenium_excise_po.selenium_lubo.base import Base


class TestActonChans(Base):

    @pytest.mark.skip
    def test_right_double(self):
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        ele_click = self.driver.find_element(By.XPATH, "//*[@value='click me']")
        double_click = self.driver.find_element(By.XPATH, "//*[@value='dbl click me']")
        right_click = self.driver.find_element(By.XPATH, "//*[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.double_click(double_click)
        action.context_click(right_click)
        sleep(3)
        action.perform()
        sleep(3)

    # todo:把鼠标移动到某个元素上
    @pytest.mark.skip
    def test_move_to(self):
        self.driver.get("https://www.baidu.com/")
        ele_move = self.driver.find_element(By.ID, 's-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele_move)
        action.perform()
        sleep(3)

    # todo:拖拽，从上面拖拽到下面
    @pytest.mark.skip
    def test_darg_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        ele_drag = self.driver.find_element(By.ID, 'dragger')
        ele_drop = self.driver.find_element_by_xpath("//*[@lang='en']//div[2]")
        ele_drop1 = self.driver.find_element_by_xpath("//*[@lang='en']//div[3]")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop).perform()
        action.click_and_hold(ele_drag).release(ele_drop1).perform()
        sleep(3)

    # todo:模拟按键方法
    def test_key(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("用户名").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main(['v', '-s', 'test_action_chains.py'])
