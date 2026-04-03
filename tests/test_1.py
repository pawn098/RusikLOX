from pages.catalog_page import CatalogPage
from pages.cart_page import CardPage
from pages.place_an_order_page import PlacePage
from pages.finaly_page import FinalyPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_order_d3(set_up):
    CP = CatalogPage(set_up)
    CP.add_product_d3_in_cart()         # Добавить D3 в Корзину
    CP.click_get_cart()                 # Перейти в Корзину

    for i in range(2):

        CARDP = CardPage(set_up)
        CARDP.place_an_order()              # Ввести PROMOCODE в поле "Промокод" и нажать кнопку "Оформить заказ"

        PAOP = PlacePage(set_up)
        PAOP.confirm_the_order()            # Заполнить поля и Оформить заказ

        FP = FinalyPage(set_up)
        FP.click_button_repeat_order()      # Скопировать Корзину

        print(f'Цикл {i+1} пройден')
        print()

def test_order_omega(set_up):
    CP = CatalogPage(set_up)
    CP.add_product_omega_in_cart()          # Добавить Omega в Корзину
    CP.click_get_cart()                     # Перейти в Корзину

    for i in range(2):

        CARDP = CardPage(set_up)
        CARDP.place_an_order()              # Ввести PROMOCODE в поле "Промокод" и нажать кнопку "Оформить заказ"


        PAOP = PlacePage(set_up)
        PAOP.confirm_the_order()            # Заполнить поля и Оформить заказ

        FP = FinalyPage(set_up)
        FP.click_button_repeat_order()      # Скопировать Корзину

        print(f'Цикл {i+1} пройден')
        print()


def test_order_omega_and_d3(set_up):
    CP = CatalogPage(set_up)
    CP.add_product_omega_in_cart()            # Добавить Omega в Корзину
    CP.add_product_d3_in_cart()               # Добавить D3 в Корзину
    CP.click_get_cart()                       # Перейти в Корзину

    for i in range(1):

        CARDP = CardPage(set_up)
        CARDP.place_an_order()             # Ввести PROMOCODE в поле "Промокод" и нажать кнопку "Оформить заказ"

        PAOP = PlacePage(set_up)
        PAOP.confirm_the_order()            # Заполнить поля и Оформить заказ

        FP = FinalyPage(set_up)
        FP.click_button_repeat_order()      # Скопировать Корзину

        print(f'Цикл {i+1} пройден')
        print()



