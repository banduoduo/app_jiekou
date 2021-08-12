from appium import webdriver

from excise.app_ium.po_del_contact.page.base_del import DelBasePage
from excise.app_ium.po_del_contact.page.del_main_page import DelMainPage


class DelApp(DelBasePage):

    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["appPackage"] = "com.tencent.tag"
            caps["noReset"] = "true"
            caps["deviceName"] = "127.0.0.1:7555"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
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

    def goto_del_main(self):
        return DelMainPage(self.driver)
