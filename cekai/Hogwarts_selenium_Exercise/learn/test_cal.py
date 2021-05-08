"""
__author__ = 'cekai_duoduo'
__time__ = '2021/4/30 5:36 下午'
"""
import pytest
import yaml

from Hogwarts_selenium_Exercise.learn.Calculator import TestCalcula

"""

1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()

"""


def get_datas():
    with open("./cal.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def test_getdatas():
    with open("./cal.yaml") as f:
        datas = yaml.safe_load(f)
    print(datas)


class TestCalculator:
    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    def setup(self):
        self.cal = TestCalcula()

    def teardown(self):
        pass

    @pytest.mark.parametrize('a,b,expect', get_datas()['add'],
                             ids=get_datas()['ids'])
    def test_add_int(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [[0.2, 0.2, 0.4], [0.5, 0.5, 1]],
                             ids=['float1', 'float2'])
    def test_add_float(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [[3, 3, 1], [60, 20, 3]],
                             ids=['div_int1', 'div_int2'])
    def test_div_int(self, a, b, expect):
        assert expect == self.cal.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [[0.3, 0.1, 0.3], [0.9, 0.9, 1]],
                             ids=['div_float1', 'div_float2'])
    def test_div_float(self, a, b, expect):
        assert expect == round(self.cal.div(a, b))

    @pytest.mark.parametrize('a,b,expect', [[0, 2, 0], [2, 0, 0]],
                             ids=['div_zero1', 'div_zero2'])
    def test_div_zero(self, a, b, expect):
        try:
            assert expect == self.cal.div(a, b)
        except ZeroDivisionError:
            print("除数为0")
