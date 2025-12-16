import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .database import DBConnector


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.1: Оплата тура с валидной картой 'APPROVED'")
# Позитивные сценарии
# Тест 1.1: Оплата тура с валидной картой "APPROVED":
def test_payment_with_a_valid_card(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text


@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.2: Ввод валидных данных в поле 'Номер карты'")
# Тест 1.2: Ввод валидных данных в поле "Номер карты":
def test_valid_data_card_number(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.3: Ввод валидных данных в поле 'Месяц'")
# Тест 1.3: Ввод валидных данных в поле "Месяц":
def test_valid_data_month(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('12')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.4: Ввод валидных данных в поле 'Год'")
# Тест 1.4: Ввод валидных данных в поле "Год":
def test_valid_data_year(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.5: Ввод валидных данных в поле 'Владелец'")
# Тест 1.5: Ввод валидных данных в поле "Владелец":
def test_valid_data_owner(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.6: Ввод валидных данных в поле 'CVC/CVV'")
# Тест 1.6: Ввод валидных данных в поле "CVC/CVV":
def test_valid_data_cvc(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 1.7: Проверка записи в базу данных")
# Тест 1.7: Проверка записи в базу данных
def test_database_presence_rec_valid_card(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'notification_status_ok')))
        assert "Операция одобрена Банком." in success_notification.text

    with allure.step("Проверяем наличие записи в базе данных"):
        connector = DBConnector(
            host='mysql_db',
            port=3306,
            user='app',
            password='pass',
            db='app'
        )
        query = "SELECT COUNT(*) FROM payment_entity WHERE last_four_digits=%s AND status='APPROVED';"
        result = connector.fetch_data(query, ('4441',))

    with allure.step("Проверяем, что результат ненулевой и первая запись содержит значение больше 0"):
        if len(result) == 0:
            assert False, "Запрос к базе данных вернул нулевое количество записей."
        elif result[0][0] <= 0:
            assert False, "Запись о платеже не найдена в базе данных"
        else:
            assert True, "Запись о платеже найдена в базе данных."

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.8: Оплата тура с получением кредита по валидной карте 'APPROVED'")
# Тест 1.8: Оплата тура с получением кредита по валидной карте "APPROVED":
def test_valid_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.9: Ввод валидных данных в поле 'Номер карты'")
# Тест 1.9: Ввод валидных данных в поле "Номер карты":
def test_valid_data_credit_card_number(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.10: Ввод валидных данных в поле 'Месяц'")
# Тест 1.10: Ввод валидных данных в поле "Месяц":
def test_valid_data_credit_month(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.11: Ввод валидных данных в поле 'Год'")
# Тест 1.11: Ввод валидных данных в поле "Год":
def test_valid_data_credit_year(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
     buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
     buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.12: Ввод валидных данных в поле 'Владелец'")
# Тест 1.12: Ввод валидных данных в поле "Владелец":
def test_valid_data_credit_owner(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.13: Ввод валидных данных в поле 'CVC/CVV'")
# Тест 1.13: Ввод валидных данных в поле "CVC/CVV":
def test_valid_data_credit_cvc(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

@allure.epic("Позитивные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 1.14: Проверка записи в базу данных")
# Тест 1.14: Проверка записи в базу данных
def test_database_presence_rec_valid_card_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_credit_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('07')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления об успешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Операция одобрена Банком." in notification_text

    with allure.step("Проверяем наличие записи в базе данных"):
        connector = DBConnector(
            host='mysql_db',
            port=3306,
            user='app',
            password='pass',
            db='app'
        )
        query = "SELECT COUNT(*) FROM payment_entity WHERE last_four_digits=%s AND status='APPROVED';"
        result = connector.fetch_data(query, ('4441',))

    with allure.step("Проверяем, что результат ненулевой и первая запись содержит значение больше 0"):
        if len(result) == 0:
            assert False, "Запрос к базе данных вернул нулевое количество записей."
        elif result[0][0] <= 0:
            assert False, "Запись о платеже не найдена в базе данных"
        else:
            assert True, "Запись о платеже найдена в базе данных."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.1: Оплата тура с невалидной картой 'DECLINED'")
# Негативные сценарии
# Тест 2.1: Оплата тура с невалидной картой "DECLINED":":
def test_payment_by_invalid_card(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их валидными данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444442')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления о неуспешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_error')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Ошибка! Банк отказал в проведении операции." in notification_text

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.2: Ввод невалидных данных в поле 'Номер карты'")
# Тест 2.2: Ввод невалидных данных в поле "Номер карты":
@pytest.mark.parametrize("test_string", [
    "aaa",           # Буквы
    "!#$%",          # Спецсимволы
    " ",             # Пробел
])
def test_invalid_data_card_number(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()

    with allure.step("Вводим невалидные данные"):
        card_number_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = card_number_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.3: Ввод невалидных данных в поле 'Номер карты' (пустое поле)")
# Тест 2.3: Ввод невалидных данных в поле "Номер карты" (пустое поле):
def test_empty_field_card_number(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[3]')
        assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.4: Ввод невалидных данных в поле 'Месяц'")
# Тест 2.4: Ввод невалидных данных в поле "Месяц":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
    "13",
])
def test_invalid_data_month(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода, очищаем и заполняем их данными"):
        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        month_input.clear()

    with allure.step("Вводим невалидные данные"):
        month_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = month_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Проверяем корректность месяца"):
        if updated_value:
            entered_month = int(updated_value)
            if 1 <= entered_month <= 12:
                is_month_correct = True
            else:
                with allure.step("Ожидаем появления ошибки"):
                    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
                    assert "Неверно указан срок действия карты" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.5: Ввод невалидных данных в поле 'Месяц' (пустое поле)")
# Тест 2.5: Ввод невалидных данных в поле "Месяц" (пустое поле):
def test_empty_field_month(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
        assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.6: Ввод невалидных данных в поле 'Год'")
# Тест 2.6: Ввод невалидных данных в поле "Год":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
])
def test_invalid_data_year(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода, очищаем и заполняем их данными"):
        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        year_input.clear()

    with allure.step("Вводим невалидные данные"):
        year_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = year_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Проверяем корректность года"):
        if updated_value:
            entered_year = int(updated_value)
            if 25 <= entered_year:
                is_year_correct = True
            else:
                with allure.step("Ожидаем появления ошибки"):
                    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
                    assert "Истёк срок действия карты" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.7: Ввод невалидных данных в поле 'Год' (пустое поле)")
# Тест 2.7: Ввод невалидных данных в поле "Год" (пустое поле):
def test_empty_field_year(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
        assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.8: Ввод невалидных данных в поле 'Владелец'")
# Тест 2.8: Ввод невалидных данных в поле "Владелец":
@pytest.mark.parametrize("test_string", [
    "456",
    "!#$%",
    " ",
])
def test_invalid_data_owner(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        owner_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        owner_input.clear()

    with allure.step("Вводим невалидные данные"):
        owner_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = owner_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только буквы"):
        assert not any(char.isdigit() for char in updated_value), \
            f"Поле принимает значение, отличное от букв. Текущее значение: '{updated_value}'"

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.9: Ввод невалидных данных в поле 'Владелец' (пустое поле)")
# Тест 2.9: Ввод невалидных данных в поле "Владелец" (пустое поле):
def test_empty_field_owner(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[3]')
        assert "Поле обязательно для заполнения" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.10: Ввод невалидных данных в поле 'CVV/CVC'")
# Тест 2.10: Ввод невалидных данных в поле "CVV/CVC":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
])
def test_invalid_data_cvv(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        cvv_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        cvv_input.clear()

    with allure.step("Вводим невалидные данные"):
        cvv_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = cvv_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(
            set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.11: Ввод невалидных данных в поле 'CVV/CVC' (пустое поле)")
# Тест 2.11: Ввод невалидных данных в поле "CVV/CVC" (пустое поле):
def test_empty_field_cvv(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('555')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[3]')
        assert "Поле обязательно для заполнения" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура по дебетовой карте")
@allure.description("Тест 2.12: Проверка записи в базу данных")
# Тест 2.12: Проверка записи в базу данных
def test_database_by_invalid_card(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444442')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления о неуспешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_error')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Ошибка! Банк отказал в проведении операции." in notification_text

    with allure.step("Проверяем наличие записи в базе данных"):
        connector = DBConnector(
            host='mysql_db',
            port=3306,
            user='app',
            password='pass',
            db='app'
        )
        query = "SELECT COUNT(*) FROM payment_entity WHERE last_four_digits=%s AND status='DECLINED';"
        result = connector.fetch_data(query, ('4442',))

    with allure.step("Проверяем, что результат ненулевой и первая запись содержит значение больше 0"):
        if len(result) == 0:
            assert False, "Запрос к базе данных вернул нулевое количество записей."
        elif result[0][0] <= 0:
            assert False, "Запись о платеже не найдена в базе данных!"
        else:
            assert True, "Запись о платеже найдена в базе данных."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.13. Оплата тура с получением кредита по невалидной карте 'DECLINED'")
# Тест 2.13. Оплата тура с получением кредита по невалидной карте "DECLINED":
def test_payment_by_invalid_card_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444442')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления о неуспешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_error')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Ошибка! Банк отказал в проведении операции." in notification_text

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.14. Ввод невалидных данных в поле 'Номер карты'")
# Тест 2.14: Ввод невалидных данных в поле "Номер карты":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
])
def test_invalid_data_card_number_credit(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()

    with allure.step("Вводим невалидные данные"):
        card_number_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = card_number_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.15. Ввод невалидных данных в поле 'Номер карты' (пустое поле)")
# Тест 2.15: Ввод невалидных данных в поле "Номер карты (пустое поле)":
def test_empty_field_card_number_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[3]')
        assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.16. Ввод невалидных данных в поле 'Месяц'")
# Тест 2.16: Ввод невалидных данных в поле "Месяц":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
    "13",
])
def test_invalid_data_month_credit(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода, очищаем и заполняем их данными"):
        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        month_input.clear()

    with allure.step("Вводим невалидные данные"):
        month_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = month_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Проверяем корректность месяца"):
        if updated_value:
            entered_month = int(updated_value)
            if 1 <= entered_month <= 12:
                is_month_correct = True
            else:
                with allure.step("Ожидаем появления ошибки"):
                    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
                    assert "Неверно указан срок действия карты" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.17. Ввод невалидных данных в поле 'Месяц' (пустое поле)")
# Тест 2.17: Ввод невалидных данных в поле "Месяц" (пустое поле):
def test_empty_field_month_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
        assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.18. Ввод невалидных данных в поле 'Год'")
# Тест 2.18: Ввод невалидных данных в поле "Год":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
    "24",
])
def test_invalid_data_year_credit(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода, очищаем и заполняем их данными"):
        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        year_input.clear()

    with allure.step("Вводим невалидные данные"):
        year_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = year_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Проверяем корректность года"):
        if updated_value:
            entered_year = int(updated_value)
            if 25 <= entered_year:
                is_year_correct = True
            else:
                with allure.step("Ожидаем появления ошибки"):
                    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
                    assert "Истёк срок действия карты" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.19. Ввод невалидных данных в поле 'Год' (пустое поле)")
# Тест 2.19: Ввод невалидных данных в поле "Год" (пустое поле):
def test_empty_field_year_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
        assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.20. Ввод невалидных данных в поле 'Владелец'")
# Тест 2.20: Ввод невалидных данных в поле "Владелец":
@pytest.mark.parametrize("test_string", [
    "456",
    "!#$%",
    " ",
])
def test_invalid_data_owner_credit(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        owner_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        owner_input.clear()

    with allure.step("Вводим невалидные данные"):
        owner_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = owner_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert not any(char.isdigit() for char in updated_value), \
            f"Поле принимает значение, отличное от букв. Текущее значение: '{updated_value}'"

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.21. Ввод невалидных данных в поле 'Владелец' (пустое поле)")
# Тест 2.21: Ввод невалидных данных в поле "Владелец" (пустое поле):
def test_empty_field_owner_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[3]')
        assert "Поле обязательно для заполнения" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.22. Ввод невалидных данных в поле 'CVV/CVC'")
# Тест 2.22: Ввод невалидных данных в поле "CVV/CVC":
@pytest.mark.parametrize("test_string", [
    "aaa",
    "!#$%",
    " ",
])
def test_invalid_data_cvv_credit(driver, test_string):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        cvv_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        cvv_input.clear()

    with allure.step("Вводим невалидные данные"):
        cvv_input.send_keys(test_string)

    with allure.step("Новое значение поля"):
        updated_value = cvv_input.get_attribute('value')

    with allure.step("Проверяем, что поле принимает только цифры"):
        assert set(updated_value).issubset(
            set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.23. Ввод невалидных данных в поле 'CVV/CVC' (пустое поле)")
# Тест 2.23: Ввод невалидных данных в поле "CVV/CVC" (пустое поле):
def test_empty_field_cvv_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444 4444 4444 4441')

        month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('555')

        cvc_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления ошибки"):
        error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[3]')
        assert "Поле обязательно для заполнения" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

@allure.epic("Негативные сценарии")
@allure.title("Тестирование оплаты тура с кредитом")
@allure.description("Тест 2.24: Проверка записи в базу данных")
# Тест 2.24: Проверка записи в базу данных
def test_database_by_invalid_card_credit(driver):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
        buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
        buy_button.click()

    with allure.step("Находим поля ввода и заполняем их данными"):
        card_number_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
        card_number_input.clear()
        card_number_input.send_keys('4444444444444442')

        month_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')
        month_input.clear()
        month_input.send_keys('08')

        year_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')
        year_input.clear()
        year_input.send_keys('26')

        owner_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')
        owner_input.clear()
        owner_input.send_keys('DENIS IVANOV')

        cvc_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')
        cvc_input.clear()
        cvc_input.send_keys('555')

    with allure.step("Находим и нажимаем кнопку 'Продолжить'"):
        continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
        continue_button.click()

    with allure.step("Ожидаем появления уведомления о неуспешной оплате"):
        wait = WebDriverWait(driver, 15)
        success_notification = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_error')))

    with allure.step("Проверяем текст уведомления"):
        notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
        assert "Ошибка! Банк отказал в проведении операции." in notification_text

    with allure.step("Проверяем запись в базе данных"):
        connector = DBConnector(
            host='mysql_db',
            port=3306,
            user='app',
            password='pass',
            db='app'
        )
        query = "SELECT COUNT(*) FROM payment_entity WHERE last_four_digits=%s AND status='DECLINED';"
        result = connector.fetch_data(query, ('4442',))

    with allure.step("Проверяем, что результат ненулевой и первая запись содержит значение больше 0"):
        if len(result) == 0:
            assert False, "Запрос к базе данных вернул нулевое количество записей."
        elif result[0][0] <= 0:
            assert False, "Запись о платеже не найдена в базе данных!"
        else:
            assert True, "Запись о платеже найдена в базе данных."

@allure.epic("Иные проверки")
@allure.title("Проверка орфографии")
@allure.description("Тест 2.25: Проверка орфографии")
# Тест 2.25: Проверка орфографии
@pytest.mark.parametrize("expected_text, xpath", [
    ("Путешествие дня", '//*[@id="root"]/div/h2'),
    ("Марракеш", '//*[@id="root"]/div/div/div/div[2]/h3'),
    ("Сказочный Восток", '//*[@id="root"]/div/div/div/div[2]/ul/li[1]'),
    ("33 360 миль на карту", '//*[@id="root"]/div/div/div/div[2]/ul/li[2]'),
    ("До 7% на остаток по счёту", '//*[@id="root"]/div/div/div/div[2]/ul/li[3]'),
    ("Всего 45 000 руб.!", '//*[@id="root"]/div/div/div/div[2]/ul/li[4]'),
])
def test_valid_text_1(driver, expected_text, xpath):
    with allure.step("Переходим на страницу"):
        driver.get("http://localhost:8080/")

    with allure.step("Находим элемент с текстом"):
        notification_text = driver.find_element(By.XPATH, xpath).text

    with allure.step("Проверяем корректность текста"):
        assert expected_text in notification_text, f"Текст поля не содержит '{expected_text}'"