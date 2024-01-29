import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import header_locators, profile_page_locators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_profile_button(self):
        with allure.step("Проверить кнопку профиля"):
            self.find_element(header_locators.profile_button).is_displayed()
        with allure.step("Нажать кропку профиль"):
            self.find_element(header_locators.profile_button).click()

    def change_profile_name(self):
        with allure.step("Нажать на кнопку перейти в профиль"):
            self.find_element(profile_page_locators.three_points_button).click()
            time.sleep(2)
        with allure.step("Проверить отображение текста"):
            self.find_element(profile_page_locators.my_profile_text).is_displayed()
        with allure.step("Нажать на поле Имя"):
            self.find_element(profile_page_locators.firstname_input).click()
            time.sleep(2)
        with allure.step("Удалить старое имя"):
            self.find_element(profile_page_locators.firstname_input).clear()
            time.sleep(1)
        with allure.step("Удалить старое имя"):
            self.find_element(profile_page_locators.firstname_input).send_keys('Алинка')
            time.sleep(2)
        with allure.step("Пролистать страницу вниз"):
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
            time.sleep(2)
        with allure.step("Нажать на кнопку сохранить"):
            self.find_element(profile_page_locators.save_button).click()
            time.sleep(2)
        with allure.step("Удалить старое имя"):
            self.find_element(profile_page_locators.firstname_text).is_displayed()
