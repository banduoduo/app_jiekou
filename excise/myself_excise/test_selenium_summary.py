from time import sleep

import allure
import pytest
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from excise.myself_excise.base import Base


class TestAction(Base):

    @pytest.mark.skip
    @allure.story('点击操作')
    def test_action_chinas(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        ele_click = self.driver.find_element_by_xpath("//*[@value='click me']")
        ele_double = self.driver.find_element_by_xpath("//*[@value='dbl click me']")
        ele_three = self.driver.find_element_by_xpath("//*[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_three)
        action.double_click(ele_double)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    @allure.story('移动鼠标')
    def test_move(self):
        self.driver.get('https://www.baidu.com/')
        ele_move_to = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele_move_to)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    @allure.story('按住鼠标拖拽到某个地方')
    def test_drag_and_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag = self.driver.find_element_by_id('dragger')
        drop1 = self.driver.find_element_by_xpath("//*[@lang='en']//div[2]")
        drop2 = self.driver.find_element_by_xpath("//*[@lang='en']//div[3]")
        drop3 = self.driver.find_element_by_xpath("//*[@lang='en']//div[4]")
        drop4 = self.driver.find_element_by_xpath("//*[@lang='en']//div[5]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop1).perform()
        action.click_and_hold(drag).release(drop2).perform()
        sleep(3)
        action.click_and_hold(drag).release(drop3).perform()
        action.drag_and_drop(drag, drop4).perform()
        sleep(3)

    @pytest.mark.skip
    @allure.story('模拟按键空格')
    def test_space_backspace(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys('abc').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

    @pytest.mark.skip
    def test_alert_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')

        drag22 = self.driver.find_element_by_id('draggable')
        drop22 = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag22, drop22).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(3)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()

    @pytest.mark.skip
    def test_windows_learn(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath("//*[@id='s-top-loginbtn']").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        data = self.driver.window_handles
        self.driver.switch_to.window(data[-1])
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('1234')
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('0000')
        self.driver.switch_to_window(data[0])
        self.driver.find_element(By.XPATH, "//*[@title='用户名登录']").click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)

    @pytest.mark.skip
    def test_js1(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        ele_js = self.driver.execute_script("return document.getElementById('su')")
        ele_js.click()
        self.driver.execute_script("document.documentElement.scrollTop='10000'")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']//a[last()]").click()
        sleep(3)

    def test_data_time(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-05-20'")
        sleep(5)
        print(self.driver.execute_script("document.getElementById('train_date').value"))
