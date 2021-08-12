# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContact:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["appPackage"] = "com.tencent.tag"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_add_meber(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector().text("添加成员").instance(0));')

        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.tag:id/ays"]').send_keys('haha')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys('乐乐')
        sleep(3)
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/..//android.widget.EditText').send_keys('13211234567')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(4)
