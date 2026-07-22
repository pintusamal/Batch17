from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN = (By.XPATH, '//button[@type="submit"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    def enter_username(self, usernamevalue):
        self.type_word(self.USERNAME, usernamevalue)

    def enter_password(self, passwordvalue):
        self.type_word(self.PASSWORD, passwordvalue)

    def click_on_submit_btn(self):
        self.click_me(self.LOGIN)
