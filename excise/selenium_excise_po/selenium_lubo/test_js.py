from time import sleep

import pytest

from excise.selenium_excise_po.selenium_lubo.base import Base


class TestJS(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # todo：输入'selenium测试'点击百度一下
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        # todo:滑到最底部点击下一页
        self.driver.execute_script("document.documentElement.scrollTop='10000'")
        self.driver.find_element_by_xpath("//*[@id='page']//a[last()]").click()
        sleep(3)

    # todo:先把readonly属性删掉之后，才能更改时间控件
    def test_time_antion(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2021-05-20'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

