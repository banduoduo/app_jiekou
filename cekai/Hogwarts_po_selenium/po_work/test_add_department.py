from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from Hogwarts_po1.po_work.main_page import MainPage


class TestAddBu:
    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("name",[("快乐星球")])
    def test_add_department(self, name):
        adds_department = self.main_page.goto_contact().add_department().add_department_name(name).get_department_list()
        assert name in adds_department

    # @pytest.mark.parametrize("name",[("快乐星球2")])
    # def test_add_bumen_fail(self,name):
    #         add_list = self.main_page.goto_contact().add_bumen_fail(name)
    #         err = [i for i in add_list if != ""]
    #         assert "快乐星球2" in err[0]
