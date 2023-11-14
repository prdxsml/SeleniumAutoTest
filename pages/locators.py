from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    FORM_AUTH_CHECK = (By.CSS_SELECTOR, '#login_form')
    EMAIL_AUTH_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_AUTH_INPUT = (By.CSS_SELECTOR, '#id_login-password')
    FORM_REG_CHECK = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REGISTRATION_REPEAT_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')