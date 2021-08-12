import allure
import pytest
import yaml


def get_data():
    with open('cal.yaml') as f:
        data = yaml.safe_load(f)
    return data


def test_get_data():
    with open('cal.yaml') as f:
        data = yaml.safe_load(f)
    print(data)


@pytest.fixture(params=get_data()['add_float'], ids=get_data()['ids'])
def get_add_float(request):
    return request.param


def test_add_clua(get_add_float):
    print(get_add_float)


@allure.feature('计算器')
class TestCalcu:
    @allure.title('计算器加法')
    @allure.story('int_相加')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', [[1, 2, 3], [10000, 10000, 20000]], ids=['bitnum_int', 'bignum_int'])
    def test_add_int(self, initcalu_class, a, b, expect):
        assert expect == initcalu_class.add(a, b)

    def test_add_float(self, initcalu_class, get_add_float):
        assert get_add_float[2] == initcalu_class.add(get_add_float[0], get_add_float[1])

    def test_div_int(self, initcalu_class, get_div_int):
        assert get_div_int[2] == initcalu_class.div(get_div_int[0], get_div_int[1])

    def test_div_float1(self, initcalu_class, get_div_float1):
        assert get_div_float1[2] == initcalu_class.div(get_div_float1[0], get_div_float1[1])
