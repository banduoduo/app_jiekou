"""
__author__ = 'cekai_duoduo'
__time__ = '2021/4/30 5:36 下午'
"""
import pytest
import allure

from Hogwarts_selenium_Exercise.learn.learn_fixture.conftest import get_datas


@pytest.mark.last
@pytest.fixture(params=get_datas()['add'], ids=get_datas()['ids'])
def get_add(request):
    return request.param


def test_get_add(get_add):
    print(get_add)


@pytest.mark.run(order=1)
@pytest.fixture(params=get_datas()['div'], ids=get_datas()['ids2'])
def get_div(request):
    return request.param


def test_get_div(get_div):
    print(get_div)


@allure.feature("计算器")
class TestJSQ:

    @allure.story("相加")
    def test_add_all(self, getint_class, get_add):
        assert get_add[2] == getint_class.add(get_add[0], get_add[1])

    @allure.story("相除")
    def test_div_all(self, getint_class, get_div):
        try:
            assert get_div[2] == getint_class.div(get_div[0], get_div[1])
        except ZeroDivisionError:
            print("除数为0")

# allure
# 帮助：pytest --help|grep allure
# 生成文件：pytest --alluredir=./result(文件名)
# 进入allure报告页面：allure serve ./result
