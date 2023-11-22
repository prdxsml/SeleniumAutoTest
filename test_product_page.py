from pages.main_page import MainPage
from pages.product_page import ProductPage
import time



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.button()

def test_click_on_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button()
    time.sleep(10)
    page.item_on_basket()
    page.correct_title_on_message()
    page.correct_price_on_basket()

# Тест перехода по линке на странице. Переход между страницами. Тут мы и опишем проверки на правильность корзины.
def test_basket_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.basket_link()
    basket_page = ProductPage(browser, browser.current_url)
    basket_page.should_be_basket_url()



    # ? Дописать проверку цены
    # ? Дописать проверку названия товара


