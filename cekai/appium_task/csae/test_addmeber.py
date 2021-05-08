"""
1、添加联系人测试用例 实现PO封装
2、将日志 保存到日志文件中，打印输出日志时间

"""
from faker import Faker

from cekai.appium_task.page_addmeber.app import App


class TestAddMeber:

    def setup_class(self):
        self.faker = Faker('zh_CN')

    def setup(self):
        self.app = App()
        # 需要app 的start里返回return self 才能调用app里面的 goto_main方法
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def teardown_class(self):
        print("添加成功")

    def test_add_meber(self):
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.main.goto_contact().goto_add_meber().manual_input().edit_meber(name, phonenum).find_toast()
