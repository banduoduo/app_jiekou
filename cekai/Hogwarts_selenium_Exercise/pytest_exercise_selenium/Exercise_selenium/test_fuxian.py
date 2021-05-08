from time import sleep

import yaml
from selenium import webdriver


class TestFuxian:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("霍格沃茨测试学院")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        ele = self.driver.find_element_by_link_text("霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele


class TestWework:

    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())

        cookie = self.driver.get_cookies()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies = [{'domain': '.qq.com', 'expiry': 1618579490, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850128090655'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'y0OHzo2-lgSxoc6dW5Qud1CJ90FIma5CjC-26QB9cU_QENO89fWpu43xNYqJHNfg0uTUfCNrQjEfgY2tFo19f9WVAlTj-actPpQ85khdnFPzCKtN4rFwnf_-BTm-rAuVPbJ2GBjuApreDa_E8RY4Hd0-IctkUpfsHFjE4o4wgipQ9y0Uwh0kYFSsX69205wN_WvxE6woVqLIL9HFdseJGN8ktdMdRe9yM9exFmmpWRVmFUHQL5twy3Gdz47Tuxj-_TdUeuVdtKMM4jIDgMFO1A'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850128090655'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324994447222'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3866533'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Ifn_NSfnsF7gXILSa_boehJDxn5WaS7KuF7iwibR1Q5NImMbl2vHX996Iqg-3pth'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650115268, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618577903,1618578783,1618579142,1618579269'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618579269'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '30606841461268607'}, {'domain': '.qq.com', 'expiry': 1618665743, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1352057508.1618499602'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618609439, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2f43cff'}, {'domain': '.qq.com', 'expiry': 1681651343, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1472235149.1618499602'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650035595, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621171430, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]

        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)

    def test_cookie_v2(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data.yaml", encoding="UTF-8")as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)