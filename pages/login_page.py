from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

# ! Реализация методов проверок для страницы LoginPage. 
# ! 

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

    # етод проверки наличия формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REG_CHECK), 'FORM_REG_CHECK ..... NOT FIND'
        # assert True - просто заглушка.
