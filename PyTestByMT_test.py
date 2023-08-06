# Pytest: Оформление заказа на подключение МегаТариф
import pytest                                    # Пакет pytest
import time                                      # Модуль Время
from selenium import webdriver                   # Пакет Вебдрайвер
from selenium.webdriver.common.by import By      # Класс: "Поиск элементов"

# URL бранча
link = ['https://moscow.shop.megafon.ru/', 'https://spb.shop.megafon.ru/']

# фикстура запуска и закрытия браузера
@pytest.fixture()
def browser():
    browser = webdriver.Chrome()  # инициализируем драйвер браузера
    browser.implicitly_wait(10)   # ждать 10 сек. до поиска элемента
    yield browser                 # финализатор
    browser.quit()                # закрыть браузер

# Текст-кейс: e2e покупка МегаТарифа(MT)(ПВЗ, Нал.Расч)
# Проверка: отображение поля ввода sms кода подтверждения заказа
def case(browser):
    # Закрыть попап
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, 'div.popmechanic-main .popmechanic-close').click()

    # ВЫБРАТЬ ТАРИФ И ДОБАВИТЬ В КОРЗИНУ
    by_MegaTarif = browser.find_element(By.CSS_SELECTOR, '[aria-label="4 / 7"] .c-tariff-card-buy button')
    by_MegaTarif.click()  # Нажать кнопку "Купить" на тарифе

    by_SIM = browser.find_element(By.CSS_SELECTOR, '.c-tariff-buy-chooses :nth-child(1) .c-tariff-buy-choose-inner :nth-child(1)')
    by_SIM.click()  # Нажать кнопку "Купить SIM"

    # ОФОРМЛЕНИЕ ЗАКАЗА
    # ПОЛУЧАТЕЛЬ
    insert_FIO = browser.find_element(By.NAME, 'fullName')
    insert_FIO.send_keys('Тест Тест Тест')  # Заполнить ФИО

    insert_PHONE = browser.find_element(By.NAME, 'smsPhoneNumber')
    insert_PHONE.send_keys('1111111111')  # Заполнить Номер телефона

    insert_EMAIL = browser.find_element(By.NAME, 'email')
    insert_EMAIL.send_keys('test@test.ru')  # Заполнить Адресс Эл.Почты

    # СПОСОБ ПОЛУЧЕНИЯ
    select_PICUP = browser.find_element(By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(2)')
    select_PICUP.click()  # Выбрать Способ Получения: Самовывоз

    select_SSM = browser.find_element(By.CSS_SELECTOR, '.StoreLocatorAddress-module__storeLocatorAddress--hhyuB  button')
    select_SSM.click()  # Нажать кнопку "Выбрать адрес самовывоза"

    time.sleep(3)  # Загрузка карты
    select_LIST_SSM = browser.find_element(By.CSS_SELECTOR, '.Tabs-module__tabs--jbcOV > div:nth-child(2)')
    select_LIST_SSM.click()  # Нажать кнопку "Списком"

    select_PVZ = browser.find_element(By.CSS_SELECTOR, '.mf-offices-panel__pickups-list > a :nth-child(3) > .mf-offices-panel__item-select')
    select_PVZ.click()  # Выбрать ПВЗ

    # СПОСОБ ОПЛАТЫ
    select_NAL = browser.find_element(By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(2)')
    select_NAL.click()  # Нажать "Оплата при получении"

    # ОФОРМИТЬ ЗАКАЗ
    select_BY = browser.find_element(By.CSS_SELECTOR, '.FixedSummary-module__main--uwywf button')
    select_BY.click()  # Нажать "Оформить заказ"

    # Проверка доступности поля ввода SMS подтверждения заказа
    select_SMS = browser.find_element(By.CSS_SELECTOR, '.ConfirmSmsCode-module__confirmSmsCode--2klTl input')
    assert (select_SMS is not None, 'Тест не пройден, элемент "select_SMS" не найден, проверьте поле ввода SMS подтверждения заказа')

# Запуск тестов
class TestCaseByMT:
    # для МСК
    def test_MSK(self, browser):
        browser.get(link[0])  # открыть страницу
        case(browser)         # запустить тест-кейс
    # для СПБ
    def test_SPB(self, browser):
        browser.get(link[1])  # открыть страницу
        case(browser)         # запустить тест-кейс
# Пустая строка