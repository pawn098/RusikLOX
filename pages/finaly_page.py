from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FinalyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locator
    button_repeat_order = "//a[text()='Повторить заказ']"


    def get_button_repeat_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_repeat_order)))


    # Действие
    def click_button_repeat_order(self):
        self.get_button_repeat_order().click()