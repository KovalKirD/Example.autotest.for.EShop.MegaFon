# Страница Корзины
from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    # КОРЗИНА: ОФОРМЛЕНИЕ ЗАКАЗА
    def basket_order_sim(self):
        # ПОЛУЧАТЕЛЬ
        insert_FIO = self.browser.find_element(By.NAME, 'fullName')
        insert_FIO.send_keys('Тест Тест Тест')  # Заполнить ФИО

        insert_PHONE = self.browser.find_element(By.NAME, 'smsPhoneNumber')
        insert_PHONE.send_keys('1111111111')  # Заполнить Номер телефона

        insert_EMAIL = self.browser.find_element(By.NAME, 'email')
        insert_EMAIL.send_keys('test@test.ru')  # Заполнить Адресс Эл.Почты

        # СПОСОБ ПОЛУЧЕНИЯ
        select_PICUP = self.browser.find_element(By.CSS_SELECTOR,
                                            '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(2)')
        select_PICUP.click()  # Выбрать Способ Получения: Самовывоз

        select_SSM = self.browser.find_element(By.CSS_SELECTOR,
                                          '.StoreLocatorAddress-module__storeLocatorAddress--hhyuB  button')
        select_SSM.click()  # Нажать кнопку "Выбрать адрес самовывоза"

        select_LIST_SSM = self.browser.find_element(By.CSS_SELECTOR, '.Tabs-module__tabs--jbcOV > div:nth-child(2)')
        select_LIST_SSM.click()  # Нажать кнопку "Списком"

        select_PVZ = self.browser.find_element(By.CSS_SELECTOR, '.mf-offices-panel__pickups-list > a :nth-child(3) > .mf-offices-panel__item-select')
        select_PVZ.click()  # Выбрать ПВЗ

        # СПОСОБ ОПЛАТЫ
        select_NAL = self.browser.find_element(By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(2)')
        select_NAL.click()  # Нажать "Оплата при получении"

        # ОФОРМИТЬ ЗАКАЗ
        select_BY = self.browser.find_element(By.CSS_SELECTOR, '.FixedSummary-module__main--uwywf button')
        select_BY.click()  # Нажать "Оформить заказ"

        # Проверка доступности поля ввода SMS подтверждения заказа
        select_SMS = self.browser.find_element(By.CSS_SELECTOR, '.ConfirmSmsCode-module__confirmSmsCode--2klTl input')
        assert select_SMS is not None, \
            'Ошибка: Элемент "select_SMS" не найден, проверьте поле ввода SMS подтверждения заказа'