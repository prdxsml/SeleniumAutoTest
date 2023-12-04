from pages.main_page import MainPage
from pages.product_page import ProductPage
import time
import pytest

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()

# def test_button(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.button()

# def test_click_on_button(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_on_button()
#     time.sleep(10)
#     page.item_on_basket()
#     page.correct_title_on_message()
#     page.correct_price_on_basket()

# Тест перехода по линке на странице. Переход между страницами. Тут мы и опишем проверки на правильность корзины.
# def test_basket_link(browser):
#     # Берем линку для проверки
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     # Работаем с этой страницей
#     page = ProductPage(browser, link)
#     # Открываем страницу
#     page.open()
#     # Кликаем по кнопке / Срабатывает алерт на сайте / подставляем в него функцию из BasePage
#     page.click_on_button()
#     # Спи нахуй (Ждем пока сервер раздуплится и покажет уведомления)
#     time.sleep(10)
#     # Ищем и находим линк на корзину, переходим по нему
#     page.basket_link()
#     # Теперь работаем со страницей корзины
#     basket_page = ProductPage(browser, browser.current_url)
#     # Проверяем что линка это действительно линка корзины, а не конской залупы
#     basket_page.should_be_basket_url()
#     # Проверяем что цены на странице есть и что одна цена - это цена товара,
#     # а другая цены корзины. Понятно, что последняя будет меняться при добавлении товара
#     # и они будут не равны, но похуй (допилим позже), задача стояла проверить цену одного товара.
#     basket_page.basket_all_price()


# @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"



# product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# urls = [f"{product_link}/?promo=offer{no}" for no in range(10)]



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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


# def test_guest_cant_see_success_message:

# def test_message_disappeared_after_adding_product_to_basket: