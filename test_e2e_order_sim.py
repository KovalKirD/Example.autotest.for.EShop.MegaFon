# Текст-кейс: e2e покупка МегаТарифа(MT)(ПВЗ, Нал.Расч)
# Проверка: отображение поля ввода sms кода подтверждения заказа
import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage

# URL бранча
links = ['https://moscow.shop.megafon.ru/']  # , 'https://spb.shop.megafon.ru/', 'https://krasnodar.shop.megafon.ru/'

@pytest.mark.parametrize('link', links)
def test_order(browser, link):
    page = MainPage(browser, link)  # создать объект страницы
    page.open()                     # открыть старницу
    page.select_tarif_on_main()     # выбрать тариф на главной
    page = BasketPage(browser, '')  # создать объект страницы
    page.basket_order_sim()         # оформить заказ
# Пустая строка