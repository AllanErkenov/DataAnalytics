# Создание страницы Django

На данной странице показывается два курса с криптовалютами (USDT к рублю и TRON к USDT) и данная температура в Москве. Данные автоматически обновляются каждую минуту благодаря коду на JavaScript
Для начала нужно закачать фаилы с данного репозитория, затем открыть папку "newproject" и в ней в командной строке выполнить команду
```
python manage.py runserver.
```
Должно показать примерно такое:

```
January 17, 2025 - 20:11:09
Django version 5.1.5, using settings 'newproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

К http://127.0.0.1:8000/ добавить index и в браузере ввести http://127.0.0.1:8000/index


**Использованные библиотеки**
- django
- requests
- bs4


