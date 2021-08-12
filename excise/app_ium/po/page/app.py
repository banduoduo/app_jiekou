from appium import webdriver

from excise.app_ium.po.page.base_page import BasePage
from excise.app_ium.po.page.main_page import MainPage


class App(BasePage):
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
            print("复用 driver")
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main_page(self):
        return MainPage(self.driver)
