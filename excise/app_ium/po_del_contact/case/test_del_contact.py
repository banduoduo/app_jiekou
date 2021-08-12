from excise.app_ium.po_del_contact.page.del_app import DelApp


class TestDelContact:
    def setup_class(self):
        self.app = DelApp().start()#加上这个，就是调用这个函数里面的start方法

    def setup(self):
        self.main = self.app.goto_del_main()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_del_contact(self):
        self.main.del_main_page().del_contact_page().angage_contact_page().del_edit_page().del_meber_page().get_name_list()
