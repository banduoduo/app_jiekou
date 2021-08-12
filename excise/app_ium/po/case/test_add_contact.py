from excise.app_ium.po.page.app import App
from excise.app_ium.po.utils.contact_info import ContactInfo


class TestAddMeber:
    def setup_class(self):
        self.contactinfo = ContactInfo()
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_add_meber(self):
        name = self.contactinfo.get_name()
        phonenum = self.contactinfo.get_phonenum()
        self.main.main_page().get_namelist().add_meber().edit_add_meber(name, phonenum).find_toast()
