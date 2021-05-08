"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/11 3:26 下午'
"""


class TestAdd:
    def test_div(self, initcalc_class, get_div_datas):
        try:
            assert get_div_datas[2] == initcalc_class.div(get_div_datas[0], get_div_datas[1])
        except ZeroDivisionError:
            print("除数为0")

# class TestCal:
#     def test_add_int(self, calc_class, get_add_calc):
#         assert get_add_calc[2] == calc_class.add(get_add_calc[0], get_add_calc[1])