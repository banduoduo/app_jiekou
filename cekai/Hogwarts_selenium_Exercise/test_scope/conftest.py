import pytest


@pytest.fixture(scope="session")
def open():
    print('打开浏览器')
    yield
    print("执行teardown")
    print("最后关闭浏览器")
