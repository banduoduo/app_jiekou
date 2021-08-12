import pytest

from excise.selenium_excise_po.po_add_department.page.main_page import MainPage


class TestDepartment:
    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize('department', ['财务部'])
    def test_add_department(self, department):
        self.main_page.goto_contact().add_department().edit_department(department)

