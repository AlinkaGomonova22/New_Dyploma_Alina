import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import search_page_locators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_search_button(self):
        with allure.step("Проверка кнопки поиска"):
            self.find_element(search_page_locators.search_button).is_displayed()
        with allure.step("Нажать на кнопку поиска"):
            self.find_element(search_page_locators.search_button).click()
            time.sleep(2)

    def find_product(self):
        # with allure.step("Ввести в строку текст"):
        #     self.find_element(search_page_locators.search_field).click()
        #     time.sleep(2)
        with allure.step("Ввести в строку текст"):
            self.find_element(search_page_locators.search_field).send_keys('kiki')
            time.sleep(2)
        with allure.step("Нажать на кики"):
            self.find_element(search_page_locators.kiki_button).click()
            time.sleep(2)
        with allure.step("проверка отображения результата"):
            self.find_element(search_page_locators.result_text).is_displayed()

    def check_filters(self):
        with allure.step("Нажать на кнопку фильтр"):
            self.find_element(search_page_locators.filters_button).click()
            time.sleep(2)
        with allure.step("нажать плюс категорию"):
            self.find_element(search_page_locators.plus_category_button).click()
            time.sleep(2)
        with allure.step("нажать плюс макияж"):
            self.find_element(search_page_locators.plus_makeup_button).click()
            time.sleep(2)
        with allure.step("нажать на чекбокс глаза"):
            self.find_element(search_page_locators.eyes_checkbox).click()
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
        with allure.step("Закрыть станицу входа"):
            self.find_element(search_page_locators.close_enter_section).click()

    def check_goods(self):
        with allure.step("Нажать на товар"):
            self.find_element(search_page_locators.click_on_good).click()
            time.sleep(2)
        with allure.step("Проверить отображение"):
            self.find_element(search_page_locators.text_of_good).is_displayed()
