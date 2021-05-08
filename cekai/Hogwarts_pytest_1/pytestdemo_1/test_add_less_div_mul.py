import pytest

from Calculator import Calculator


@pytest.fixture(scope='class')
def calc_class():
    calc = Calculator()
    yield calc
    print("teardown")


class TestCal:


    # def setup_class(self):
    #     print("setup")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("teardown")
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [10000, 1000, 11000]], ids=['int11', 'int111'])
    def test_add_int(self, calc_class, a, b, expect):
        assert expect == calc_class.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.4, 0.8, 1.2]], ids=['float22', 'float222'])
    def test_add_float(self, calc_class, a, b, expect):
        assert expect == round(calc_class.add(a, b), 2)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 0], [20, 10, 10]
    ], ids=['int1', 'int_1'])
    def test_less_int(self, calc_class, a, b, expect):
        assert expect == calc_class.less(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.5, 0.1, 0.4], [1.8, 0.8, 1]], ids=['float1', 'float_1'])
    def test_less_float(self, calc_class, a, b, expect):
        assert expect == calc_class.less(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [1000, 1, 1000]
    ], ids=['int2', 'int_2'])
    def test_div_int(self, calc_class, a, b, expect):
        assert expect == (calc_class.div(a, b))

    @pytest.mark.parametrize('a,b,expect', [
        [0.4, 0.2, 0.2], [10, 1, 10]
    ], ids=['float2', 'float2_2'])
    def test_div_float(self, calc_class, a, b, expect):
        assert expect == calc_class.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0, 1, 0], [10, 0, 0]
    ], ids=['zero1', 'zero2'])
    def test_div_zero(self, calc_class, a, b, expect):
        assert expect == calc_class.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [1000, 1, 1000]
    ], ids=['int3', 'int_3'])
    def test_mul_int(self, calc_class, a, b, expect):
        assert expect == calc_class.mul(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.4, 0.2, 0.08], [10, 1, 10]
    ], ids=['float3', 'float_3'])
    def test_mul_float(self, calc_class, a, b, expect):
        assert expect == round(calc_class.mul(a, b), 2)
