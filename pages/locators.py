from selenium.webdriver.common.by import By
from selenium import webdriver

# ! Страница локаторов. Опеределяем переменные и переиспользуем в проекте.


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    URL_LINK = 'login'
    #? Чекаем существование формы логина, именно формы, а не полей
    # ? Сначала пишем красные тесты, чтобы проверки падали, затем проверяем зелеными тестами
    FORM_AUTH_CHECK = (By.CSS_SELECTOR, '#login_form')
    #? Чекаем существование формы регистрации, именно формы, а не полей
    FORM_REG_CHECK = (By.CSS_SELECTOR, '#register_form')


class Basket():
    # Цена товара на страницеж
    PRICE = (By.CLASS_NAME, 'price_color')
    BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_ADD_TO_BASKET = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade in')
