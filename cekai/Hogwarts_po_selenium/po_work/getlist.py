from selenium.webdriver.common.by import By

from Hogwarts_po1.po_work.base_page import BasePage


class ContactPage(BasePage):
    def get_department_list(self):
        # ele_list = self.driver.find_element(By.CSS_SELECTOR, '.jstree-ocl').click()
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-anchor')
        #ele_list.click()
        # print(ele_list)
        name_list = []
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list


    # def get_department_list(self):
    #     # 每次调用前刷新界面，确保获取最新的页面数据
    #     self.driver.refresh()
    #     # 获取当前部门名称
    #     department_name = self.find_all(self.__department_name)
    #     dp_name_list = [i.text for i in department_name]
    #
    #     return dp_name_list