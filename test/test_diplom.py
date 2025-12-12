import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# Позитивные сценарии
# Тест 1.1: Оплата тура с валидной картой "APPROVED":
def test_payment_with_a_valid_card(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.2: Ввод валидных данных в поле "Номер карты":
def test_valid_data_card_number(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.3: Ввод валидных данных в поле "Месяц":
def test_valid_data_month(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.4: Ввод валидных данных в поле "Год":
def test_valid_data_year(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.5: Ввод валидных данных в поле "Владелец":
def test_valid_data_owner(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.6: Ввод валидных данных в поле "CVC/CVV":
def test_valid_data_cvc(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.7: Проверка записи в базу данных

# Тест 1.8: Оплата тура с получением кредита по валидной карте "APPROVED":
def test_valid_credit(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить в кредит'
    buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
    buy_credit_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.9: Ввод валидных данных в поле "Номер карты":
def test_valid_data_credit_card_number(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить в кредит'
    buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
    buy_credit_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.10: Ввод валидных данных в поле "Месяц":
def test_valid_data_credit_month(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить в кредит'
    buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
    buy_credit_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.11: Ввод валидных данных в поле "Год":
def test_valid_data_credit_year(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить в кредит'
    buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
    buy_credit_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.12: Ввод валидных данных в поле "Владелец":
def test_valid_data_credit_owner(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить в кредит'
    buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
    buy_credit_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text

# Тест 1.13: Ввод валидных данных в поле "CVC/CVV":
def test_valid_data_credit_cvc(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить в кредит'
    buy_credit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[2]')
    buy_credit_button.click()

    # Находим поля ввода и заполняем их валидными данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления об успешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_ok')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Операция одобрена Банком." in notification_text


# # Тест 1.14: Проверка записи в базу данных

# Негативные сценарии
# Тест 2.1: Оплата тура с невалидной картой "DECLINED":":
def test_payment_by_invalid_card(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления уведомления о неуспешной оплате
    wait = WebDriverWait(driver, 15)
    success_notification = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.notification.notification_status_error')))

    # Проверяем текст уведомления
    notification_text = success_notification.find_element(By.CLASS_NAME, 'notification__content').text
    assert "Ошибка! Банк отказал в проведении операции." in notification_text

# Тест 2.2: Ввод невалидных данных в поле "Номер карты":
def test_invalid_data_letter_card_number(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их данными
    card_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
    card_number_input.clear()

    # Изначальное пустое значение поля
    initial_value = card_number_input.get_attribute('value')

    # Вводим невалидные данные
    test_string = "4444aaaa"
    card_number_input.send_keys(test_string)

    # Новое значение поля
    updated_value = card_number_input.get_attribute('value')

    # Проверяем, что поле принимает только цифры
    assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"


# Тест 2.5: Ввод невалидных данных в поле "Номер карты":
def test_empty_field_card_number(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления ошибки
    error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[3]')
    assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."

# Тест 2.6: Ввод невалидных данных в поле "Месяц":
def test_invalid_data_month(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода, очищаем и заполняем их данными
    month_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
    month_input.clear()

    # Изначальное пустое значение поля
    initial_value = month_input.get_attribute('value')

    # Вводим невалидные данные
    test_string = "13"
    month_input.send_keys(test_string)

    # Новое значение поля
    updated_value = month_input.get_attribute('value')

    # Проверяем, что поле принимает только цифры
    assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

   # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Проверяем корректность месяца
    if updated_value:
        entered_month = int(updated_value)
        if 1 <= entered_month <= 12:
            is_month_correct = True
        else:
        # Ожидаем появления ошибки
            error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
            assert "Неверно указан срок действия карты" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."


# Тест 2.7: Ввод невалидных данных в поле "Месяц":
def test_empty_field_month(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их данными
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

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Ожидаем появления ошибки
    error_message = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
    assert "Неверный формат" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."


# Тест 2.10: Ввод невалидных данных в поле "Месяц":
def test_invalid_data_letter_month(driver):

    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода и заполняем их данными
    month_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
    month_input.clear()

    # Изначальное пустое значение поля
    initial_value = month_input.get_attribute('value')

    # Вводим невалидные данные
    test_string = "пп"
    month_input.send_keys(test_string)

    # Новое значение поля
    updated_value = month_input.get_attribute('value')

    # Проверяем, что поле принимает только цифры
    assert set(updated_value).issubset(
        set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"


# Тест 2.11: Ввод невалидных данных в поле "Год":
def test_invalid_data_year(driver):
    # Переходим на страницу
    driver.get("http://localhost:8080/")

    # Находим и нажимаем кнопку 'Купить'
    buy_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/button[1]')
    buy_button.click()

    # Находим поля ввода, очищаем и заполняем их данными
    year_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')
    year_input.clear()

    # Изначальное пустое значение поля
    initial_value = year_input.get_attribute('value')

    # Вводим невалидные данные
    test_string = "24"
    year_input.send_keys(test_string)

    # Новое значение поля
    updated_value = year_input.get_attribute('value')

    # Проверяем, что поле принимает только цифры
    assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    # Находим и нажимаем кнопку "Продолжить"
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')
    continue_button.click()

    # Проверяем корректность года
    if updated_value:
        entered_year = int(updated_value)
        if 25 <= entered_year:
            is_year_correct = True
        else:
        # Ожидаем появления ошибки
            error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
            assert "Истёк срок действия карты" in error_message.text, "Ошибка не появилась или текст не соответствует ожиданию."