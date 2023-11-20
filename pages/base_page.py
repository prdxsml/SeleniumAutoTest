from selenium.common.exceptions import NoSuchElementException

# ! Базовая страница от которой наследуются все остальные классы.
# ! Описываются вспомогательные методы для работы с драйвером

class BasePage():
    # Добавляем метод-конструтор. Передаем в него экземпляр драйвера и url-адрес
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True