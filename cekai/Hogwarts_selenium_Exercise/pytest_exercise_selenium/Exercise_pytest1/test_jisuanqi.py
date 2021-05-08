import pytest
import allure
import yaml
#暂时改造失败，会面会再继续的

@allure.feature("计算器")
class TestJisuanqi():
    def setup(self):
        pass

    def teardown(self):
        pass

    def pytest_collect_modfiyiterms1(session, confing, iterms: list):
        print("搜集所有的测试用例方法")
        print(iterms)
        for iterm in iterms:
            iterm.name = iterm.name.encode('utf-8').decode('unicode-escape')
            iterm.nodeid = iterm.nodeid.encode('utf-8').decode('unicode-escape')


def test_getdata():
    with open('jisuanqi.yaml')as f:
        data = yaml.safe_load(f)
    print(data)


def get_data():
    with open('jisuanqi.yaml') as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture(scope='session')
def test_add(self, a, b):
    return a + b


def test_div(self, a, b):
    return a / b


print("teardown")


@pytest.fixture(params=get_data()['add_int'])
def get_add_int(request):
    return request.param


@pytest.fixture(params=get_data()['add_float'])
def get_add_float(request):
    return request.param


@pytest.fixture(params=get_data()['div_int'])
def get_div_int(request):
    return request.param


@pytest.fixture(params=get_data()['div_float'])
def get_div_float(request):
    return request.param


@pytest.fixture(params=get_data()['div_zero'])
def get_div_zero(request):
    return request.param
