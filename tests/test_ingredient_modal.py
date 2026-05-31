import allure
from pages.main_page import MainPage

@allure.feature("Ингредиенты")
class TestIngredientModal:
    @allure.title("Клик на ингредиент открывает модальное окно")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        assert page.is_modal_visible()

    @allure.title("Модальное окно закрывается крестиком")
    def test_modal_closes(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        assert page.is_modal_visible()
        page.close_modal()
        assert not page.is_modal_visible()