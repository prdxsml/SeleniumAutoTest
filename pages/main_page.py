from .base_page import BasePage
from .locators import MainPageLocators

from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # Хорошая практика сначала делать тест красным, а потом зеленым. Ниже селектор
        # намеренно сделан неправильно
        # Символ * - указывает на то, что мы передали именно пару и этот кортеж надо распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_auth_login_input(self):
        assert self.is_element_present(*MainPageLocators.EMAIL_AUTH_INPUT), 'EMAIL_AUTH_INPUT ..... OK'
    def should_be_auth_email_input(self):
        assert self.is_element_present(*MainPageLocators.PASSWORD_AUTH_INPUT), 'PASSWORD_AUTH_INPUT ..... OK'
    def should_be_reg_email_input(self):
        assert self.is_element_present(*MainPageLocators.EMAIL_REGISTRATION_INPUT), 'EMAIL_REGISTRATION_INPUT ..... OK'
    def should_be_reg_pass_input(self):
        assert self.is_element_present(*MainPageLocators.PASSWORD_REGISTRATION_INPUT), 'PASSWORD_REGISTRATION_INPUT ..... OK'
    def should_be_ref_pass_repeat_input(self):
        assert self.is_element_present(*MainPageLocators.PASSWORD_REGISTRATION_REPEAT_INPUT), 'PASSWORD_REGISTRATION_REPEAT_INPUT ..... OK'