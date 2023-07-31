# Оформление заказа на подключение МегаТариф
import time                                      # Модуль Время
from selenium import webdriver                   # Пакет Вебдрайвер
from selenium.webdriver.common.by import By      # Класс: "Поиск элементов"

try:
    driver = webdriver.Chrome()                      # инициализируем драйвер браузера
    driver.get('https://moscow.shop.megafon.ru/')    # открыть страницу
    driver.implicitly_wait(7)   # Ждать 7 сек. до поиска элемента
    # Закрыть попап
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, 'div.popmechanic-main .popmechanic-close').click()

    # ВЫБРАТЬ ТАРИФ И ДОБАВИТЬ В КОРЗИНУ
    by_MegaTarif = driver.find_element(By.CSS_SELECTOR, '[aria-label="4 / 7"] .c-tariff-card-buy button')
    by_MegaTarif.click()  # Нажать кнопку "Купить" на тарифе

    by_SIM = driver.find_element(By.CSS_SELECTOR, '.c-tariff-buy-chooses :nth-child(1) .c-tariff-buy-choose-inner :nth-child(1)')
    by_SIM.click()  # Нажать кнопку "Купить SIM"

    # ОФОРМЛЕНИЕ ЗАКАЗА
    # ПОЛУЧАТЕЛЬ
    insert_FIO = driver.find_element(By.NAME, 'fullName')
    insert_FIO.send_keys('Тест Тест Тест')  # Заполнить ФИО

    insert_PHONE = driver.find_element(By.NAME, 'smsPhoneNumber')
    insert_PHONE.send_keys('1111111111')  # Заполнить Номер телефона

    insert_EMAIL = driver.find_element(By.NAME, 'email')
    insert_EMAIL.send_keys('test@test.ru')  # Заполнить Адресс Эл.Почты

    # СПОСОБ ПОЛУЧЕНИЯ
    select_PICUP = driver.find_element(By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(2)')
    select_PICUP.click()  # Выбрать Способ Получения: Самовывоз

    select_SSM = driver.find_element(By.CSS_SELECTOR, '.StoreLocatorAddress-module__storeLocatorAddress--hhyuB  button')
    select_SSM.click()  # Нажать кнопку "Выбрать адрес самовывоза"

    time.sleep(3)
    select_LIST_SSM = driver.find_element(By.CSS_SELECTOR, '.Tabs-module__tabs--jbcOV > div:nth-child(2)')
    select_LIST_SSM.click()  # Нажать кнопку "Списком"

    select_PVZ = driver.find_element(By.CSS_SELECTOR, '.mf-offices-panel__pickups-list > a :nth-child(3) > .mf-offices-panel__item-select')
    select_PVZ.click()  # Выбрать ПВЗ

    # СПОСОБ ОПЛАТЫ
    select_NAL = driver.find_element(By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(2)')
    select_NAL.click()  # Нажать "Оплата при получении"

    # ОФОРМИТЬ ЗАКАЗ
    select_BY = driver.find_element(By.CSS_SELECTOR, '.FixedSummary-module__main--uwywf button')
    select_BY.click()  # Нажать "Оформить заказ"

finally:
    time.sleep(20)  # Задержка 20сек.
    driver.quit()  # Выход
    # Пустая строка