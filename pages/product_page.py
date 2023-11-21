from .base_page import BasePage
from .locators import Basket
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_button(self):
        assert self.browser.find_element(*Basket.BUTTON), "Кнопка не найдена"
    
    def click_on_button(self):
        press = self.browser.find_element(*Basket.BUTTON)
        press.click()