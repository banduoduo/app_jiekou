import pytest

# class AddDivConftest:
#
#     def setup_class(self):
#         from excise.myself_excise.aadd_div import Adddiv
#         self.calua = Adddiv()
#
#     def teardown_class(self):
#         print("teardown_class")
import yaml

from excise.myself_excise.aadd_div import Adddiv


def pytest_collection_modifyitems(session, config, items: list):
    print("搜集所有的测试用例方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='class')
def initclass():
    calua = Adddiv()
    yield calua
    print('teardown_class')


def get_data():
    with open('div.yaml') as f:
        data = yaml.safe_load(f)
    return data


def test_getdata():
    with open('div.yaml') as f:
        data = yaml.safe_load(f)
    print(data)


@pytest.fixture(params=get_data()['div_int'], ids=get_data()['ids'])
def div_int(request):
    return request.param


def test_div_int(div_int):
    print(div_int)


@pytest.fixture(params=get_data()['div_float'], ids=get_data()['ids2'])
def div_zero(request):
    return request.param


def test_divzero(div_zero):
    print(div_int)


@pytest.fixture(params=[[0.1, 0.1, 0.2], [0.3, 0.4, 0.7]], ids=['float_little', 'float_big'])
def add_float(request):
    return request.param


def test_add_float(add_float):
    print(add_float)
