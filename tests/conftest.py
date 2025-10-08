import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    print('Начало теста')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    driver.get('https://litte-dev-shop.appprod.ru/collection/all')
    driver.maximize_window()

    yield driver
    print('Конец теста')
    #driver.quit()