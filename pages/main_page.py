# Главная Страница
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def select_tarif_on_main(self):
        # ВЫБРАТЬ ТАРИФ И ДОБАВИТЬ В КОРЗИНУ
        button_buy_megatarif = self.browser.find_element(*MainPageLocators.BUTTON_BUY_MEGATARIF)
        button_buy_megatarif.click()  # Нажать кнопку "Купить" на тарифе

        button_buy_sim = self.browser.find_element(*MainPageLocators.BUTTON_BUY_SIM_OR_ESIM)
        button_buy_sim.click()  # Нажать кнопку "Купить SIM"