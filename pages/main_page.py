import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/') and contains(text(), 'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")
    INGREDIENT = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ADD_BUTTON = (By.XPATH, "//button[text()='Добавить']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2")

    @allure.step("Клик на Конструктор")
    def click_constructor(self):
        self.click(self.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на Ленту заказов")
    def click_order_feed(self):
        self.click(self.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        self.click(self.INGREDIENT)

    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        return self.is_visible(self.MODAL_CONTENT)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    @allure.step("Получение значения счётчика")
    def get_counter(self):
        return int(self.get_text(self.COUNTER))

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient(self):
        before = self.get_counter()
        self.click_ingredient()
        self.click(self.ADD_BUTTON)
        self.wait.until(lambda d: self.get_counter() > before)

    @allure.step("Клик на Оформить заказ")
    def click_order_button(self):
        self.click(self.ORDER_BUTTON)

    @allure.step("Получение номера заказа из модалки")
    def get_order_number(self):
        return self.get_text(self.ORDER_NUMBER)