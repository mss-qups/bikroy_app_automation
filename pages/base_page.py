from time import sleep


# from selenium.webdriver.common.action_chains import ActionChains
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction


class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def click_by_id(self, locator):
        sleep(1)
        self.driver.find_element_by_id(locator).click()

    def click_by_class_name(self, locator):
        sleep(1)
        self.driver.find_element_by_class_name(locator).click()

    def clear_data(self, locator):
        self.driver.find_element(locator).clear()

    def send_data(self, data, locator):
        # self.driver.implicitly_wait(1)
        sleep(1)
        self.driver.find_element_by_id(locator).set_value(data)

    def is_element_displayed(self, locator):
        val = self.driver.find_element(locator).is_displayed()
        return val

    def get_attribute_value(self, attributeName, locator):
        val = self.driver.find_element(locator).get_attribute(attributeName)
        return val

    def go_back(self):
        self.driver.implicitly_wait(1)
        self.driver.back()
        # sleep(1)

    def find_element(self, locator):
        return self.driver.find_element(locator)

    # Search for multiple elements
    def find_elements(self, locator):
        elements = self.driver.find_element(locator)
        return elements

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0,0)")