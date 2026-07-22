import pytest

from Pages.base_page import BasePage
from utils.common_funtions import read_data_from_input_data

driver = None


@pytest.fixture(scope="class")
def open_orange_hrm(request):
    browser = read_data_from_input_data("browser")
    url = read_data_from_input_data("url")
    global driver
    basePage = BasePage(driver=None)
    driver = basePage.open_browser(browser)
    basePage.open_application(url)
    basePage.window_maximize()
    request.cls.driver = driver
    yield
    basePage.close_app()


