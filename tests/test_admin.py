import time

import pytest

from Pages.admin_page import DashboardPage
from Pages.login_page import LoginPage
from utils.common_funtions import read_data_from_input_data


class TestAdmin:

    @pytest.mark.usefixtures("open_orange_hrm")
    def test_verify_admin_functionality(self):
        username = read_data_from_input_data("username")
        pwd = read_data_from_input_data("password")
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(pwd)
        login_page.click_on_submit_btn()
        admin_page = DashboardPage(self.driver)
        admin_page.click_admin_btn()
        admin_page.enter_value_in_username_field("Admin")
        admin_page.select_value_in_userrole_field()
        admin_page.enter_value_in_empname_field("Adolph Gerlach")
        time.sleep(5)

    @pytest.mark.usefixtures("open_orange_hrm")
    def test_capture_first_row_data_and_verify(self):
        username = read_data_from_input_data("username")
        pwd = read_data_from_input_data("password")
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(pwd)
        login_page.click_on_submit_btn()
        admin_page = DashboardPage(self.driver)
        admin_page.click_admin_btn()
        username = admin_page.fetch_first_row_username()
        user_role = admin_page.fetch_first_row_userrole()
        emp_name = admin_page.fetch_first_row_employeename()
        status = admin_page.fetch_first_row_status()

        admin_page.enter_value_in_username_field(username)
        admin_page.select_userrole_field(user_role)
        admin_page.enter_value_in_empname_field(emp_name)
        admin_page.select_status_field(status)

        admin_page.click_on_search_btn()
        time.sleep(2)
        act_message = admin_page.fetch_record_value()
        assert   "(1) Record Found" in act_message


