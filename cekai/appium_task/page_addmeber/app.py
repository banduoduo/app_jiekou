# app.py  app相关的操作，启动，关闭，重启
from appium import webdriver

from appium_task.page_addmeber.base_page import BasePage
from appium_task.page_addmeber.main_page import MainPage


class App(BasePage):
    # 启动
    def start(self):
        if self.driver == None:
            # 启动app
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["settings[waitForIdleTimeout]"] = 0
            # caps['dontStopAppOnReset'] = True
            caps["noReset"] = "true"
            caps['skipDeviceInitialization'] = True
            # 客户端与服务端建立连接的代码
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待,更智能，中间任何时间等到某个元素都停止查找，继续往后执行，
            # 每次调用find_element的时候都会激活这种等待方式
            self.driver.implicitly_wait(5)
            # 需要return self 在其他页面才能调用到app里的方法
        else:
            print("复用driver")
            self.driver.launch_app()
        return self

    # 重启
    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    # 关闭
    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # app 需要入口
        return MainPage(self.driver)
