import pytest

# todo：使用fixture实现setup和teardown
import yaml

from excise.pytest_Calculator_allure.calculator import Calculator


@pytest.fixture(scope='class')
def initcalu_class():
    calc = Calculator()
    yield calc
    print("打印setup+teardown功能")


def pytest_collection_modifyitems(session, config, items: list):
    print("搜集所有的测试用例方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def get_data():
    with open('cal.yaml') as f:
        data = yaml.safe_load(f)
    return data


def test_get_data():
    with open('cal.yaml') as f:
        data = yaml.safe_load(f)
    print(data)


@pytest.mark.run(order=0)
@pytest.fixture(params=get_data()['add_float'], ids=get_data()['ids'])
def get_add_float(request):
    return request.param


def test_add_clua(get_add_float):
    print(get_add_float)


@pytest.mark.run(order=3)
@pytest.fixture(params=[[20, 10, 2], [1000, 0, False]], ids=['整数除', '除数为0'])
def get_div_int(request):
    return request.param


def test_div_calc(get_div_int):
    print(get_div_int)


@pytest.mark.run(order=2)
@pytest.fixture(params=[[0.5, 0.1, 5], [1000, 500, 2]], ids=['小数除', '大数除'])
def get_div_float1(request):
    return request.param


def test_div_calc1(get_div_float1):
    print(get_div_float1)
