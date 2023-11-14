from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        # Хорошая практика сначала делать тест красным, а потом зеленым. Ниже селектор
        # намеренно сделан неправильно
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"