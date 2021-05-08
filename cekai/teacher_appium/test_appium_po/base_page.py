from appium import webdriver


class TestAddMeber:
    def addmeber(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(4)
