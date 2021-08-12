from appium import webdriver

from excise.app_ium.po.po1.page.base_add import BaseAdd
from excise.app_ium.po.po1.page.main_add import MainAdd


class AppAdd(BaseAdd):

    def start(self):

        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["appPackage"] = "com.tencent.tag"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)

        else:
            print('复用 driver')
        return self

    def stop(self):
        self.driver.quit()

    def goto_main_add(self):
        return MainAdd(self.driver)
