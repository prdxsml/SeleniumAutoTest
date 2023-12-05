# from pages.main_page import MainPage
from pages.product_page import ProductPage
# import time
# import pytest

# Должен падать - ok
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.netative_button_click()
    page.user_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.user_cant_see_success_message_after_adding_product_to_basket()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.netative_button_click()
    page.is_disappeared()

