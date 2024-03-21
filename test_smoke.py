import pytest
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

# Объект: Тариф "МегаФон 3.0. МегаТариф"
# Тип теста: Smoke, e2e
# Ожидаемый результат: Кнопка "Оформить заказ" кликабельна

# URL бранча
links = ['https://moscow.shop.megafon.ru/', 'https://spb.shop.megafon.ru/', 'https://krasnodar.shop.megafon.ru/']

#Тест-Кейс 1: ПВЗ, Нал.Расч
# @pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_order_sim_pickup_cash(browser, link):
    page = MainPage(browser, link)     # создать объект главной страницы
    page.open()
    page.click_button_buy_megatarif()
    page.click_button_buy_sim()
    page = BasketPage(browser, '')     # создать объект страницы корзины
    page.insert_fio_in_input()
    page.insert_email_in_input()
    page.insert_phone_in_input()
    page.select_delivery_pickup_method()
    page.click_button_select_address_store()
    page.select_list_stores()
    page.click_button_select_pvz_in_list_store()
    page.select_cash_payment_method()
    page.should_clickable_checkout_button()

# Тест-Кейс 2: Курьером, Нал.Расч
# @pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_order_sim_courier_cash(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.click_button_buy_megatarif()
    page.click_button_buy_sim()
    page = BasketPage(browser, '')
    page.insert_fio_in_input()
    page.insert_email_in_input()
    page.insert_phone_in_input()
    page.should_be_selected_delivery_ship_method()
    page.click_button_select_address_delivery()
    page.input_address_delivery()
    page.click_button_save_address_delivery()
    page.select_type_delivery_courier()
    page.should_be_span_date_delivery()
    page.select_cash_payment_method_for_get_method_delivery()
    page.should_clickable_checkout_button()

# Тест-Кейс 3: Экспересс-доставка, Нал.Расч
# @pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_order_sim_express_cash(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.click_button_buy_megatarif()
    page.click_button_buy_sim()
    page = BasketPage(browser, '')
    page.insert_fio_in_input()
    page.insert_email_in_input()
    page.insert_phone_in_input()
    page.should_be_selected_delivery_ship_method()
    page.click_button_select_address_delivery()
    page.input_address_delivery()
    page.click_button_save_address_delivery()
    page.select_type_delivery_express()
    page.select_cash_payment_method_for_get_method_delivery()
    page.should_clickable_checkout_button()