import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_all_time_counter_increments(self, driver, auth_user):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        before = order_feed.get_all_time_counter()
        
        main_page.click_constructor()
        main_page.add_ingredient()
        main_page.click_order_button()
        
        main_page.click_order_feed()
        after = order_feed.get_all_time_counter()
        assert after > before

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_counter_increments(self, driver, auth_user):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        before = order_feed.get_today_counter()
        
        main_page.click_constructor()
        main_page.add_ingredient()
        main_page.click_order_button()
        
        main_page.click_order_feed()
        after = order_feed.get_today_counter()
        assert after > before

    @allure.title("Номер заказа появляется в 'В работе'")
    def test_order_number_in_work(self, driver, auth_user):
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_modal()
        
        main_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        assert order_number in order_feed.get_order_numbers_in_work()