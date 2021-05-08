# import pytest
#
#
# class TestDate:
#     @pytest.mark.parametrize("a,b", [(10, 20), (10, 5), (3, 9)])
#     def test_pytest11(self, a, b):
#         print(a + b)

import pytest
import yaml


class TestDate:
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("data.yaml")))
    def test_pytest11(self, a, b):
        print(a + b)
