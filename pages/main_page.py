# Главная Страница
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def click_button_buy_megatarif(self):  # Нажать кнопку "Купить" на МегаТариф
        button_buy_megatarif = self.browser.find_element(*MainPageLocators.BUTTON_BUY_MEGATARIF)
        button_buy_megatarif.click()

    def click_button_buy_sim(self):  # Нажать кнопку "Купить SIM"
        button_buy_sim = self.browser.find_element(*MainPageLocators.BUTTON_BUY_SIM_OR_ESIM)
        button_buy_sim.click()