from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestNYApp:
    def setup(self):
        # This sample code uses the Appium python client
        # pip install Appium-Python-Client
        # Then you can paste this into a file and simply run with Python

        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.weex.nuoya"
        caps["appActivity"] = ".llmw.SplashActivity"
        caps["noReset"] = "true"
        caps["udid"] = "emulator-5554"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_nuoya(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.weex.nuoya:id/container']//android.widget.FrameLayout[2]//android.widget.FrameLayout[1]/android.widget.EditText").click()
        self.driver.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("1232121")