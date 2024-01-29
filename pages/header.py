import platform
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import home_page_locators, choose_city_locators


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://goldapple.by/')
            time.sleep(3)
            self.accept_cookies()

    def search(self, text):
        with allure.step("Нажать на кнопку поиска"):
            self.find_element().click()
            time.sleep(1)
        with allure.step("Очистить поле поиска"):
            try:
                self.find_element(home_page_locators.search_input_clear_button).click()
            except NoSuchElementException:
                pass
            time.sleep(1)
        with allure.step("Ввести в поисковую строку"):
            self.find_element(home_page_locators.search_input).send_keys(text)
            time.sleep(1)
        with allure.step("Подтвердить поиск нажав на клавишу Enter"):
            self.find_element(home_page_locators.search_input).send_keys(Keys.ENTER)
            time.sleep(1)