from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a")
    ORDER_FEED_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a")
    INGREDIENT = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[2]")
    MODAL_CONTENT = (By.XPATH, "//*[@id='root']/div/section[1]/div[1]/div")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//*[@id='root']/div/section[1]/div[1]/button/svg/path")
    ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    ORDER_NUMBER = (By.XPATH, "//*[@id='root']/div/section[2]/div[1]/div/h2")

    def click_constructor(self):
        self.click(self.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click(self.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click(self.INGREDIENT)

    def is_modal_visible(self):
        return self.is_visible(self.MODAL_CONTENT)

    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    def click_order_button(self):
        self.click(self.ORDER_BUTTON)

    def get_order_number(self):
        return self.get_text(self.ORDER_NUMBER)