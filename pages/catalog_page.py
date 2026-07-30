from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#locator
    product_omega = "//form[@data-product-id='472262821']//button[@type='submit']"
    product_D3_2000_ME = "//form[@data-product-id='472263032']//button[@type='submit']"
    cart = "//a[@class='header__control-btn header__cart']"
    snackbar = "//div[contains(@class,'micro-alert-item') and contains(., 'Товар добавлен')]"

    def get_product_D3_2000_ME(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_D3_2000_ME)))
    def get_product_omega(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_omega)))
    def get_cart(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def wait_snackbar_disappear(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.snackbar)))



    #Действие



    # Добавить D3 в Корзину (мой)
    def add_product_d3_in_cart(self):
        self.get_product_D3_2000_ME().click()
        self.wait_snackbar_disappear()        # Чтобы успеть сработать клику и пропустить снекбар (перекрывает Корзину)
        self.refresh_q()
        print("D3 добавлен в корзину")



    # Добавить Omega в Корзину (мой)
    def add_product_omega_in_cart(self):
        print()
        self.get_product_omega().click()
        self.wait_snackbar_disappear()        # Чтобы успеть сработать клику и пропустить снекбар (перекрывает Корзину)
        self.refresh_q()
        print("Omega добавлен в корзину")

    # Перейти в Корзину (мой)
    def click_get_cart(self):
        self.get_cart().click()
        self.refresh_q()















