from excise.app_ium.po.po1.page.app_add import AppAdd
from excise.app_ium.po.po1.utils.contact_add_info import ContactInfoAdd


class TestAddMeber:

    def setup_class(self):
        self.coninfo = ContactInfoAdd()
        self.app = AppAdd().start()

    def setup(self):
        self.main = self.app.goto_main_add()

    def teartown(self):
        pass

    def teartown_class(self):
        self.app.stop()

    def test_meber_add(self):
        name = self.coninfo.add_name()
        phone_num = self.coninfo.add_phone()
        self.main.main_add().contact_add().meber_add().edit_add(name, phone_num).find_toast()
