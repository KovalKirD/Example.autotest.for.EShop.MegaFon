# Базовая Страница
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def is_element_present(self, how, what):  # элемент присутвтует на странице
        try:
            WebDriverWait(self.browser, 7).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_element_clickable(self, how, what):  # элемент кликабельный
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))
        except NoSuchElementException:
            return False
        return True