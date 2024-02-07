import time
import pytest
import allure
from pages.home_page import HomePage
from pages.header import Header
from pages.search_page import SearchPage


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Домашняя страница")
@allure.title("Проверка сторисов")
def test_stories(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.check_stories_visible()
    home_page.click_stories()
    time.sleep(3)


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Header")
@allure.title("Проверка Header")
def test_header_buttons(driver):
    header = Header(driver)
    home_page = HomePage(driver)
    home_page.open()
    header.check_brands()
    header.check_stocks()
    header.check_clients_days()
    header.check_sales()
    time.sleep(3)


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Поиск")
@allure.title("Проверка поиска")
def test_search_page(driver):
    search = SearchPage(driver)
    home_page = HomePage(driver)
    home_page.open()
    search.check_search_button()
    search.find_product()
    search.check_filters()
    search.add_in_liked()
    search.check_goods()
    time.sleep(3)
