# Локаторы
from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_BUY_MEGATARIF = (By.CSS_SELECTOR, '[aria-label="4 / 7"] .c-tariff-card-buy button')
    BUTTON_BUY_SIM_OR_ESIM = (By.CSS_SELECTOR, '.c-tariff-buy-chooses :nth-child(1) .c-tariff-buy-choose-inner :nth-child(1)')

class BasketPageLocators:
    # ПОЛУЧАТЕЛЬ
    INPUT_FIO = (By.NAME, 'fullName')
    INPUT_PHONE = (By.NAME, 'smsPhoneNumber')
    INPUT_EMAIL = (By.NAME, 'email')
    # СПОСОБ ПОЛУЧЕНИЯ
    GET_METHOD_PICKUP = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(2)')
    GET_METHOD_DELIVERY = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(1)')
    GET_METHOD_DELIVERY_SELECTED = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(1).Option-module__selected--YFDSZ')
    # АДРЕС
    BUTTON_SELECT_ADDRESS_STORE = (By.CSS_SELECTOR, '.StoreLocatorAddress-module__storeLocatorAddress--hhyuB  button')
    BUTTON_SELECT_ADDRESS_DELIVERY = (By.CSS_SELECTOR, '.AddressesCheckout-module__addressesCheckout--xlmQ9 button')
    LIST_STORES = (By.CSS_SELECTOR, '.Tabs-module__tabs--jbcOV > div:nth-child(2)')
    BUTTON_SELECT_PVZ = (By.CSS_SELECTOR, '.mf-offices-panel__pickups-list > a :nth-child(3) > .mf-offices-panel__item-select')
    INPUT_ADDRESS_DELIVERY = (By.CSS_SELECTOR, '.Select-module__select--W-iMl input')
    BUTTON_SAVE_ADDRESS_DELIVERY = (By.CSS_SELECTOR, 'button.ChangeAddress-module__button--FcrvC')
    # ТИП ДОСТАВКИ
    TYPE_DELIVERY_COURIER = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(1)')
    TYPE_DELIVERY_EXPRESS = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(2)')
    # ДАТА И ВРЕМЯ ДОСТАВКИ
    SPAN_DATE_DELIVERY = (By.CSS_SELECTOR, '.DeliverySlotsWrapper-module__list--zwv0l > div:nth-child(1) span')
    # СПОСОБ ОПЛАТЫ
    PAYMENT_METHOD_CASH = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(2)')
    PAYMENT_METHOD_CASH_FOR_GET_METHOD_DELIVERY = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(8) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(1)')
    # ОФОРМИТЬ ЗАКАЗ
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, '.FixedSummary-module__main--uwywf button')
    INPUT_CONFIRM_SMS_CODE = (By.CSS_SELECTOR, '.ConfirmSmsCode-module__confirmSmsCode--2klTl input')