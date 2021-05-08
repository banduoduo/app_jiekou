from Hogwarts_selenium_Exercise.po.mainpage import MainPage


class TestAddPage:
    def test_addmeber(self):
        mainpage = MainPage()
        mainpage.goto_addmeberpage().addmeberpage().get_contact_list()

