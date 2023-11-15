from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    #? Чекаем существование формы логина, именно формы, а не полей
    # ? Сначала пишем красные тесты, чтобы проверки падали, затем проверяем зелеными тестами
    FORM_AUTH_CHECK = (By.CSS_SELECTOR, '#login_form')
    # EMAIL_AUTH_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    # PASSWORD_AUTH_INPUT = (By.CSS_SELECTOR, '#id_login-password')
    #? Чекаем существование формы регистрации, именно формы, а не полей
    FORM_REG_CHECK = (By.CSS_SELECTOR, '#register_form')
    # EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    # PASSWORD_REGISTRATION_INPUT = (By.CSS_SELECTOR, '#id_registration-password')
    # PASSWORD_REGISTRATION_REPEAT_INPUT = (By.CSS_SELECTOR, '#id_registration-password')