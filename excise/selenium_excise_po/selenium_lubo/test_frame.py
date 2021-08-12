# todo:1.打开百度页面点击登录，2.在弹框中点击立刻注册 输入用户名和密码 3.返回刚才的登录页面，点击登录 4.输入用户名和密码
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from excise.selenium_excise_po.selenium_lubo.base import Base


class TestFrame(Base):
    @pytest.mark.skip
    def test_switch_windows(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.XPATH, "//*[@id='s-top-loginbtn']").click()
        # todo:打印当前的窗口页面
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        # todo:打印所有的窗口页面
        print(self.driver.window_handles)
        data = self.driver.window_handles
        self.driver.switch_to_window(data[-1])
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('1234')
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('0000')
        sleep(3)
        self.driver.switch_to_window(data[0])
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@title='用户名登录']").click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # self.driver.switch_to_frame('iframeResult')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        self.driver.switch_to_default_content()
        # self.driver.switch_to.parent_frame()
        print(self.driver.find_element_by_id('submitBTN').text)
