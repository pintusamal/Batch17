import pytest

from Pages.login_page import LoginPage
from utils.common_funtions import read_data_from_input_data


class TestLogin:

    @pytest.mark.usefixtures("open_orange_hrm")
    def test_verify_login_funciton(self):
        username = read_data_from_input_data("username")
        pwd = read_data_from_input_data("password")
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(pwd)
        login_page.click_on_submit_btn()