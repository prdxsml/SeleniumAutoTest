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
    
    # Тайтл названия товара. Берется из хлебных
    TITLE_ITEM = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > ul > li.active')
    
    # Цена товара в сообщении / В текущей реализации проверяется только его существование
    PRICE_ON_BASKET = (By.CLASS_NAME, 'col-sm-3.price_color.align-right')
    
    #! Цена товара на странице товара / В текущей реализации проверяется только его существование
    MAIN_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    
    # Линк на страницу с корзиной
    # BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    # BASKET_ITEM_PRICE = (By.CLASS_NAME, 'total.align-right')
    # ITEM_PRICE = (By.CLASS_NAME, 'price_color.align-right')
    
    #! Цена товара в корзине
    BASKET_PRICE_ITEM = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[4]/p')

    #! Определяем элемент, откуда будем брать заголовки для всех товаров. Основной тайтл h1 на странице товара
    TITLE_TOVARA = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')

    #! Определяем элемент во всплывающем элементе о стоимости корзины
    PRICE_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')

    # Элемент из бредкрамбов с которым будем соотносить основной тайтл страницы
    BREADCRAMB_TITLE = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > ul > li.active')

    #! Сообщение о добавлении товара с тайтлом
    ITEM_ADD_TO_BASKE_NEW = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')

    # Цена корзины на продуктовой странице в сообщении
    BASKET_ON_PPP = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs')