# Локаторы
from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_BUY_MEGATARIF = (By.CSS_SELECTOR, '[aria-label="4 / 7"] .c-tariff-card-buy button')
    BUTTON_BUY_SIM_OR_ESIM = (By.CSS_SELECTOR, '.c-tariff-buy-chooses :nth-child(1) .c-tariff-buy-choose-inner :nth-child(1)')