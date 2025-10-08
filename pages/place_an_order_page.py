from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlacePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    NAME = 'лавров'
    PHONE = '+7(777)777-77-77'

#locator
    name = "(//input[@id='client_contact_name'])[1]"
    phone = "(//input[@id='client_phone'])[1]"
    checkbox = "(//span[@class='co-toggable_field-input co-toggable_field-input--checkbox'])[1]"
    button_confirm_the_order = "(//button[@id='create_order'])[1]"
    button_repeat_order = "//a[@href='/orders/ae5d83a671743d44c6aa10c33af9f44f/duplicate']"

    def get_name(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))
    def get_phone(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    def get_checkbox(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))
    def get_button_confirm_the_order(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_confirm_the_order)))




    #Действие
    def confirm_the_order(self):
        self.get_name().send_keys(self.NAME)
        self.get_phone().send_keys(self.PHONE)
        self.move_to_elements(self.get_button_confirm_the_order())
        self.get_checkbox().click()
        self.get_button_confirm_the_order().click()

