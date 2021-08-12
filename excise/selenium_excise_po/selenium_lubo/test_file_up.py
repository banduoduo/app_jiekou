# todo:1.将元素1拖拽到元素2，2.有弹窗等待几秒看弹窗，3.再点击运行返回原始页面
from time import sleep

from selenium.webdriver import ActionChains

from excise.selenium_excise_po.selenium_lubo.base import Base


class TestFile(Base):
    def test_file_drag_drop(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')

        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
