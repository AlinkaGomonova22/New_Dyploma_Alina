import time

import allure


from pages.base_page import BasePage
from pages.locators import header_locators, search_page_locators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_search_button(self):
        with allure.step("Проверка кнопки поиска"):
            self.find_element(header_locators.search_button).is_displayed()
        with allure.step("Нажать на кнопку поиска"):
            self.find_element(header_locators.search_button).click()
            time.sleep(2)

    def find_product(self):
        with allure.step("Ввести в строку текст"):
            self.find_element(search_page_locators.search_field).send_keys("kiki")
            time.sleep(2)
        with allure.step("проверка отображения результата"):
            self.find_element(search_page_locators.result_text).is_displayed()

    def check_filters(self):
        with allure.step("Нажать на кнопку фильтр"):
            self.find_element(search_page_locators.filters_button).click()
            time.sleep(2)
        with allure.step("выбрать в наличии"):
            self.find_element(search_page_locators.in_stock_checkbox).click()
            time.sleep(2)
        with allure.step("выбрать со скидкой"):
            self.find_element(search_page_locators.with_sale_checkbox).click()
            time.sleep(2)
        with allure.step("нажать показать товар"):
            self.find_element(search_page_locators.show_goods).click()
            time.sleep(2)
        with allure.step("проверка отображения результата"):
            self.find_element(search_page_locators.result_text).is_displayed()

    def add_in_liked(self):
        with allure.step("Нажать на кнопку лайк"):
            self.find_element(search_page_locators.ad_in_liked_button).click()
            time.sleep(2)
        with allure.step("Проверка уведомления"):
            self.find_element(search_page_locators.notification).is_displayed()
