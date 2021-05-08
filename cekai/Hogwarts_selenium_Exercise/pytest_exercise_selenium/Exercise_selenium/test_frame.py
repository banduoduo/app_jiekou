"""
__author__ = 'cekai_duoduo'
__time__ = '2021/5/3 10:22 下午'
"""
from selenium import webdriver


class TestFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        # print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
