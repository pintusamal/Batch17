from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class DashboardPage(BasePage):
    ADMIN_BTN = (By.XPATH, '//span[text()="Admin"]')
    USERNAME_INPUT = (By.XPATH, '//label[text()="Username"]/../following-sibling::div/input[@class="oxd-input oxd-input--active"]')
    USERROLE_FILED = (By.XPATH, '(//div[@class="oxd-select-text--after"])[1]')
    STATUS_FILED_ARROW = (By.XPATH, '(//div[@class="oxd-select-text--after"])[2]')
    USERROLE_DROPDOWN_VALUE = (By.XPATH , '//div[@class="oxd-select-option"]/span[text()="Admin"]')
    EMPNAME_FILED = (By.XPATH , '//input[@placeholder="Type for hints..."]')
    FIRST_ROW_USERNAME_fIELD = (By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div")
    FIRST_ROW_USER_ROLE_fIELD = (By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[3]/div")
    FIRST_ROW_EMPLOYEE_NAME_fIELD = (By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[4]/div")
    FIRST_ROW_STATUS_fIELD = (By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[5]/div")
    SEARCH_BTM = (By.XPATH, '//button[@type="submit"]')
    RECORD_MESSAGE_TEXT = (By.XPATH, '//span[contains(normalize-space(), "Found")]')



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_admin_btn(self):
        self.click_me(self.ADMIN_BTN)

    def enter_value_in_username_field(self, usernmae_text):
        self.type_word(self.USERNAME_INPUT , usernmae_text)

    def select_value_in_userrole_field(self):
        self.click_me(self.USERROLE_FILED)
        self.click_me(self.USERROLE_DROPDOWN_VALUE)

    def enter_value_in_empname_field(self, empName):
        self.type_word(self.EMPNAME_FILED, empName)
        first_name = empName.split()[0]
        EMPNAME_SUGGESTION_FILED = (By.XPATH, f'//span[contains(text(), "{first_name}")]')
        self.click_me(EMPNAME_SUGGESTION_FILED)

    def fetch_first_row_username(self):
        username_value = self.fetch_value(self.FIRST_ROW_USERNAME_fIELD)
        return username_value

    def fetch_first_row_userrole(self):
        username_value = self.fetch_value(self.FIRST_ROW_USER_ROLE_fIELD)
        return username_value

    def fetch_first_row_employeename(self):
        username_value = self.fetch_value(self.FIRST_ROW_EMPLOYEE_NAME_fIELD)
        return username_value

    def fetch_first_row_status(self):
        username_value = self.fetch_value(self.FIRST_ROW_STATUS_fIELD)
        return username_value

    def select_userrole_field(self, userrole_text):
        self.click_me(self.USERROLE_FILED)
        locator = (By.XPATH, f'//div[@class="oxd-select-option"]/span[text()="{userrole_text}"]')
        self.click_me(locator)

    def select_status_field(self, status_text):
        self.click_me(self.STATUS_FILED_ARROW)
        locator = (By.XPATH, f'//div[@class="oxd-select-option"]/span[text()="{status_text}"]')
        self.click_me(locator)

    def click_on_search_btn(self):
        self.click_me(self.SEARCH_BTM)

    def fetch_record_value(self):
        record_value = self.fetch_value(self.RECORD_MESSAGE_TEXT)
        return record_value