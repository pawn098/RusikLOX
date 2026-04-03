from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CardPage(BasePage):
    PROMOCODE = 'скайуокер'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



#locator
    promo = "//input[@placeholder='Промокод или Сертификат']"   # Локатор для поля "Промокод"
    button_place_an_order = "//button[text()='Оформить заказ']" # Локатор для кнопки "Оформить заказ"

    # Получить локатор для поля "Промокод"
    def get_promo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.promo)))

    # Получить локатор для кнопки "Оформить заказ"
    def get_button_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_place_an_order)))

    # Ввести PROMOCODE в поле "Промокод" и нажать кнопку "Оформить заказ"
    def place_an_order(self):
        self.get_promo().send_keys(self.PROMOCODE)
        self.get_button_place_an_order().click()
