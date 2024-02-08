# Конфигурация Тестов
import pytest                   # пакет pytest
from selenium import webdriver  # пакет Вебдрайвер

# фикстура запуска/закрытия браузера
@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()  # инициализируем драйвер браузера
    print('\nbrowser start for test')
    yield browser                 # финализатор
    print('\nbrowser quit')
    browser.quit()                # закрыть браузер