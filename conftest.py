# Конфигурация Тестов
import pytest                   # пакет pytest
from selenium import webdriver  # пакет Вебдрайвер

def pytest_addoption(parser):  # обработчик опции
    parser.addoption('--browser_name', action='store', default='firefox',
                     help='Choose browser: chrome or firefox')

# фикстура запуска/закрытия браузера
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")  #запрос опции в cli
    browser = None
    if browser_name == "chrome":  # инициализируем драйвер браузера
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser                 # финализатор
    print('\nbrowser quit')
    browser.quit()                # закрыть браузер