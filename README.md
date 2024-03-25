# Example.autotest.for.EShop.MegaFon
## Пример автотеста для Интернет-Магазина МегаФон

Ресурс: https://moscow.shop.megafon.ru/  
Язык: **Python**  
Фреймворк: **Selenium WebDriver**  
Среда тестирования: **Pytest**  
Тип теста: **Smoke**

### Запуск:
Создать виртуальное окружение:
```
python venv test_venv
```
Установить зависимости:
```
pip install -r requirements.txt
```
Выполнить тест:
```
pytest -v --tb=line --html=report.html --browser_name=chrome
```
