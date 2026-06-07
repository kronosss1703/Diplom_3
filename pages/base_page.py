import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получение текста из {locator}")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверка видимости {locator}")
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step("Ожидание URL содержит {text}")
    def wait_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url