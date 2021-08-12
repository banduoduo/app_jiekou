import allure
import pytest


@allure.feature('计算器')
class TestClaua:

    @allure.story('相加')
    @allure.step('int型')
    @pytest.mark.parametrize('a,b,expect', [[1, 2, 3], [1000, 2000, 3000]], ids=['int_little', 'int_big'])
    def test_add_int(self, a, b, expect):
        assert expect == a + b

    @allure.story('相加')
    @allure.step('float型')
    def test_add_float(self, initclass, add_float):
        assert add_float[2] == initclass.add(add_float[0], add_float[1])

    @allure.story('相除')
    @allure.step('int型')
    def test_div_int(self, initclass, div_int):
        assert div_int[2] == initclass.div(div_int[0], div_int[1])

    @allure.story('相除')
    @allure.step('zero型')
    def test_div_zero(self, initclass, div_zero):
        try:
            assert div_zero[2] == initclass.div(div_zero[0], div_zero[1])
        except ZeroDivisionError:
            print('除数为0')
