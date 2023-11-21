from .base_page import BasePage
from .locators import Basket
import time
# from base_page import solve_quiz_and_get_code
# from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    
    def button(self):
        assert self.browser.find_element(*Basket.BUTTON), "Кнопка не найдена"
    
    def click_on_button(self):
        link = self.browser.find_element(*Basket.BUTTON)
        link.click()
        BasePage.solve_quiz_and_get_code(self)
        # у = BasePage.solve_quiz_and_get_code(self)
        # alert.send_keys(у)



        
    def item_on_basket(self):
        assert self.browser.find_element(*Basket.ITEM_ADD_TO_BASKET), "Такого элемента нет"
