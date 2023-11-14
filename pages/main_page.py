# Из-за разницы в пакетах импорт может работать с точкой или без
from .base_page import BasePage
# Предка указали в скобках
class MainPage(BasePage):
    def go_to_login_page(self):
    # Если верстка изменится, то заменить селектор потребуется только в одном месте
    # Обращаемся к методу класса BasePage, где хранится browser
    login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()