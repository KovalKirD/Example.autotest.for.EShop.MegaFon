import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage

# URL бранча
links = ['https://moscow.shop.megafon.ru/']  # , 'https://spb.shop.megafon.ru/', 'https://krasnodar.shop.megafon.ru/'

# Текст-кейс: e2e покупка МегаТарифа(MT)(ПВЗ, Нал.Расч)
# Проверка: отображение поля ввода sms кода подтверждения заказа
@pytest.mark.parametrize('link', links)
def test_order(browser, link):
    page = MainPage(browser, link)     # создать объект главной страницы
    page.open()                        # открыть главную старницу
    page.click_button_buy_megatarif()  # нажать кнопку "Купить" на МегаТариф
    page.click_button_buy_sim()        # нажать кнопку "Купить SIM"
    page = BasketPage(browser, '')     # создать объект страницы корзины
    page.insert_fio_in_input()
    page.insert_email_in_input()
    page.insert_phone_in_input()
    page.select_delivery_pickup_method()
    page.click_button_select_address_store()
    page.select_list_stores()
    page.click_button_select_pvz_in_list_store()
    page.select_cash_payment_method()
    page.click_checkout_button()
    page.should_be_input_confirm_sms_code()
# Пустая строка