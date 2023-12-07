from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

# Реализация методов проверок для страницы LoginPage

# Класс для страницы LoginPage(наследуется от BasePage)
class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    # Метод проверки урла на содержание нужного слова в адресе
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert "login" in self.current_url, 'сообщение об ошибке'
        # assert self.is_element_present(*LoginPageLocators.FORM_AUTH_CHECK), "Login link is not presented"
        # assert True - просто заглушка
        assert "login" in self.url, 'сообщение об ошибке'
        # assert "login" in self.current_url(*LoginPageLocators.URL_LINK), "Login link is not presented"


    # Метод проверки наличия логин формы
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_AUTH_CHECK), 'FORM_AUTH_CHECK ..... NOT FIND'
        # assert True


    # Метод проверки наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REG_CHECK), 'FORM_REG_CHECK ..... NOT FIND'
        # assert True - просто заглушка.


    def register_new_user(self, email, password):
        # Находим инпут ввода почты
        email_input = self.browser.find_element(*BasePageLocators.EMAIL_INPUT)
        # Отправляем в инпут
        email_input.send_keys(email)
        # Находим поле ввода пароля
        password_input = self.browser.find_element(*BasePageLocators.PASS_INPUT)
        # Отправляем пароль в инпут
        password_input.send_keys(password)
        # Находим подтверждение пароля
        password_repeat = self.browser.find_element(*BasePageLocators.PASS_INPUT_REPEAT)
        # Повторяем ввод тестового пароля
        password_repeat.send_keys(password)
        # Находим кнопку регистрации пользователя
        registation_button = self.browser.find_element(*BasePageLocators.REG_BTN)
        registation_button.click()