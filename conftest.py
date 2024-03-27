# Конфигурация Тестов
import pytest                   # пакет pytest
from selenium import webdriver  # пакет Вебдрайвер
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):  # обработчик опции
    parser.addoption('--browser_name', action='store', default='firefox',
                     help='Choose browser: chrome or firefox')  # выбор браузера
    parser.addoption('--ui', action='store', default='', help='Choose: headless or none')  # запуск браузера без UI

# фикстура запуска/закрытия браузера
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")  #запрос опции в cli
    browser = None
    ui = request.config.getoption("ui")
    option = Options()
    if ui == "headless":
        option.add_argument('--headless')
    if browser_name == "chrome":  # инициализируем драйвер браузера
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=option)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser                 # финализатор
    print('\nbrowser quit')
    browser.quit()                # закрыть браузер