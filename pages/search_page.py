import time

import allure
from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.locators import header_locators, search_page_locators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_search_results_count(self):
        with allure.step("Проверить, что количество результатов больше нуля"):
            count = self.get_search_results_count()
            assert count > 0

    def check_search_texts_are_equal(self):
        with allure.step("Проверить, текст поиска в поле поиска и в заголовке страницы совпадают"):
            first_text = self.find_element(home_page_locators.search_input).get_attribute('value')
            second_text = self.find_element(search_page_locators.search_title).text.replace("‘", "").replace("’",
                                                                                                             "")
            assert first_text == second_text

    def check_nothing_found(self):
        try_again_text = 'Spróbuj wpisać coś innego lub sprawdź pisownię.'
        with allure.step("Проверить, что нет никаких результатов"):
            assert self.is_element_present(search_page_locators.nothing_found)
            assert self.find_element(search_page_locators.try_search_again).text == try_again_text

    def check_items_sorted_by_price(self, sort):
        with allure.step("Проверить, что список найден"):
            assert self.is_element_present(search_page_locators.search_results_grid)
        with allure.step("Проверить, что цены отсортированы по возрастанию"):
            grid = self.find_elements(search_page_locators.search_results_grid)
            assert len(grid) > 0

            prices = self.find_elements(search_page_locators.search_results_prices)

            for i in range(len(prices) - 1):
                price_current = self.convert_price_text_to_number(prices[i].text)
                price_next = self.convert_price_text_to_number(prices[i + 1].text)
                if sort == 'low_to_high':
                    assert price_current <= price_next
                elif sort == 'high_to_low':
                    assert price_current >= price_next

    def get_search_results_count(self):
        with allure.step("Получить количество результатов поиска"):
            text = self.find_element(search_page_locators.results_count).text
            count = float(text.replace("Liczba produktów: ", "").replace(" ", ""))
        return count

    def sort_by_price_low_to_high(self):
        with allure.step("Нажать на выбор сортировки"):
            self.find_element(search_page_locators.sort).click()
            time.sleep(1)
        with allure.step("Выбрать сортировку по цене по возрастанию"):
            self.find_element(search_page_locators.sort_by_price_low_to_high).click()
            time.sleep(2)

    def sort_by_price_high_to_low(self):
        with allure.step("Нажать на выбор сортировки"):
            self.find_element(search_page_locators.sort).click()
            time.sleep(1)
        with allure.step("Выбрать сортировку по цене по возрастанию"):
            self.find_element(search_page_locators.sort_by_price_high_to_low).click()
            time.sleep(2)

    def filter_by_brand(self, brand):
        with allure.step("Нажать на поле фильтрации по бренду"):
            self.find_element(search_page_locators.brand_filter).click()
            time.sleep(1)
        with allure.step("Нажать на поле ввода бренда для поиска"):
            self.find_element(search_page_locators.brand_filter_search).click()
            time.sleep(1)
        with allure.step("Ввести бренд для поиска"):
            self.find_element(search_page_locators.brand_filter_search_input).send_keys(brand)
            time.sleep(1)
        with allure.step("Нажать на кнопку поиска"):
            self.find_element(search_page_locators.brand_filter_search_input).send_keys(Keys.ENTER)
            time.sleep(1)
        with allure.step("Нажать на первый результат (бренд)"):
            self.find_element(search_page_locators.brand_filter_search_first_result).click()
            time.sleep(1)
        with allure.step("Нажать на кнопку подтверждения поиска по бренду"):
            self.find_element(search_page_locators.brand_filter_search_submit).click()
            time.sleep(2)