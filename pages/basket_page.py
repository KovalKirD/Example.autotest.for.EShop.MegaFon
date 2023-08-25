# Страница Корзины
import time
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
  # ПОЛУЧАТЕЛЬ
    def insert_fio_in_input(self):  # Заполнить ФИО
        input_fio = self.browser.find_element(*BasketPageLocators.INPUT_FIO)
        input_fio.send_keys('Тест Тест Тест')

    def insert_phone_in_input(self):  # Заполнить Номер телефона
        input_phone = self.browser.find_element(*BasketPageLocators.INPUT_PHONE)
        input_phone.send_keys('1111111111')

    def insert_email_in_input(self):  # Заполнить Адресс Эл.Почты
        input_email = self.browser.find_element(*BasketPageLocators.INPUT_EMAIL)
        input_email.send_keys('test@test.ru')

  # СПОСОБ ПОЛУЧЕНИЯ
    def select_delivery_pickup_method(self):  # Выбрать Способ Получения: Самовывоз
        pickup_delivery = self.browser.find_element(*BasketPageLocators.GET_METHOD_PICKUP)
        pickup_delivery.click()

  # АДРЕС
    def click_button_select_address_store(self):  # Нажать кнопку "Выбрать адрес самовывоза"
        button_select_address_store = self.browser.find_element(*BasketPageLocators.BUTTON_SELECT_ADDRESS_STORE)
        button_select_address_store.click()

    def click_button_select_address_delivery(self): # Нажать кнопку "Добавить адрес доставки"
        button_select_address_delivery = self.browser.find_element(*BasketPageLocators.BUTTON_SELECT_ADDRESS_DELIVERY)
        button_select_address_delivery.click()

    def select_list_stores(self):  # Выбрать: "Списком"
        time.sleep(3)  # на загрузку карты
        list_stores = self.browser.find_element(*BasketPageLocators.LIST_STORES)
        list_stores.click()

    def click_button_select_pvz_in_list_store(self):  # Нажать кнопу "Выбрать" ПВЗ
        button_select_pvz = self.browser.find_element(*BasketPageLocators.BUTTON_SELECT_PVZ)
        button_select_pvz.click()

    def should_be_selected_delivery_ship_method(self):  # проверка: выбран способ получения "Доставка"
        assert self.is_element_selected(*BasketPageLocators.GET_METHOD_DELIVERY_SELECTED), \
            'Ошибка: Способ получения "Доставка" не выбран'

  # СПОСОБ ОПЛАТЫ
    def select_cash_payment_method(self):  # выбрать "Оплата при получении"
        payment_cash = self.browser.find_element(*BasketPageLocators.PAYMENT_METHOD_CASH)
        payment_cash.click()

  # ОФОРМИТЬ ЗАКАЗ
    def click_checkout_button(self):  # нажать кнопку "Оформить заказ"
        checkout_button = self.browser.find_element(*BasketPageLocators.BUTTON_CHECKOUT)
        checkout_button.click()

    def should_be_input_confirm_sms_code(self):  # Проверка доступности поля ввода SMS подтверждения заказа
        input_confirm_sms_code = self.browser.find_element(*BasketPageLocators.INPUT_CONFIRM_SMS_CODE)
        assert input_confirm_sms_code is not None, \
            'Ошибка: Элемент "input_confirm_sms_code" не найден, проверьте поле ввода SMS подтверждения заказа'