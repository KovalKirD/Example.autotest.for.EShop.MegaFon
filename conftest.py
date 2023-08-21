# Конфигурация Тестов
import pytest                   # пакет pytest
from selenium import webdriver  # пакет Вебдрайвер

# фикстура запуска/закрытия браузера
@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()  # инициализируем драйвер браузера
    yield browser                 # финализатор
    browser.quit()                # закрыть браузер