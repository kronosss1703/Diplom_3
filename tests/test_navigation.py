import allure
from pages.main_page import MainPage

@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Переход в Конструктор")
    def test_constructor_navigation(self, driver):
        page = MainPage(driver)
        page.click_order_feed()
        page.click_constructor()
        assert "feed" not in driver.current_url

    @allure.title("Переход в Ленту заказов")
    def test_order_feed_navigation(self, driver):
        page = MainPage(driver)
        page.click_order_feed()
        assert "feed" in driver.current_url