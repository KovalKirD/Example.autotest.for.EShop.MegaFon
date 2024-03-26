# Example.autotest.for.EShop.MegaFon
## Пример автотеста для Интернет-Магазина МегаФон

Ресурс: https://moscow.shop.megafon.ru/  
ЯП: **Python**  
Фреймворк: **Selenium WebDriver**  
Среда тестирования: **Pytest**  
Тип теста: **Smoke**

### Запуск:
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
