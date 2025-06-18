from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class TestRegistrationForm:
    @allure.title("Успешная регистрация пользователя")
    @allure.feature("Регистрация")
    @allure.story("Позитивный сценарий")
    def test_successful_registration(self, browser):
        """Тест успешной регистрации с валидными данными"""

        test_email = f"test_{int(time.time())}@example.com"
        test_password = "TestPassword123!"
        test_username = "testuser"

        with allure.step("Открываем страницу регистрации"):
            browser.get("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        with allure.step(f"Вводим email: {test_email}"):
            email_field = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input.MuiInputBase-input"))
            )
            email_field.clear()
            email_field.send_keys(test_email)

        with allure.step(f"Вводим имя пользователя: {test_username}"):
            username_field = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
            )
            username_field.clear()
            username_field.send_keys(test_username)

        with allure.step("Вводим пароль"):
            password_field = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))
            )
            password_field.clear()
            password_field.send_keys(test_password)

        with allure.step("Нажимаем кнопку регистрации"):
            register_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='registration-page-registration-button']"))
            )
            register_button.click()

        with allure.step("Проверяем успешную регистрацию и приветственный текст"):
            welcome_selector = "[data-testid='navigation-navbar-welcome-title-text']"
            welcome_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, welcome_selector))
            )
            actual_text = welcome_element.text
            assert "Welcome" in actual_text, f"Ожидалось, что в приветствии будет слово 'Welcome', но получено: '{actual_text}'"