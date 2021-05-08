import pytest


def add(x, y):
    return x + y


def test_add():
    assert add(1, 10) == 11
    assert add(1, 100) == 102


def setup_module():
    print("\nsetup_module,只执行一次，当有多个测试类的时候使用")


def teatdown_module():
    print("\nteardown_module, 只执行一次，当有多个测试类的时候使用")


class TestClass1:
    @classmethod
    def set_class(cls):
        print("\nsetup_class,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class,只执行一次")

    def set_moudle(self):
        print("\nsetup_module1,只执行一次，当有多个测试类的时候使用")

    def teardown_module(self):
        print("\nteardown_module1, 只执行一次，当有多个测试类的时候使用")

    def test_three(self):
        print("test_three, 测试用例")

    def test_four(self):
        print("test_four, 测试用例")


class TestClass2:
    @classmethod
    def setup_class(cls):
        print("\nsetup_class2,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class2,只执行一次")

    def setup_method(self):
        print("\nsetup_method, 每个测试方法都执行一次")

    def teardown_method(self):
        print("\nteardown_method, 每个测试方法都执行一次 ")

    def test_two(self):
        print("test_two, 测试用例")

    def test_one(self):
        print("test_one,测试用例")


class TestClass:

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_class(self):
        x = 'this'

        assert 'i' in x
        assert 'b' not in x

    def test_class_v1(self):
        x = 'hello'

        assert hasattr(x, 'check')


class TestOrder:
    @pytest.mark.run(order=2)
    def test_one(self):
        print("第一条测试用例")

    @pytest.mark.run(order=1)
    def test_two(self):
        print("第二条测试用例")

    @pytest.mark.run(order=-1)
    def test_three(self):
        print("第三条测试用例")


# class TestCase:
@pytest.fixture()
def login():
    print("login, 这是个登录方法")
    return ('tom', '123')


@pytest.fixture()
def operate():
    print("operate,登录后操作")


def test_case1(login, operate):
    print(login)
    print("test_case1, 需要登录")


def test_case2():
    print("test_case2，不需要登录")


def test_case3(login):
    print(login)
    print("test_case3，需要登录")
