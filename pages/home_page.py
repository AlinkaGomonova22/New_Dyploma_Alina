import platform
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import home_page_locators, choose_city_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://goldapple.by/')
            time.sleep(3)
            self.accept_cookies()

    def accept_cookies(self):
        pass

    def confirm_city(self):
        with allure.step("Нажать на кнопку Да,верно (подтвердить город) "):
            self.i(choose_city_locators.confirm_city_minsk_button).click()
            time.sleep(2)

    def check_stories_visible(self):
        with allure.step("Проверка отображения стторисов"):
            self.is_element_visible(home_page_locators.stock_stories_button).is_displayed()
            self.is_element_visible(home_page_locators.for_me_stories_button).is_displayed()
            self.is_element_visible(home_page_locators.life_stories_button).is_displayed()
            self.is_element_visible(home_page_locators.hits_stories_button).is_displayed()
            self.is_element_visible(home_page_locators.rad_stories_button).is_displayed()
            self.is_element_visible(home_page_locators.darling_stories_button).is_displayed()
            self.is_element_visible(home_page_locators.news_stories_button).is_displayed()
            time.sleep(1)
    #
    # def scroll_to_bottom(self):
    #     with allure.step("Пролистать до низа страницы"):
    #         self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
    #         time.sleep(1)
    #
    # def scroll_to_newsletter(self):
    #     with allure.step("Пролистать до подписки на новости"):
    #         self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
    #         time.sleep(2)
    #
    # def get_vertical_offset(self):
    #     with allure.step("Получить вертикальный сдвиг"):
    #         return self.driver.execute_script("return window.pageYOffset;")
    #
    # def search(self, text):
    #     with allure.step("Нажать на кнопку поиска"):
    #         self.find_element(home_page_locators.search_input).click()
    #         time.sleep(1)
    #     with allure.step("Очистить поле поиска"):
    #         try:
    #             self.find_element(home_page_locators.search_input_clear_button).click()
    #         except NoSuchElementException:
    #             pass
    #         time.sleep(1)
    #     with allure.step("Ввести в поисковую строку"):
    #         self.find_element(home_page_locators.search_input).send_keys(text)
    #         time.sleep(1)
    #     with allure.step("Подтвердить поиск нажав на клавишу Enter"):
    #         self.find_element(home_page_locators.search_input).send_keys(Keys.ENTER)
    #         time.sleep(1)
    #
    # def go_to_login_window(self):
    #     with allure.step("Нажать кнопку войти на главном экране"):
    #         actions = ActionChains(self.driver)
    #         time.sleep(1)
    #         login_icon = self.find_element(autorization_page_locators.picture_authorization)
    #         actions.move_to_element(login_icon).perform()
    #         time.sleep(1)
    #
    # def go_to_login_screen(self):
    #     with allure.step("Перейти на страницу авторизации"):
    #         self.go_to_login_window()
    #         self.find_element(autorization_page_locators.picture_authorization).click()
    #         time.sleep(1)
    #
    # def go_to_registration_screen(self):
    #     with allure.step("Перейти на страницу регистрации"):
    #         self.go_to_login_window()
    #         self.find_element(autorization_page_locators.log_in_in_window).click()
    #         time.sleep(1)
    #
    # def go_to_favourites(self):
    #     with allure.step("Нажать кнопку избранных товаров"):
    #         self.find_element(home_page_locators.button_favorites).click()
    #     with allure.step("Нажать кнопку всех избранных товаров"):
    #         self.find_element(home_page_locators.all_favorites).click()
    #
    # def add_item_to_cart(self):
    #     with allure.step("Нажать кнопку товара из раздела спорт"):
    #         button_sport_all = self.find_element(home_page_locators.button_sport_all)
    #         button_sport_all.click()
    #     time.sleep(1)
    #
    #     title = self.find_element(
    #         clothes_page_locators.first_element_title
    #     ).text
    #
    #     with allure.step("Перейти на страницу товара"):
    #         self.find_element(clothes_page_locators.first_element_card).click()
    #         time.sleep(1)
    #     with allure.step("Выбрать размер"):
    #         self.find_element(clothes_page_locators.item_select_size).click()
    #         time.sleep(1)
    #         self.find_element(clothes_page_locators.item_select_first_size).click()
    #         time.sleep(1)
    #     with allure.step("Нажать кнопку добавить в корзину"):
    #         self.find_element(clothes_page_locators.add_to_cart_button).click()
    #         time.sleep(1)
    #
    #     return title
    #
    # def check_is_in_favourites(self, item_that_was_added_title, item_that_was_added_description):
    #     with allure.step("Проверка наличия выбранных товаров"):
    #         item_in_favourites_title = \
    #             self.find_element(clothes_page_locators.first_element_title)
    #         item_in_favourites_description = \
    #             self.find_element(clothes_page_locators.first_element_title)
    #
    #         assert item_that_was_added_title == item_in_favourites_title.text
    #         assert item_that_was_added_description == item_in_favourites_description.text
    #
    # def check_go_to_top(self):
    #     self.scroll_to_bottom()
    #     with allure.step("Проверка наличия кнопки верх"):
    #         assert self.find_element(home_page_locators.top_button).is_displayed()
    #     with allure.step("Проверка вертикального сдвига"):
    #         assert self.get_vertical_offset() > 0
    #     with allure.step("Нажать на кнопку вверх"):
    #         self.go_to_top()
    #     with allure.step("Проверка отсутствия вертикального сдвига"):
    #         assert self.get_vertical_offset() == 0
    #
    # def subscribe_to_newsletter_without_email(self):
    #     with allure.step("Выбрать категорию подписки"):
    #         self.find_element(home_page_locators.newsletter_women_category).click()
    #         time.sleep(1)
    #     with allure.step("Нажать на кнопку подписаться"):
    #         self.find_element(home_page_locators.newsletter_submit).click()
    #         time.sleep(2)
    #     with allure.step("Проверить наличие ошибки отсутствия email"):
    #         assert self.find_element(home_page_locators.newsletter_error_no_email).is_displayed()
    #
    # def subscribe_to_newsletter_without_category(self):
    #     with allure.step("Ввести email"):
    #         self.find_element(home_page_locators.newsletter_email_input).send_keys(
    #             self.driver.credentials.get('email'))
    #         time.sleep(1)
    #     with allure.step("Нажать на кнопку подписаться"):
    #         self.find_element(home_page_locators.newsletter_submit).click()
    #         time.sleep(2)
    #     with allure.step("Проверить наличие ошибки отсутствия категории"):
    #         assert self.find_element(home_page_locators.newsletter_error_no_category).is_displayed()
    #
    # def subscribe_to_newsletter(self, success_label):
    #     with allure.step("Ввести email"):
    #         self.find_element(home_page_locators.newsletter_email_input).send_keys(
    #             self.driver.credentials.get('email'))
    #         time.sleep(1)
    #     with allure.step("Выбрать категорию подписки"):
    #         self.find_element(home_page_locators.newsletter_women_category).click()
    #         time.sleep(1)
    #     with allure.step("Нажать на кнопку подписаться"):
    #         self.find_element(home_page_locators.newsletter_submit).click()
    #         time.sleep(3)
    #     success_text = self.find_element(home_page_locators.newsletter_success)
    #     with allure.step("Проверить наличие подтверждения подписки"):
    #         assert success_text.is_displayed()
    #         assert success_text.text == success_label
    def accept_cookies(self):
        pass
