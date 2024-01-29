import time
import pytest
import allure
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.header import Header
from pages.profile_page import ProfilePage
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
    header.check_catalog()
    header.check_brands()
    header.check_novelties()
    header.check_stocks()
    header.check_clients_days()
    header.check_stores()
    header.check_gift_cards()
    header.check_sales()
    header.check_liked()
    header.check_basket()
    time.sleep(3)


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Профиль")
@allure.title("Проверка Профиля")
def test_profile_page(driver):
    profile = ProfilePage(driver)
    profile.check_profile_button()
    profile.change_profile_name()
    time.sleep(3)


@pytest.mark.presentation
@pytest.mark.non_multiple_CPUs_run
@allure.suite("Поиск")
@allure.title("Проверка поиска")
def test_search_page(driver):
    search = SearchPage(driver)
    search.check_search_button()
    search.find_product()
    search.check_filters()
    search.add_in_liked()
    time.sleep(3)
