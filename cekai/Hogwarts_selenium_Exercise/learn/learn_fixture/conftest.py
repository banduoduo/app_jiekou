"""
__author__ = 'cekai_duoduo'
__time__ = '2021/4/30 8:53 下午'
"""
import pytest
import yaml

from Hogwarts_selenium_Exercise.learn.learn_fixture.Calculator import TestCalcula


def get_datas():
    with open("./cal.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def test_getdatas():
    with open("./cal.yaml") as f:
        datas = yaml.safe_load(f)
    print(datas)


@pytest.fixture(scope='class')
def getint_class():
    print("开始计算")
    cal = TestCalcula()
    yield cal
    print("计算结束")


def pytest_collection_modifyitems(session, config, items: list):
    print("这是收集所有测试用例的方法")
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
