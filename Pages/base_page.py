from selenium import webdriver
from selenium.common import NoSuchElementException, exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, browser):
        if browser == "chrome":
            self.driver = self.open_chrome()
        elif browser == "firefox":
            self.driver = self.open_firefox()
        else:
            self.driver = self.open_edge()
        return self.driver


    def open_chrome(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def open_firefox(self):
        self.driver = webdriver.Firefox()
        return self.driver

    def open_edge(self):
        self.driver = webdriver.Edge()
        return self.driver
    
    def open_application(self, url):
        self.driver.get(url)

    def window_maximize(self):
        self.driver.maximize_window()

    def close_app(self):
        self.driver.close()


    def get_web_element(self, locator):
        try:
            self.wait_for_object(locator)
            element  = self.driver.find_element(locator[0], locator[1])
            return element
        except NoSuchElementException:
            print("element is not present in the page")
            raise exceptions.NoSuchElementException

    def type_word(self, locator, value):
        element = self.get_web_element(locator)
        self.wait_for_object(locator)
        element.send_keys(value)

    def click_me(self,locator):
        self.wait_for_object(locator)
        element = self.get_web_element(locator)
        element.click()

    def javascript_click(self,locator):
        element = self.get_web_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def action_chain_click(self, locator):
        element = self.get_web_element(locator)
        action = ActionChains(self.driver)
        action.click(element).perform()

    def wait_for_object(self,locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def fetch_value(self, locator):
        self.wait_for_object(locator)
        element = self.get_web_element(locator)
        return element.text