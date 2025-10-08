from pages.catalog_page import CatalogPage
from pages.cart_page import CardPage
from pages.place_an_order_page import PlacePage
from pages.finaly_page import FinalyPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def test_1(set_up):
    CP = CatalogPage(set_up)
    CP.click_get_product_D3_2000_ME_cart()

    for i in range(20):

        CARDP = CardPage(set_up)
        CARDP.place_an_order()

        PAOP = PlacePage(set_up)
        PAOP.confirm_the_order()

        FP = FinalyPage(set_up)
        FP.click_button_repeat_order()






