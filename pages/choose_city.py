import platform
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import header_locators, choose_city_locators


class ChooseCity(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_city_button(self):
        with allure.step("Проверка отображения кнопки выбора города"):
            self.find_element(choose_city_locators.choose_city_button).is_displayed()

    def click_on_city_button(self):
        with allure.step("Проверка отображения кнопки выбора города"):
            self.find_element(choose_city_locators.choose_city_button).click()
            time.sleep(1)

    def auto_(self):
        self.find_element(choose_city_locators.find_city_input).is_displayed()
        self.find_element()
        # self.find_element(autorization_page_locators.name).send_keys(self.driver.credentials.get('firstName'))
        # time.sleep(1)
        # self.find_element(autorization_page_locators.surname).click()
        # self.find_element(autorization_page_locators.surname).send_keys(self.driver.credentials.get('lastName'))
        # time.sleep(1)
        # self.find_element(autorization_page_locators.e_mail_address_first).click()
        # self.find_element(autorization_page_locators.e_mail_address_first).send_keys(
        #     self.driver.credentials.get('email'))
        # time.sleep(1)
        # self.find_element(autorization_page_locators.password_first).click()
        # self.find_element(autorization_page_locators.password_first).send_keys(self.driver.credentials.get('password'))
        # time.sleep(1)
        # self.find_element(home_page_locators.agree_rules).click()
        # time.sleep(1)
        # self.find_element(home_page_locators.button_register).click()
        # time.sleep(1)