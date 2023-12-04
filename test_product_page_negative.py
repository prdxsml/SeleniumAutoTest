# from pages.main_page import MainPage
from pages.product_page import ProductPage
# import time
# import pytest

# Чтобы скормить демону пулл из документов надо будет разбить ссылки на строки и написать алгоритм подстановки и проверки
# его в цикле(вероятно). Надо подумать над реализацией.
# @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])

# def test_what_in_title_and_price(browser, promo_offer):
#     # Сюда подставляем линк, проверяемой страницы
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     # Указывем какие методы, фикстуры и с какой страницы используем
#     page = ProductPage(browser, link)
#     # Метод открытия страниц
#     page.open()
#     # Метод клика по кнопке и подстановки решения
#     page.click_on_button()
#     # Ждем сервера
#     time.sleep(10)
#     # Метод проверки и выгребания тайтла со страницы. Ипользуется сравнение внутри
#     page.title_equally_title_on_message()
#     # Метод проверки цены и выгребания со страницы. Ипользуется сравнение внутри
#     page.price_equally_price_on_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button()
    page.is_disappeared()