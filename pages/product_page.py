from .base_page import BasePage
from .locators import Basket
import time


class ProductPage(BasePage):

    # Проверка наличия кнопки
    def button(self):
        assert self.browser.find_element(*Basket.BUTTON), "Кнопка не найдена"

    # Проверка кликабельности кнопки и автоподстановка уровнения
    def click_on_button(self):
        link = self.browser.find_element(*Basket.BUTTON)
        link.click()
        BasePage.solve_quiz_and_get_code(self)

    # Проверка поиска элемента с названием(тайтлом)
    def item_on_basket(self):
        assert self.browser.find_element(*Basket.ITEM_ADD_TO_BASKET), "Такого элемента нет"

    # Проверка что мы добавили в корзину верный элемент
    def correct_title_on_message(self):
        message = self.browser.find_element(*Basket.TITLE_ITEM)
        assert 'The shellcoder\'s handbook' in message.text, 'Тайтл не совпадает'

    # Проверка корректного селектора для стоимости корзины
    def correct_price_on_basket(self):
        assert self.browser.find_element(*Basket.PRICE_ON_BASKET), 'PRICE_ON_BASKET - Такого элемента нет'
        assert self.browser.find_element(*Basket.MAIN_PRICE), 'MAIN_PRICE - нетути, ищи дальше'

    def basket_link(self):
        link = self.browser.find_element(*Basket.BASKET_LINK)
        link.click()

    # Метод проверки урла на содержание нужного слова в адресе
    def should_be_basket_url(self):
        assert "basket" in self.url, 'сообщение об ошибке'

