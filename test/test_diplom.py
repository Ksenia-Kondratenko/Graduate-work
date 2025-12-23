import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.utils.database import DBConnector
from .data.card_data import CardData
from .pages.payment_page import PaymentPage


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

@pytest.fixture
def payment_page(driver):
    return PaymentPage(driver)

@pytest.mark.usefixtures("clear_database")
class TestValidPayments:
    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.1: Оплата тура с валидной картой 'APPROVED'")
    def test_valid_payment(self, payment_page):
        with allure.step("Переходим на страницу"):
            payment_page.open()

        with allure.step("Находим и нажимаем кнопку 'Купить'"):
            payment_page.click_buy_button()

        with allure.step("Заполняем форму валидными данными"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.2: Ввод валидных данных в поле 'Номер карты'")
    def test_valid_data_card_number(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату с валидными данными"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.3: Ввод валидных данных в поле 'Месяц'")
    def test_valid_data_month(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату с валидными данными"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                '12',
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.4: Ввод валидных данных в поле 'Год'")
    def test_valid_data_year(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату с валидными данными"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                '26',
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.5: Ввод валидных данных в поле 'Владелец'")
    def test_valid_data_owner(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату с валидными данными"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                'DENIS IVANOV',
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.6: Ввод валидных данных в поле 'CVC/CVV'")
    def test_valid_data_cvc(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату с валидными данными"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                '555'
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.7: Проверка записи в базу данных")
    def test_database_presence_rec_valid_card(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

        with allure.step("Проверяем наличие записи в базе данных"):
            connector = DBConnector(
                host='localhost',
                port=3306,
                user='app',
                password='pass',
                db='app'
            )
            query = "SELECT COUNT(*) FROM payment_entity WHERE last_four_digits=%s AND status='APPROVED';"
            result = connector.fetch_data(query,('4441',))

        with allure.step("Проверяем, что результат ненулевой и первая запись содержит значение больше 0"):
            if len(result) == 0:
                assert False, "Запрос к базе данных вернул нулевое количество записей."
            elif result[0][0] <= 0:
                assert False, "Запись о платеже не найдена в базе данных"
            else:
                assert True, "Запись о платеже найдена в базе данных."

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.8: Проверка отсутствия данных карты в базе данных")
    def test_database_absence_card_data(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

        with allure.step("Проверяем отсутствие данных карты в базе данных"):
            connector = DBConnector(
                host='localhost',
                port=3306,
                user='app',
                password='pass',
                db='app'
            )
            query = "SELECT COUNT(*) FROM payment_entity WHERE card_number LIKE '%4444%' OR cvc IS NOT NULL;"
            result = connector.fetch_data(query)

        with allure.step("Проверяем, что запрос вернул 0 записей"):
            if len(result) == 0:
                assert False, "Запрос к базе данных вернул нулевое количество записей."
            elif result[0][0] > 0:
                assert False, "В базе данных обнаружены данные карты"
            else:
                assert True, "Данные карты не обнаружены в базе данных."

@pytest.mark.usefixtures("clear_database")
class TestCreditPurchase:
    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.9: Оплата тура с получением кредита по валидной карте 'APPROVED'")
    def test_valid_credit_purchase(self, payment_page):
        with allure.step("Переходим на страницу"):
            payment_page.open()

        with allure.step("Находим и нажимаем кнопку 'Купить в кредит'"):
            payment_page.click_buy_credit_button()

        with allure.step("Заполняем поля ввода валидными данными"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.10: Ввод валидных данных в поле 'Номер карты'")
    def test_valid_data_credit_card_number(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой с кредитом"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.11: Ввод валидных данных в поле 'Месяц'")
    def test_valid_data_credit_month(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                '07',
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.12: Ввод валидных данных в поле 'Год'")
    def test_valid_data_credit_year(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                '26',
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.13: Ввод валидных данных в поле 'Владелец'")
    def test_valid_data_credit_owner(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                'DENIS IVANOV',
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.14: Ввод валидных данных в поле 'CVC/CVV'")
    def test_valid_data_credit_cvc(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                '555'
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

    @allure.epic("Позитивные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 1.15: Проверка записи в базу данных")
    def test_database_presence_rec_valid_card_credit(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

        with allure.step("Проверяем наличие записи в базе данных"):
            connector = DBConnector(
                host='localhost',
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
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 1.16: Проверка отсутствия данных карты в базе данных при оплате с кредитом")
    def test_database_absence_card_data_credit(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату валидной картой в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем успешную оплату"):
            notification_text = payment_page.verify_successful_payment()
            assert "Операция одобрена Банком." in notification_text

        with allure.step("Проверяем отсутствие полных данных карты в базе данных"):
            connector = DBConnector(
                host='localhost',
                port=3306,
                user='app',
                password='pass',
                db='app'
            )
            query = "SELECT COUNT(*) FROM payment_entity WHERE card_number LIKE '%4444%' OR cvc IS NOT NULL;"
            result = connector.fetch_data(query)

        with allure.step("Проверяем, что запрос вернул 0 записей"):
            if len(result) == 0:
                assert False, "Запрос к базе данных вернул нулевое количество записей."
            elif result[0][0] > 0:
                assert False, "В базе данных обнаружены данные карты"
            else:
                assert True, "Данные карты не обнаружены в базе данных."

@pytest.mark.usefixtures("clear_database")
class TestInvalidPayments:
    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.1: Оплата тура с невалидной картой 'DECLINED'")
    def test_payment_by_invalid_card(self, payment_page):
        with allure.step("Переходим на страницу и пробуем произвести оплату невалидной картой"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.INVALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем неуспешную оплату"):
            notification_text = payment_page.verify_failed_payment()
            expected_text = "Ошибка! Банк отказал в проведении операции."
            assert expected_text in notification_text, f"Фактический текст уведомления: '{notification_text}', ожидаемый: '{expected_text}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.2: Ввод невалидных данных в поле 'Номер карты'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
    ])
    def test_invalid_data_card_number(self, payment_page, test_string):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Вводим невалидные данные в поле 'Номер карты'"):
            payment_page.fill_card_number(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_card_number_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.3: Ввод невалидных данных в поле 'Номер карты' (пустое поле)")
    def test_empty_field_card_number(self, payment_page):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Оставляем поле 'Номер карты' пустым и заполняем остальные поля"):
            payment_page.fill_card_number("")
            payment_page.fill_form(
                "",
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Пытаемся отправить форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_card_number()
            assert "Неверный формат" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.4: Ввод невалидных данных в поле 'Месяц'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
        "13",
    ])
    def test_invalid_data_month(self, payment_page, test_string):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Вводим невалидные данные в поле 'Месяц'"):
            payment_page.fill_month(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_month_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

        with allure.step("Проверяем корректность месяца"):
            if updated_value:
                entered_month = int(updated_value)
                if 1 <= entered_month <= 12:
                    is_month_correct = True
                else:
                    with allure.step("Ожидаем появления ошибки"):
                        error_message = payment_page.get_error_message_for_month()
                        assert "Неверно указан срок действия карты" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.5: Ввод невалидных данных в поле 'Месяц' (пустое поле)")
    def test_empty_field_month(self, payment_page):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Оставляем поле 'Месяц' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                '',
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_month()
            assert "Неверный формат" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.6: Ввод невалидных данных в поле 'Год'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
    ])
    def test_invalid_data_year(self, payment_page, test_string):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Вводим невалидные данные в поле 'Год'"):
            payment_page.fill_year(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_year_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

        with allure.step("Проверяем корректность года"):
            if updated_value:
                entered_year = int(updated_value)
                if 25 <= entered_year:
                    is_year_correct = True
                else:
                    with allure.step("Ожидаем появления ошибки"):
                        error_message = payment_page.get_error_message_for_year()
                        assert "Истёк срок действия карты" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.7: Ввод невалидных данных в поле 'Год' (пустое поле)")
    def test_empty_field_year(self, payment_page):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Оставляем поле 'Год' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                '',
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_year()
            assert "Неверный формат" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.8: Ввод невалидных данных в поле 'Владелец'")
    @pytest.mark.parametrize("test_string", [
        "456",
        "!#$%",
        " ",
    ])
    def test_invalid_data_owner(self, payment_page, test_string):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Вводим невалидные данные в поле 'Владелец'"):
            payment_page.fill_owner(test_string)

        with allure.step("Проверяем, что поле принимает только буквы"):
            updated_value = payment_page.get_owner_value()
            assert not any(char.isdigit() for char in updated_value), \
                f"Поле принимает значение, отличное от букв. Текущее значение: '{updated_value}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.9: Ввод невалидных данных в поле 'Владелец' (пустое поле)")
    def test_empty_field_owner(self, payment_page):
        with allure.step("Переходим на страницу и проводим оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Оставляем поле 'Владелец' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                '',
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_owner()
            assert "Поле обязательно для заполнения" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.10: Ввод невалидных данных в поле 'CVV/CVC'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
    ])
    def test_invalid_data_cvv(self, payment_page, test_string):
        with allure.step("Переходим на страницу и начинаем оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Вводим невалидные данные в поле 'CVV/CVC'"):
            payment_page.fill_cvc(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_cvc_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.11: Ввод невалидных данных в поле 'CVV/CVC' (пустое поле)")
    def test_empty_field_cvv(self, payment_page):
        with allure.step("Переходим на страницу и проводим оформление оплаты"):
            payment_page.open()
            payment_page.click_buy_button()

        with allure.step("Оставляем поле 'CVV/CVC' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                ''
            )

        with allure.step("Пытаемся отправить форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_cvc()
            assert "Поле обязательно для заполнения" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура по дебетовой карте")
    @allure.description("Тест 2.12: Проверка записи в базу данных")
    def test_database_by_invalid_card(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату невалидной картой"):
            payment_page.open()
            payment_page.click_buy_button()
            payment_page.fill_form(
                CardData.INVALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем неуспешную оплату"):
            notification_text = payment_page.verify_failed_payment()
            assert "Ошибка! Банк отказал в проведении операции." in notification_text

        with allure.step("Проверяем наличие записи в базе данных"):
            connector = DBConnector(
                host='localhost',
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

@pytest.mark.usefixtures("clear_database")
class TestInvalidCreditPayments:
    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.13: Оплата тура с получением кредита по невалидной карте 'DECLINED'")
    def test_payment_by_invalid_card_credit(self, payment_page):
        with allure.step("Переходим на страницу и проводим оплату в кредит невалидной картой"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.INVALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем неуспешную оплату"):
            notification_text = payment_page.verify_failed_payment()
            assert "Ошибка! Банк отказал в проведении операции." in notification_text

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.14: Ввод невалидных данных в поле 'Номер карты'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
    ])
    def test_invalid_data_card_number_credit(self, payment_page, test_string):
        with allure.step("Переходим на страницу и инициируем оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Вводим невалидные данные в поле 'Номер карты'"):
            payment_page.fill_card_number(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_card_number_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.15: Ввод невалидных данных в поле 'Номер карты' (пустое поле)")
    def test_empty_field_card_number_credit(self, payment_page):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Оставляем поле 'Номер карты' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                '',
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Пытаемся отправить форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_card_number_credit()
            assert "Неверный формат" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.16: Ввод невалидных данных в поле 'Месяц'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
        "13",
    ])
    def test_invalid_data_month_credit(self, payment_page, test_string):
        with allure.step("Переходим на страницу и инициируем оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Вводим невалидные данные в поле 'Месяц'"):
            payment_page.fill_month(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_month_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

        with allure.step("Проверяем корректность месяца"):
            if updated_value:
                entered_month = int(updated_value)
                if 1 <= entered_month <= 12:
                    is_month_correct = True
                else:
                    with allure.step("Ожидаем появления ошибки"):
                        error_message = payment_page.get_error_message_for_month()
                        assert "Неверно указан срок действия карты" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.17: Ввод невалидных данных в поле 'Месяц' (пустое поле)")
    def test_empty_field_month_credit(self, payment_page):
        with allure.step("Переходим на страницу и инициируем оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Оставляем поле 'Месяц' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                '',
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_month_credit()
            assert "Неверный формат" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.18: Ввод невалидных данных в поле 'Год'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
        "24",
    ])
    def test_invalid_data_year_credit(self, payment_page, test_string):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Вводим невалидные данные в поле 'Год'"):
            payment_page.fill_year(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_year_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

        with allure.step("Проверяем корректность года"):
            if updated_value:
                entered_year = int(updated_value)
                if 25 <= entered_year:
                    is_year_correct = True
                else:
                    with allure.step("Ожидаем появления ошибки"):
                        error_message = payment_page.get_error_message_for_year()
                        assert "Истёк срок действия карты" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.19: Ввод невалидных данных в поле 'Год' (пустое поле)")
    def test_empty_field_year_credit(self, payment_page):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Оставляем поле 'Год' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                '',
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_year_credit()
            assert "Неверный формат" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.20: Ввод невалидных данных в поле 'Владелец'")
    @pytest.mark.parametrize("test_string", [
        "456",
        "!#$%",
        " ",
    ])
    def test_invalid_data_owner_credit(self, payment_page, test_string):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Вводим невалидные данные в поле 'Владелец'"):
            payment_page.fill_owner(test_string)

        with allure.step("Проверяем, что поле принимает только буквы"):
            updated_value = payment_page.get_owner_value()
            assert not any(char.isdigit() for char in updated_value), \
                f"Поле принимает значение, отличное от букв. Текущее значение: '{updated_value}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.21: Ввод невалидных данных в поле 'Владелец' (пустое поле)")
    def test_empty_field_owner_credit(self, payment_page):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Оставляем поле 'Владелец' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                '',
                CardData.VALID_CVC
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_owner_credit()
            assert "Поле обязательно для заполнения" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.22: Ввод невалидных данных в поле 'CVV/CVC'")
    @pytest.mark.parametrize("test_string", [
        "aaa",
        "!#$%",
        " ",
    ])
    def test_invalid_data_cvv_credit(self, payment_page, test_string):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Вводим невалидные данные в поле 'CVV/CVC'"):
            payment_page.fill_cvc(test_string)

        with allure.step("Проверяем, что поле принимает только цифры"):
            updated_value = payment_page.get_cvc_value()
            assert set(updated_value).issubset(set("0123456789")), f"Поле приняло символы, отличные от цифр. Текущее значение: '{updated_value}'"

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.23: Ввод невалидных данных в поле 'CVV/CVC' (пустое поле)")
    def test_empty_field_cvv_credit(self, payment_page):
        with allure.step("Переходим на страницу и проводим оплату в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()

        with allure.step("Оставляем поле 'CVV/CVC' пустым и заполняем остальные поля"):
            payment_page.fill_form(
                CardData.VALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                ''
            )

        with allure.step("Отправляем форму"):
            payment_page.submit_form()

        with allure.step("Ожидаем появления ошибки"):
            error_message = payment_page.get_error_message_for_cvc_credit()
            assert "Поле обязательно для заполнения" in error_message, "Ошибка не появилась или текст не соответствует ожиданию."

    @allure.epic("Негативные сценарии")
    @allure.title("Тестирование оплаты тура с кредитом")
    @allure.description("Тест 2.24: Проверка записи в базу данных")
    def test_database_by_invalid_card_credit(self, payment_page):
        with allure.step("Переходим на страницу и производим оплату невалидной картой в кредит"):
            payment_page.open()
            payment_page.click_buy_credit_button()
            payment_page.fill_form(
                CardData.INVALID_CARD_NUMBER,
                CardData.VALID_MONTH,
                CardData.VALID_YEAR,
                CardData.VALID_OWNER,
                CardData.VALID_CVC
            )
            payment_page.submit_form()

        with allure.step("Проверяем неуспешную оплату"):
            notification_text = payment_page.verify_failed_payment()
            assert "Ошибка! Банк отказал в проведении операции." in notification_text

        with allure.step("Проверяем запись в базе данных"):
            connector = DBConnector(
                host='localhost',
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

@pytest.mark.usefixtures("clear_database")
class TestOtherChecks:
    @allure.epic("Иные проверки")
    @allure.title("Проверка орфографии")
    @allure.description("Тест 2.25: Проверка орфографии")
    @pytest.mark.parametrize("expected_text, xpath", [
        ("Путешествие дня", '//*[@id="root"]/div/h2'),
        ("Марракеш", '//*[@id="root"]/div/div/div/div[2]/h3'),
        ("Сказочный Восток", '//*[@id="root"]/div/div/div/div[2]/ul/li[1]'),
        ("33 360 миль на карту", '//*[@id="root"]/div/div/div/div[2]/ul/li[2]'),
        ("До 7% на остаток по счёту", '//*[@id="root"]/div/div/div/div[2]/ul/li[3]'),
        ("Всего 45 000 руб.!", '//*[@id="root"]/div/div/div/div[2]/ul/li[4]'),
    ])
    def test_valid_text_1(self, payment_page, expected_text, xpath):
        with allure.step("Переходим на страницу"):
            payment_page.open()

        with allure.step("Находим элемент с текстом"):
            notification_text = payment_page.get_text_from_xpath(xpath)

        with allure.step("Проверяем корректность текста"):
            assert expected_text in notification_text, f"Текст поля не содержит '{expected_text}'"