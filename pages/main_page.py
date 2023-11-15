from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from .locators import LoginPageLocators

from selenium.webdriver.common.by import By


class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #? Первый вариант переключения страниц
        # return LoginPage(browser=self, url=self.browser.current_url)
        #? Второй вариант переключения страниц 
        

    def should_be_login_link(self):
        # Хорошая практика сначала делать тест красным, а потом зеленым. Ниже селектор
        # намеренно сделан неправильно
        # Символ * - указывает на то, что мы передали именно пару и этот кортеж надо распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # find_login_link = self.browser.current_url()
        # find_login_link.click()


    def should_be_auth_login_input(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_AUTH_INPUT), 'EMAIL_AUTH_INPUT ..... NOT'
    def should_be_auth_email_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_AUTH_INPUT), 'PASSWORD_AUTH_INPUT ..... NOT'
    def should_be_reg_email_input(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_INPUT), 'EMAIL_REGISTRATION_INPUT ..... NOT'
    def should_be_reg_pass_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT), 'PASSWORD_REGISTRATION_INPUT ..... NOT'
    def should_be_ref_pass_repeat_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_REPEAT_INPUT), 'PASSWORD_REGISTRATION_REPEAT_INPUT ..... NOT'