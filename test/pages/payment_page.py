from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:8080/"                           # Адрес домашней страницы
        self.buy_button = (By.XPATH, '//*[@id="root"]/div/button[1]')  # Селектор кнопки "Купить"
        self.buy_credit_button = (By.XPATH, '//*[@id="root"]/div/button[2]')  # Селектор кнопки "Купить в кредит"
        self.card_number_field = (By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[2]/input')  # Поле номера карты
        self.month_field = (By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[2]/input')  # Поле месяца
        self.year_field = (By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[2]/input')  # Поле года
        self.owner_field = (By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[2]/input')  # Поле владельца
        self.cvc_field = (By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[2]/input')  # Поле CVC
        self.continue_button = (By.XPATH, '//*[@id="root"]/div/form/fieldset/div[4]/button')  # Кнопка "Продолжить"
        self.success_notification = (By.CSS_SELECTOR, '.notification.notification_status_ok')  # Уведомление успеха
        self.error_notification = (By.CSS_SELECTOR, '.notification.notification_status_error')  # Уведомление ошибки

    def open(self):
        # Переход на страницу
        self.driver.get(self.url)

    def click_buy_button(self):
        # Нажатие кнопки "Купить"
        buy_button = self.driver.find_element(*self.buy_button)
        buy_button.click()

    def click_buy_credit_button(self):
        # Нажатие кнопки "Купить в кредит"
        buy_credit_button = self.driver.find_element(*self.buy_credit_button)
        buy_credit_button.click()

    def fill_form(self, card_number, month, year, owner, cvc):
        # Заполнение полей
        inputs = {
            'card_number': self.card_number_field,
            'month': self.month_field,
            'year': self.year_field,
            'owner': self.owner_field,
            'cvc': self.cvc_field
        }

        for field_name, locator in inputs.items():
            input_field = self.driver.find_element(*locator)
            input_field.clear()
            if field_name == 'card_number':
                input_field.send_keys(card_number)
            elif field_name == 'month':
                input_field.send_keys(month)
            elif field_name == 'year':
                input_field.send_keys(year)
            elif field_name == 'owner':
                input_field.send_keys(owner)
            elif field_name == 'cvc':
                input_field.send_keys(cvc)

    def submit_form(self):
        # Нажатие кнопки "Продолжить"
        continue_button = self.driver.find_element(*self.continue_button)
        continue_button.click()

    def verify_successful_payment(self):
        # Проверка появления уведомления об успешной оплате
        wait = WebDriverWait(self.driver, 15)
        success_notification = wait.until(EC.visibility_of_element_located(self.success_notification))
        return success_notification.text

    def verify_failed_payment(self):
        # Проверка появления уведомления о неуспешной оплате
        wait = WebDriverWait(self.driver, 15)
        error_notification = wait.until(EC.visibility_of_element_located(self.error_notification))
        return error_notification.text

    def fill_card_number(self, number):
        # Заполняем поле номера карты
        card_number_field = self.driver.find_element(*self.card_number_field)
        card_number_field.clear()
        card_number_field.send_keys(number)

    def get_card_number_value(self):
        # Возвращаем текущее значение поля номера карты
        card_number_field = self.driver.find_element(*self.card_number_field)
        return card_number_field.get_attribute('value')

    def get_error_message_for_card_number(self):
        # Возвращаем текст ошибки для поля номера карты
        error_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[3]')
        return error_element.text

    def fill_month(self, month):
        # Заполняем поле месяца
        month_field = self.driver.find_element(*self.month_field)
        month_field.clear()
        month_field.send_keys(month)

    def get_month_value(self):
        # Возвращаем текущее значение поля месяца
        month_field = self.driver.find_element(*self.month_field)
        return month_field.get_attribute('value')

    def get_error_message_for_month(self):
        # Возвращает текст ошибки для поля месяца (Тест 2.5)
        error_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
        return error_element.text

    def fill_year(self, year):
        # Заполняем поле года
        year_field = self.driver.find_element(*self.year_field)
        year_field.clear()
        year_field.send_keys(year)

    def get_year_value(self):
        # Возвращаем текущее значение поля года
        year_field = self.driver.find_element(*self.year_field)
        return year_field.get_attribute('value')

    def get_error_message_for_year(self):
        # Возвращаем текст ошибки для поля года (Тест 2.7)
        error_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
        return error_element.text

    def fill_owner(self, owner):
        # Заполняем поле владельца
        owner_field = self.driver.find_element(*self.owner_field)
        owner_field.clear()
        owner_field.send_keys(owner)

    def get_owner_value(self):
        # Возвращаем текущее значение поля владельца
        owner_field = self.driver.find_element(*self.owner_field)
        return owner_field.get_attribute('value')

    def get_error_message_for_owner(self):
        # Возвращаем текст ошибки для поля владельца (Тест 2.9)
        error_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[3]')
        return error_element.text

    def fill_cvc(self, cvc):
        # Заполняем поле CVV/CVC
        cvc_field = self.driver.find_element(*self.cvc_field)
        cvc_field.clear()
        cvc_field.send_keys(cvc)

    def get_cvc_value(self):
        # Возвращаем текущее значение поля CVV/CVC
        cvc_field = self.driver.find_element(*self.cvc_field)
        return cvc_field.get_attribute('value')

    def get_error_message_for_cvc(self):
        # Возвращаем текст ошибки для поля CVV/CVC (Тест 2.11)
        error_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[3]')
        return error_element.text

    def get_error_message_for_card_number_credit(self):
        # Возвращаем текст ошибки для поля номера карты (Тест 2.15)
        error_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[1]/span/span/span[3]')
        return error_element.text

    def get_error_message_for_month_credit(self):
        # Возвращает текст ошибки для поля месяц (Тест 2.17)
        error_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[2]/span/span[1]/span/span/span[3]')
        return error_element.text

    def get_error_message_for_year_credit(self):
        # Возвращает текст ошибки для поля года (Тест 2.19)
        error_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[2]/span/span[2]/span/span/span[3]')
        return error_element.text

    def get_error_message_for_owner_credit(self):
        # Возвращает текст ошибки для поля владельца (Тест 2.21)
        error_element = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/form/fieldset/div[3]/span/span[1]/span/span/span[3]')
        return error_element.text

    def get_error_message_for_cvc_credit(self):
        # Возвращает текст ошибки для поля CVV/CVC (Тест 2.23)
        error_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/form/fieldset/div[3]/span/span[2]/span/span/span[3]')
        return error_element.text

    def get_text_from_xpath(self, xpath):
        # Возвращаем текст элемента по указанному XPath
        element = self.driver.find_element(By.XPATH, xpath)
        return element.text
