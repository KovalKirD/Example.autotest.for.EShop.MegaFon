# Базовая Страница
class BasePage:
    def __init__(self, browser, url, timeout=10):  # конструктор класса
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # ожидать элемент в течении _сек.

    def open(self):  # открыть старницу
        self.browser.get(self.url)