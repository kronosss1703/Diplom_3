import allure
from pages.main_page import MainPage

@allure.feature("Счётчик ингредиентов")
class TestCounter:
    @allure.title("Счётчик увеличивается при добавлении ингредиента")
    def test_counter_increments(self, driver):
        page = MainPage(driver)
        before = page.get_counter()
        page.add_ingredient()
        after = page.get_counter()
        assert after == before + 1