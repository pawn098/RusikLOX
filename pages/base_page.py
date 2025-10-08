from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)


    def refresh_q(self):
        self.driver.refresh()

    def move_to_elements(self, getter):
        self.action.move_to_element(getter).perform()


