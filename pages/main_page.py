from .base_page import BasePage

# ! Страница для определения классов. Классы наследюуюся от BasePage.

class MainPage(BasePage):
    def __init__(self, *args, **kwards):
        super(MainPage, self).__init__(*args, **kwards)