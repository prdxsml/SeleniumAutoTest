from os import link
from .base_page import BasePage
from .locators import BasketPageLocator
from .locators import MainPageLocators


class BasketPage(BasePage):

    # Проверка наличия кнопки
    def button_basket(self):
        assert self.is_element_present(*MainPageLocators.GUEST_BASKET_BUTTON), "Ошибка. Элемент должен отображаться"


    # Переход по ссылке из кнопки
    def button_basket_click(self):
        """
        При успользовании метода browser.find_element - элемент находит и отрабатывает,
        а при использовании метода is_element_present - нет.
        """
        link = self.browser.find_element(*MainPageLocators.GUEST_BASKET_BUTTON)
        link.click()


    # Проверка, что элемент корзины отсутствует
    def check_is_basket_clear(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_ITEM_WRAPPER), "Элемент есть, ошибка. Элемент не должен отображаться"


    # Проверка, что страница корзины содержит надпись
    def text_is_basket_clear(self):
        assert self.browser.find_element(*BasketPageLocator.TEXT_IN_BASKET), "Элемента нет, ошибка. Элемент должен отображаться"


    # Метод доавления в корзину товары
    def add_to_basket(self):
        link = self.browser.find_element(*BasketPageLocator.ADD_TO_BASKET)
        link.click()


    def check_is_basket_clear_negative(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_ITEM_WRAPPER), "Элемента нет, ошибка. Элемент должен отображаться"


    # Проверка, что страница корзины содержит надпись
    def text_is_basket_clear_negative(self):
        assert self.is_not_element_present(*BasketPageLocator.TEXT_IN_BASKET), "Элемента есть, ошибка. Элемент не должен отображаться"