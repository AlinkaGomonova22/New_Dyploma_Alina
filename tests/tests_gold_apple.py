import time
import pytest
import allure
# from pages.choose_city import CartPage
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.choose_city import ChooseCity
from pages.header import Header
# from pages.registration_page import RegistrationPage
from pages.search_page import SearchPage


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Домашняя страница")
@allure.title("Проверка отображения сторисов")
def test_cart_remove(driver):
    home_page = HomePage(driver)
    choose_city = ChooseCity(driver)

    home_page.open()
    choose_city.check_city_button()




#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Корзина")
# @allure.title("Сумма стоимости нескольких товаров в корзине")
# def test_cart_multiple(driver):
#     home_page = HomePage(driver)
#     cart_page = CartPage(driver)
#
#     home_page.open()
#     home_page.add_item_to_cart()
#     home_page.go_to_cart_page()
#     initial_price = cart_page.get_item_price()
#     cart_page.select_multiple_items_in_cart()
#     cart_page.check_price_has_increased(initial_price, 2)

#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Поиск, фильтрация и сортировка")
# @allure.title("Поиск товаров")
# def test_search(driver):
#     home_page = HomePage(driver)
#     search_page = SearchPage(driver)
#
#     search_texts = ['Torba', 'Koszulka', 'Bluza', 'Spodnie']
#     home_page.open()
#
#     for search_text in search_texts:
#         home_page.search(search_text)
#         time.sleep(1)
#         search_page.check_search_results_count()
#         search_page.check_search_texts_are_equal()
#         time.sleep(1)
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Поиск, фильтрация и сортировка")
# @allure.title("Поиск отсутствующего товара")
# def test_absent_search(driver):
#     home_page = HomePage(driver)
#     search_page = SearchPage(driver)
#
#     search_text = '423u8r9uioehfgju4839uijrefhio'
#     home_page.open()
#
#     home_page.search(search_text)
#     time.sleep(1)
#     search_page.check_nothing_found()
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Поиск, фильтрация и сортировка")
# @allure.title("Сортировка по цене: по возрастанию")
# def test_sort(driver):
#     home_page = HomePage(driver)
#     search_page = SearchPage(driver)
#
#     search_text = 'Torba'
#     home_page.open()
#
#     home_page.search(search_text)
#     search_page.sort_by_price_low_to_high()
#     search_page.check_items_sorted_by_price(sort='low_to_high')
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Поиск, фильтрация и сортировка")
# @allure.title("Сортировка по цене: по убыванию")
# def test_sort(driver):
#     home_page = HomePage(driver)
#     search_page = SearchPage(driver)
#
#     search_text = 'Torba'
#     home_page.open()
#
#     home_page.search(search_text)
#     search_page.sort_by_price_high_to_low()
#     search_page.check_items_sorted_by_price(sort='high_to_low')
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Поиск, фильтрация и сортировка")
# @allure.title("Фильтрация по бренду")
# def test_filter(driver):
#     home_page = HomePage(driver)
#     search_page = SearchPage(driver)
#
#     search_text = 'Torba'
#     filter_brand = 'adidas'
#     home_page.open()
#
#     home_page.search(search_text)
#     count = search_page.get_search_results_count()
#     search_page.filter_by_brand(filter_brand)
#     filtered_count = search_page.get_search_results_count()
#     assert count > filtered_count
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Навигация")
# @allure.title("Тест кнопки ""Наверх""")
# def test_go_to_top(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#
#     home_page.check_go_to_top()
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Рассылка")
# @allure.title("Тест подписки на рассылку: Успех")
# def test_newsletter(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#
#     home_page.scroll_to_newsletter()
#     home_page.subscribe_to_newsletter('Już prawie!')
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Рассылка")
# @allure.title("Тест подписки на рассылку: Без email")
# def test_newsletter_without_email(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#
#     home_page.scroll_to_newsletter()
#     home_page.subscribe_to_newsletter_without_email()
#
#
# @pytest.mark.presentation
# @pytest.mark.non_multiple_CPUs_run
# @allure.suite("Рассылка")
# @allure.title("Тест подписки на рассылку: Без категории")
# def test_newsletter_without_category(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#
#     home_page.scroll_to_newsletter()
#     home_page.subscribe_to_newsletter_without_category()