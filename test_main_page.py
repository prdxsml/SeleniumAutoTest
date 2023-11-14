from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# def test_should_be_auth_login_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_auth_email_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_reg_email_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_reg_pass_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_should_be_ref_pass_repeat_input(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
