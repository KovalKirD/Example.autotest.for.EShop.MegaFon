# Example.autotest.for.EShop.MegaFon
## Пример автотеста для Интернет-Магазина МегаФон
 
ЯП: **Python**  
Фреймворк: **Selenium WebDriver**  
Среда тестирования: **Pytest**  
Браузер: **Chrome/Firefox**

### Описание Теста:
**Цель:** Проверка возможности оформления и выбора/заполнения атрибутов заказа в корзине на подключение.  
**Тип:** Smoke, e2e  
**Ресурс:** https://shop.megafon.ru/  
**Товар:** Тариф "Мегафон 3.0. МегаТариф"  
**Бранч:** moscow, spb, krasnodar  
**Ожидаемый результат:** Кнопка "Оформить заказ" кликабельна  
**Колличество проверок:** 9шт.
#### Тест-Кейсы:
1. ПВЗ, Нал.Расч
2. Курьером, Нал.Расч
3. Экспересс-доставка, Нал.Расч

### Запуск в CLI:
#### Пердустановлено:
1. Python
2. Google Chrome / Mozila FireFox
3. chromdriver / geckodriver
   
Создать виртуальное окружение:
```
python -m venv test_venv
```
Активировать окружение:
```
source test_venv/bin/activate
```
Установить зависимости:
```
pip install -r requirements.txt
```
Выполнить тест:
```
pytest -v --tb=line --html=report.html --browser_name=chrome
```
