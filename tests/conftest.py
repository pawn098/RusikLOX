import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.base_page import BasePage


@pytest.fixture()
def set_up():
    print()
    print()
    print('Начало теста')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    driver.get('https://litte-dev-shop.appprod.ru/collection/all')
    driver.maximize_window()

    base_page = BasePage(driver)
    base_page.handle_dev_password()

    yield driver
    print('Конец теста')
    #driver.quit()