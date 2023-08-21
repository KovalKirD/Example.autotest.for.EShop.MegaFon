# Конфигурация Тестов
import pytest                   # пакет pytest
from selenium import webdriver  # пакет Вебдрайвер

# фикстура запуска/закрытия браузера
@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()  # инициализируем драйвер браузера
    browser.implicitly_wait(10)   # ждать 10 сек. до поиска элемента
    yield browser                 # финализатор
    browser.quit()                # закрыть браузер