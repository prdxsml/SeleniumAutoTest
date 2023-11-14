from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортируем класс из каталога - "/pages/main_page.py"
from .pages.main_page import MainPage


#? pytest -v --tb=line --language=en test_main_page.py

def go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем PageObject, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    
# Вынесли проверку на логин в отдельную функцию
# Эта функция не пойдет в проверку тестов, т.к. не начинается с test_
# def go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     # Если верстка изменится, то заменить селектор потребуется только в одном месте
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

# Основная функция в которую передаем другие функции. Она исполнится, т.к.
# начинается с test_
# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     go_to_login_page(browser)
