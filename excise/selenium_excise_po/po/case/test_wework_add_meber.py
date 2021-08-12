from time import sleep

import pytest


from excise.selenium_excise_po.po.page.main_page import MainPage


class TestMeber:
    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.parametrize('username,accid,phone', [['测试A', '006', '13807850025']])
    def test_wework_add(self, username, accid, phone):
        hh_list = self.main.goto_add_meber().add_meber(username, accid, phone).add_name_List()
        print(hh_list)
        assert username in hh_list


    @pytest.mark.parametrize('username,accid,phone', [['ho', '077', '13807850025']])
    def test_wework_add_fail(self, username, accid, phone):
        data_list = self.main.goto_add_meber().add_meber_fail(username, accid, phone).daa_name_list_fail()
        sleep(8)
        err = [i for i in data_list if i != ""]
        print(err)
        assert "该手机已被“测试A”占有" in err[0]
