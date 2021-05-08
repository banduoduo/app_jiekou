"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:05 下午'
"""


# def test_daka(login):
#     print('打卡')
import pytest

from Hogwarts_selenium_Exercise.pytest_exercise_selenium import Calculator


@pytest.fixture(scope='class')
def calc_class():
    calc = Calculator()
    yield calc
    print("teardown")

    @pytest.fixture(params=[[1, 1, 2], [10000, 1000, 11000]], ids=['int11', 'int111'])
    def get_add_calc(request):
        return request.param

    def test_get_calc(get_add_calc):
        print(test_get_calc)


class TestCal:
    def test_add_int(self, calc_class, get_add_calc):
        assert get_add_calc[2] == calc_class.add(get_add_calc[0], get_add_calc[1])


# class TestDiv:
#     def test_div(self, initcalc_class, get_div_datas):
#         try:
#             assert get_div_datas[2] == initcalc_class.div(get_div_datas[0], get_div_datas[1])
#         except ZeroDivisionError:
#             print("除数为0")