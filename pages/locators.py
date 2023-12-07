from selenium.webdriver.common.by import By

# Страница локаторов. Опеределяем переменные и переиспользуем в проекте.

# Класс локаторов для основной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


# Класс локаторов для страницы логина
class LoginPageLocators():
    # Линк логина
    URL_LINK = 'login'
    # Чекаем существование формы логина, именно формы, а не полей
    # Сначала пишем красные тесты, чтобы проверки падали, затем проверяем зелеными тестами
    FORM_AUTH_CHECK = (By.CSS_SELECTOR, '#login_form')
    # Чекаем существование формы регистрации, именно формы, а не полей
    FORM_REG_CHECK = (By.CSS_SELECTOR, '#register_form')


class BasketPageLocators():
    # Кнопка "Добавить в корзину"
    ADD_BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    # Цена товара на странице товара / В текущей реализации проверяется только его существование
    MAIN_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    # Определяем элемент, откуда будем брать заголовки для всех товаров. Основной тайтл h1 на странице товара
    TITLE_TOVARA = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    # Сообщение о добавлении товара с тайтлом
    ITEM_ADD_TO_BASKE_NEW = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    # Цена корзины на продуктовой странице в сообщении
    BASKET_ON_PPP = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs')
    POP_UP_TITLE = (By.XPATH, '//*[@id="messages"]/div[12]')


# Локаторы для проверок логина, регистрации, поломанной линки
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    # Для отслеживания правильной работы. Сломанный линк
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_bad')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    # Локаторы для регистрации
    EMAIL_INPUT = (By.ID,'id_registration-email')
    PASS_INPUT = (By.ID, 'id_registration-password1')
    PASS_INPUT_REPEAT = (By.ID, 'id_registration-password2')
    REG_BTN = (By.NAME, 'registration_submit')


class NetativeLocators():
    NEGGATIVE_TEST_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE=(By.CSS_SELECTOR,".alert-success")


class BasketPageLocator():
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    BASKET_BUTTON = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    TITLE_BASKET_CLEAR = (By.CSS_SELECTOR, '#content_inner > p')