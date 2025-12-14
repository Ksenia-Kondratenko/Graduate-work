# Описание проекта
Проект по автоматизированному тестированию Java-приложения с использованием Selenium и Allure Framework. Проект содержит UI-тесты, проверку базы данных и формирование отчетов в формате Allure.
## Инструкция по запуску
1. Установите необходимые инструменты:
- Docker и Docker Compose;
- Python 3.13.

2. Создайте виртуальное окружение:
- Перейдите в директорию проекта;
- Выполните команду: python -m venv venv;
- Активируйте виртуальное окружение: для Linux/Mac - команда source venv/bin/activate; для Windows - команда venv\Scripts\activate;

3. Установите зависимости из файла requirements.txt: команда pip install -r requirements.txt;


4. Запустите контейнеры с помощью Docker Compose: команда docker-compose up -d;


5. Запустите автотесты с генерацией отчетов Allure: команда pytest --alluredir=allure-results;


6. Просмотрите отчёт Allure: команда allure serve allure-results.



