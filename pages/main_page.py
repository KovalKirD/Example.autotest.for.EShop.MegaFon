# Главная Страница
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def select_tarif_on_main(self):
        # ВЫБРАТЬ ТАРИФ И ДОБАВИТЬ В КОРЗИНУ
        by_MegaTarif = self.browser.find_element(By.CSS_SELECTOR,
                                                 '[aria-label="4 / 7"] .c-tariff-card-buy button')
        by_MegaTarif.click()  # Нажать кнопку "Купить" на тарифе

        by_SIM = self.browser.find_element(By.CSS_SELECTOR,
                                           '.c-tariff-buy-chooses :nth-child(1) .c-tariff-buy-choose-inner :nth-child(1)')
        by_SIM.click()  # Нажать кнопку "Купить SIM"