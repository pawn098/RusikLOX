from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CardPage(BasePage):
    PROMO = 'лавров'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



#locator
    promo = "//input[@placeholder='Промокод или Сертификат']"
    button_place_an_order = "//button[text()='Оформить заказ']"

    def get_promo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.promo)))
    def get_button_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_an_order)))

    def place_an_order(self):
        self.get_promo().send_keys(self.PROMO)
        self.get_button_place_an_order().click()
