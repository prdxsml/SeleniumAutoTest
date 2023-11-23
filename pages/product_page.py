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

    def title_equally_title_on_message(self):
        # 1. Основной тайтл для сравнения
        product_page_title = self.browser.find_element(*Basket.TITLE_TOVARA)
        product_page_title_text = product_page_title.text
        print('Тайтл на странице товара:', product_page_title_text)
        # 2. Тайтл из всплывающего сообщения, после добавления в корзину
        product_message_title = self.browser.find_element(*Basket.ITEM_ADD_TO_BASKE_NEW)
        product_message_title_text = product_message_title.text
        print('Тайтл на сообщении о добавлении в корзину:', product_message_title_text)
        # 3. Функция проверки двух тайтлов
        assert product_page_title_text == product_message_title_text, "Тайтлы на странице и в корзине: НЕ СОВПАДАЮТ"
        print ('Тайтлы на странице и в корзине: СОВПАДАЮТ', product_page_title_text == product_message_title_text)

    def price_equally_price_on_basket(self):
        # Цена на странице товара
        product_page_price = self.browser.find_element(*Basket.MAIN_PRICE)
        product_page_price_text = product_page_price.text
        print('Цена товара на странице продукта:', product_page_price_text)
        # Цена товара в корзине
        basket_page_price = self.browser.find_element(*Basket.BASKET_ON_PPP)
        basket_page_price_text = basket_page_price.text
        print('Цена товара в корзине:', basket_page_price_text)
        # Сравнение цен на странице товара и в корзине
        assert product_page_price_text in basket_page_price_text, 'Цена товара на странице продукта и корзине: НЕ СОВПАДАЮТ'
        if f'{product_page_price_text}' in basket_page_price_text:
            print('Цена товара на странице продукта и корзине: СОВПАДАЮТ')