from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time
import pytest

"""
Страница для добавления тестов. Соотносится со страницей: main_page.py
По этому же примеру оформляются другие тесты для страниц: ***_page.py == test_***_page.py
Под разные тесты можно создать разные файлы с определенными классами, а можно сделать как тут:
подсобывать в параметр page = нужный класс и через него проверять методами, описанными в этом классе
"""

# Тест проверки перехода между страницами - ok
def test_guest_can_go_to_login_page(browser: WebDriver):
    # Стартовый линк
    link = "http://selenium1py.pythonanywhere.com"
    # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    #Открываем страницу
    page.open()
    # Выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()


# Тест проверки наличия ссылки, которая ведет на логин - ok
def test_guest_should_see_login_link(browser: WebDriver):
    # Указываем на каком линке будем проверять
    link = "http://selenium1py.pythonanywhere.com"
    # Указываем через какой класс и какими методами будет проводить тест
    page = MainPage(browser, link)
    # Открываем ссылку. Она кроссится с фикстурами в base
    page.open()
    # Запускаем метод описанный в классе
    page.go_to_login_page()


def test_should_be_login_url(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


# Тест перехода в корзину под гостем
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.button_basket()
    time.sleep(10)
    page.button_basket_click()
    time.sleep(10)
    page.check_is_basket_clear()
    time.sleep(10)
    page.text_is_basket_clear()
    time.sleep(10)
