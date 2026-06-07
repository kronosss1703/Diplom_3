import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    WORKING_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_all_time_counter(self):
        return int(self.get_text(self.ALL_TIME_COUNTER))

    @allure.step("Получение значения счётчика 'Выполнено за сегодня'")
    def get_today_counter(self):
        return int(self.get_text(self.TODAY_COUNTER))

    @allure.step("Получение списка номеров заказов в работе")
    def get_order_numbers_in_work(self):
        elements = self.driver.find_elements(*self.WORKING_ORDERS)
        return [el.text for el in elements]