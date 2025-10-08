from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#locator
    product_D3_2000_ME = "(//button[text()='В корзину'])[2]"
    cart = "//a[@class='header__control-btn header__cart']"

    def get_product_D3_2000_ME(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_D3_2000_ME)))
    def get_cart(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))



    #Действие
    def click_get_product_D3_2000_ME_cart(self):
        self.get_product_D3_2000_ME().click()
        self.get_cart().click()
        self.refresh_q()














