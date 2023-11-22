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

    def basket_all_price(self):
        assert self.is_element_present(*Basket.BASKET_ITEM_PRICE), 'Элемент корзиночной цены проебан'
        assert self.is_element_present(*Basket.ITEM_PRICE), 'Элемент цены товара проебан'

        basket_item_price_el = self.browser.find_element(*Basket.BASKET_ITEM_PRICE)
        item_price_el = self.browser.find_element(*Basket.ITEM_PRICE)
        basket_item_price = basket_item_price_el.text
        item_price = item_price_el.text

        assert basket_item_price == item_price, 'Ошибка нахуй'

    def what_in_title_and_price(self):
        #? Функция показывает что лежит в заголовке / Работает
        # x = self.browser.find_element(*Basket.TITLE_TOVARA)
        # x_text = x.text
        # print('x_text', x_text)

        #? Функция показывает что лежит в цене / Работает
        # y = self.browser.find_element(*Basket.PRICE_ADD_TO_BASKET)
        # y_text = y.text
        # print('y_text', y_text)

        # Функция поиска тайтла в бредкрамбах / Работает / Не используем
        # z = self.browser.find_element(*Basket.BREADCRAMB_TITLE)
        # z_text = z.text
        # print('z_text', z_text)

        #? Функция показывает, что лежит в месаге о добавлении товара / Работает
        m = self.browser.find_element(*Basket.ITEM_ADD_TO_BASKE_NEW)
        m_text = m.text
        print('m_text', m_text)

    def title_equally_title_on_message(self):
        # 1. Основной тайтл для сравнения
        x = self.browser.find_element(*Basket.TITLE_TOVARA)
        x_text = x.text
        print('===x_text===', x_text)
        # 2. Тайтл из всплывающего сообщения, после добавления в корзину
        m = self.browser.find_element(*Basket.ITEM_ADD_TO_BASKE_NEW)
        m_text = m.text
        print('===m_text===', m_text)
        # 3. Функция проверки двух тайтлов
        assert x_text == m_text, "Не совпадают"
        print ('Совпадают', x_text == m_text)