from os import link
from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import NetativeLocators

class ProductPage(BasePage):

    # Проверка наличия кнопки
    def button(self):
        assert self.browser.find_element(*BasketPageLocators.ADD_BASKET_BUTTON), "Кнопка не найдена"


    # Метод открытия страницы
    def open(self):
        self.browser.get(self.url)

    # Проверка кликабельности кнопки и автоподстановка уровнения
    def click_on_button(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_BASKET_BUTTON)
        link.click()
        BasePage.solve_quiz_and_get_code(self)


    def basket_link(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()


    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.POP_UP_TITLE), "Success message is presented, but should not be"
        assert "basket" in self.url, 'сообщение об ошибке'


    def title_equally_title_on_message(self):
        # 1. Основной тайтл для сравнения
        product_page_title = self.browser.find_element(*BasketPageLocators.TITLE_TOVARA)
        product_page_title_text = product_page_title.text
        print('Тайтл на странице товара:', product_page_title_text)
        # 2. Тайтл из всплывающего сообщения, после добавления в корзину
        product_message_title = self.browser.find_element(*BasketPageLocators.ITEM_ADD_TO_BASKE_NEW)
        product_message_title_text = product_message_title.text
        print('Тайтл на сообщении о добавлении в корзину:', product_message_title_text)
        # 3. Функция проверки двух тайтлов
        assert product_page_title_text == product_message_title_text, "Тайтлы на странице и в корзине: НЕ СОВПАДАЮТ"
        print ('Тайтлы на странице и в корзине: СОВПАДАЮТ', product_page_title_text == product_message_title_text)


    def price_equally_price_on_basket(self):
        # Цена на странице товара
        product_page_price = self.browser.find_element(*BasketPageLocators.MAIN_PRICE)
        product_page_price_text = product_page_price.text
        print('Цена товара на странице продукта:', product_page_price_text)
        # Цена товара в корзине
        basket_page_price = self.browser.find_element(*BasketPageLocators.BASKET_ON_PPP)
        basket_page_price_text = basket_page_price.text
        print('Цена товара в корзине:', basket_page_price_text)
        # Сравнение цен на странице товара и в корзине
        assert product_page_price_text in basket_page_price_text, 'Цена товара на странице продукта и корзине: НЕ СОВПАДАЮТ'
        if f'{product_page_price_text}' in basket_page_price_text:
            print('Цена товара на странице продукта и корзине: СОВПАДАЮТ')


    def user_cant_see_success_message_after_adding_product_to_basket(self):
        link = self.browser.find_element(*NetativeLocators.NEGGATIVE_TEST_BUTTON)
        link.click()
        assert self.is_element_present(*NetativeLocators.SUCCESS_MESSAGE), "Сообщение существует, это ошибка"


    def test_guest_cant_see_success_message(self):
        button = self.is_not_element_present(*NetativeLocators.NEGGATIVE_TEST_BUTTON)


    def test_message_disappeared_after_adding_product_to_basket(self):
        basket_button = self.is_element_present(*NetativeLocators.NEGGATIVE_TEST_BUTTON)
        basket_button.click()
        assert self.is_disappeared(*NetativeLocators.SUCCESS_MESSAGE), "Сообщение существует, это ошибка"