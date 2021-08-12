from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excise.myself_excise.base import Base


class TestClick(Base):
    def test_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        sigle_click = self.driver.find_element(By.XPATH, '//*[@value="click me"]')
        double_click = self.driver.find_element(By.XPATH, '//*[@value="dbl click me"]')
        right_click = self.driver.find_element(By.XPATH, '//*[@value="right click me"]')
        action = ActionChains(self.driver)

        WebDriverWait(self.driver, 4).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@value="click me"]')))
        action.click(sigle_click)
        action.double_click(double_click)
        action.context_click(right_click)

        action.perform()

    def test_move_to_shubiao(self):
        self.driver.get("https://www.baidu.com/")
        set = self.driver.find_element(By.ID, 's-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(set).perform()

    def test_drag_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag = self.driver.find_element_by_id('dragger')
        drop = self.driver.find_element_by_xpath('//*[@lang="en"]//div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag, drop).perform()
        action.click_and_hold(drag).release(drop).perform()
        sleep(3)

    def test_space(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        self.driver.find_element_by_xpath('/html/body/label[1]/input').click()
        action = ActionChains(self.driver)
        action.send_keys('haha').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(2)

    def test_alert_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, 'draggable')))
        drag1 = self.driver.find_element_by_id('draggable')
        drop1 = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag1, drop1).perform()
        sleep(3)
        self.driver.switch_to.alert.accept()
        sleep(4)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        sleep(3)
        self.driver.find_element_by_id('submitBTN').click()
        sleep(4)

    #  todo:1.打开百度页面点击登录，2.在弹框中点击立刻注册 输入用户名和密码 3.返回刚才的登录页面，点击登录 4.输入用户名和密码
    def test_switch_to_windowns(self):
        self.driver.get('https://www.baidu.com/')
        sleep(2)
        self.driver.find_element_by_id('s-top-loginbtn').click()
        sleep(2)
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element_by_css_selector('.pass-reglink.pass-link').click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        windown1 = self.driver.window_handles
        self.driver.switch_to_window(windown1[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('123ff')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('1123345')
        sleep(3)
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.switch_to_window(windown1[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('qw445')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('1234666')
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)

    def test_js(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2021-1-03'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)


class TestTouch:
    def setup_class(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def test_touch_baidu(self):
        self.driver.get('https://www.baidu.com/')
        top = self.driver.find_element_by_id('kw')
        top.send_keys('elenium测试')
        click_baidu = self.driver.find_element_by_id('su')
        action = TouchActions(self.driver)
        action.tap(click_baidu)
        sleep(3)
        action.scroll_from_element(top, 0, 10000)
        action.perform()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@class="page-inner"]//a[last()]').click()

        sleep(3)
