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
    DELIVERY_METHOD_PICKUP = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(2) > div > :nth-child(2)')
    BUTTON_SELECT_ADDRESS_STORE = (By.CSS_SELECTOR, '.StoreLocatorAddress-module__storeLocatorAddress--hhyuB  button')
    LIST_STORES = (By.CSS_SELECTOR, '.Tabs-module__tabs--jbcOV > div:nth-child(2)')
    BUTTON_SELECT_PVZ = (By.CSS_SELECTOR, '.mf-offices-panel__pickups-list > a :nth-child(3) > .mf-offices-panel__item-select')
    # СПОСОБ ОПЛАТЫ
    PAYMENT_METHOD_CASH = (By.CSS_SELECTOR, '.Checkout-module__main--a-NUG > div:nth-child(2) > div > div:nth-child(6) > .OptionsWrapper-module__options--I4ac4 > div:nth-child(2)')
    # ОФОРМИТЬ ЗАКАЗ
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, '.FixedSummary-module__main--uwywf button')
    INPUT_CONFIRM_SMS_CODE = (By.CSS_SELECTOR, '.ConfirmSmsCode-module__confirmSmsCode--2klTl input')