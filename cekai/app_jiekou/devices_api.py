# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestApi:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # 模拟在测试中来电和发短信
        self.driver.make_gsm_call('18217457772', GsmCallActions.CALL)
        self.driver.send_sms('18217374490', 'hello appium api')
        # 模拟把数据更改为飞行模式再变为wifi模式
        self.driver.set_network_connection(1)
        sleep(9)
        # 把前面和后面的操作截图下来并保存在一个文件夹中
        self.driver.get_screenshot_as_file('./photos/img.png')
        self.driver.set_network_connection(2)
        sleep(9)


