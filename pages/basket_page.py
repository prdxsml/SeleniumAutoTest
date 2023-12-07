from .base_page import BasePage
from .locators import BasketPageLocator
from .locators import MainPageLocators



class BasketPage(BasePage):

    # Проверим существование кнопки с переходом в корзину
    def guest_basket_button_exists(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_BUTTON), 'Кнопки перехода в корзину не обнаружено'
        basket_button = self.is_element_present(*BasketPageLocator.BASKET_BUTTON)
        basket_button.click()
    
    # Клик на кнопке Корзина
    def guest_click_basket_button(self):
        basket_button = self.is_element_present(*BasketPageLocator.BASKET_BUTTON)
        basket_button.click()
    
    # Проверка сопоставление текста на странице Корзина. Убедимся, что Корзина пуста.
    # def guest_basket_clear(self):
    #     guest_should_see = self.is_element_present(*BasketPageLocator.TITLE_BASKET_CLEAR)
    #     assert 'Ваша корзина пуста' in guest_should_see.text, 'Ошибка. Корзина не пуста'
    #     print('В корзине нет товаров')

    # Проверка для 1 теста в main_page
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        guest_basket_button = self.is_element_present(*MainPageLocators.GUEST_BASKET_BUTTON)
        guest_basket_button.click()


    # Проверка наличия кнопки
    def button_basket(self):
        assert self.is_element_present(*MainPageLocators.GUEST_BASKET_BUTTON), "Кнопки нет"
    
    # Переход по ссылке из кнопки
    def button_basket_click(self):
        """
        При успользовании метода browser.find_element - элемент находит и отрабатывает,
        а при использовании метода is_element_present - нет.
        """
        link = self.browser.find_element(*MainPageLocators.GUEST_BASKET_BUTTON)
        link.click()

    def check_is_basket_clear(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_ITEM_WRAPPER), "Элемент есть,"

    def text_is_basket_clear(self):
        assert self.browser.find_element(*BasketPageLocator.TEXT_IN_BASKET), "Нет"