"""
1、删除联系人用例 实现PO封装
2、将日志 保存到日志文件中，打印输出日志时间
"""
from cekai.appium_task.page_delcontact.del_app import DelApp


class TestDelMeber:

    def setup_class(self):
        pass

    def setup(self):
        self.app = DelApp()
        # 需要app 的start里返回return self 才能调用app里面的 goto_main方法
        self.delmain = self.app.start().goto_del_main()

    def teardown(self):
        self.app.stop()

    def teardown_class(self):
        print("添加成功")

    def test_del_meber(self):
        self.delmain.goto_delcontact().manage_contacts().editpage().edit_del().del_person().editpage()
