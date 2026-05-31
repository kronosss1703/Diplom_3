from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    WORKING_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")

    def get_all_time_counter(self):
        return int(self.get_text(self.ALL_TIME_COUNTER))

    def get_today_counter(self):
        return int(self.get_text(self.TODAY_COUNTER))

    def get_order_numbers_in_work(self):
        return [el.text for el in self.driver.find_elements(*self.WORKING_ORDERS)]