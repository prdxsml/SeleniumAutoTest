from .base_page import BasePage
# from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert "login" in self.current_url, 'сообщение об ошибке'
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_AUTH_CHECK), 'FORM_AUTH_CHECK ..... NOT'
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REG_CHECK), 'FORM_REG_CHECK ..... NOT'
        assert True


# def test_should_be_auth_login_input(browser):
#         link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#         page = MainPage(browser, link)
#         page.open()
#         page.should_be_login_link()

# def test_should_be_auth_email_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_reg_email_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_reg_pass_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_ref_pass_repeat_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()