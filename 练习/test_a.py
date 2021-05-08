# import pytest
#
#
# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5
# #   好啦 后边如果需要其他版本depython 可以用pyenv 一般一个版本就够了
# # 创建虚拟环境和我刚才操作一样ok
#
# def test_answer1():
#     assert func(4) == 5
#
#
# class TestDemo:
#     def test_a(self):
#         print("a")
#
#     def b(self):
#         print("c")
#
#
# if __name__ == '__main__':
#     pytest.main(['test_a.py'])


import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("data", yaml.safe_load(open("data.yaml")))
    def test_a(self, data):
        if "test" in data:
            print("这是测试环境")
            print("测试环境的ip是：", data["test"])
        elif "dev" in data:
            print("这是开发环境")
            print("这是开发环境的ip是：", data["dev"])

    def test_b(self):
        print(yaml.safe_load(open("data.yaml")))
