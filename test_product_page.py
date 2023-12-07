from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time
import pytest


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


def test_guest_can_add_product_to_basket(browser):
    # Сюда подставляем линк, проверяемой страницы
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # Указывем какие методы, фикстуры и с какой страницы используем
    page = ProductPage(browser, link)
    # Метод открытия страниц
    page.open()
    # Метод клика по кнопке и подстановки решения
    page.click_on_button()
    # Ждем сервера
    time.sleep(10)
    # Метод проверки и выгребания тайтла со страницы. Ипользуется сравнение внутри
    page.title_equally_title_on_message()
    # Метод проверки цены и выгребания со страницы. Ипользуется сравнение внутри
    page.price_equally_price_on_basket()


# Чтобы скормить демону пулл из документов надо будет разбить ссылки на строки и написать алгоритм подстановки и проверки
# его в цикле(вероятно). Надо подумать над реализацией.
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # Сюда подставляем линк, проверяемой страницы
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    # Указывем какие методы, фикстуры и с какой страницы используем
    page = ProductPage(browser, link)
    # Метод открытия страниц
    page.open()
    # Метод клика по кнопке и подстановки решения
    page.click_on_button()
    # Ждем сервера
    time.sleep(10)
    # Метод проверки и выгребания тайтла со страницы. Ипользуется сравнение внутри
    page.title_equally_title_on_message()
    # Метод проверки цены и выгребания со страницы. Ипользуется сравнение внутри
    page.price_equally_price_on_basket()


@pytest.mark.reg
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = 'humph-misuse-wing'
        page.register_new_user(email,password)
        time.sleep(10)
        page.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.user_cant_see_success_message_after_adding_product_to_basket()

    def test_guest_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()



# Негативные тесты
"""
1. Открываем страницу товара
2. Добавляем товар в корзину
3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
"""
@pytest.mark.negative_test
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

""" 
1. Открываем страницу товара
2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
"""
@pytest.mark.negative_test
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()


"""
1. Открываем страницу товара
2. Добавляем товар в корзину
3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
"""
@pytest.mark.negative_test
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_message_disappeared_after_adding_product_to_basket()

