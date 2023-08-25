# Базовая Страница
from selenium.webdriver.support.expected_conditions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url, timeout=10):  # конструктор класса
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # ожидать элемент в течении _сек.

    def open(self):  # открыть старницу
        self.browser.get(self.url)

    def is_element_selected(self, how, what):  # элемент должен быть выбран
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True