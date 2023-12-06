import time
import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage

# ! Страница для добавления тестов. Соотносится со страницей: main_page.py
# ! По этому же примеру оформляются другие тесты для страниц: ***_page.py == test_***_page.py
# ! Под разные тесты можно создать разные файлы с определенными классами, а можно сделать как тут:
# ! подсобывать в параметр page = нужный класс и через него проверять методами, описанными в этом классе


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    # link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    # Указываем на каком линке будем проверять
    link = "http://selenium1py.pythonanywhere.com"
    # Указываем через какой класс и какими методами будет проводить тест
    page = MainPage(browser, link)
    # Открываем ссылку. Она кроссится с фикстурами в base
    page.open()
    # Запускаем метод описанный в классе
    page.go_to_login_page()


def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

@pytest.mark.test2
def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

    """
    1. Гость открывает главную страницу 
    2. Переходит в корзину по кнопке в шапке сайта
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста
    """
@pytest.mark.test1
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = BasketPage(browser, link)
    page.open
    # time.sleep(15)
    page.go_to_basket_page()
    # page.guest_basket_button_exists()
    # page.guest_click_basket_button()
    # page.guest_basket_clear()