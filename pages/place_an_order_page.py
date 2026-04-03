from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class PlacePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    fake = Faker('ru_RU')  # Для генерации тестовых данных на русском языке
    NAME = fake.name()
    PHONE = fake.phone_number()
    CITY = fake.address()

    #locator
    name = "(//input[@id='client_contact_name'])[1]"
    phone = "(//input[@id='client_phone'])[1]"
    city = "(//input[@id='shipping_address_full_locality_name'])[1]"
    checkbox = "(//span[@class='co-toggable_field-input co-toggable_field-input--checkbox'])[1]"
    button_confirm_the_order = "(//button[@id='create_order'])[1]"
    button_repeat_order = "//a[@href='/orders/ae5d83a671743d44c6aa10c33af9f44f/duplicate']"

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))
    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))
    def get_button_confirm_the_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_confirm_the_order)))


    #Действие

    # Заполнить поля и Оформить заказ
    def confirm_the_order(self):

        self.get_name().send_keys(self.NAME)
        print('Имя заполнено')

        self.get_phone().send_keys(self.PHONE)
        print('Телефон заполнен')

        self.get_city().send_keys(self.CITY)
        print('Адрес заполнен')

        self.move_to_elements(self.get_button_confirm_the_order())
        self.get_checkbox().click()
        print('Чекбокс активирован')

        self.get_button_confirm_the_order().click()
        print('Заказ оформлен')

