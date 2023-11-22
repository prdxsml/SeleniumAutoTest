from selenium.webdriver.common.by import By
from selenium import webdriver

# ! Страница локаторов. Опеределяем переменные и переиспользуем в проекте.


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    # Линка логина
    URL_LINK = 'login'
    
    # Чекаем существование формы логина, именно формы, а не полей
    # Сначала пишем красные тесты, чтобы проверки падали, затем проверяем зелеными тестами
    FORM_AUTH_CHECK = (By.CSS_SELECTOR, '#login_form')
    
    # Чекаем существование формы регистрации, именно формы, а не полей
    FORM_REG_CHECK = (By.CSS_SELECTOR, '#register_form')


class Basket():
    
    # Цена товара на страницеж
    PRICE = (By.CLASS_NAME, 'price_color')
    
    # Кнопка
    BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    
    # Сообщение о добавлении товара с тайтлов
    ITEM_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    
    # Тайтл названия товара
    TITLE_ITEM = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > ul > li.active')
    
    # Цена товара в сообщении
    PRICE_ON_BASKET = (By.CLASS_NAME, 'col-sm-3.price_color.align-right')
    
    # Цена товара на странице товара
    MAIN_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    
    # Линк на страницу с корзиной
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')