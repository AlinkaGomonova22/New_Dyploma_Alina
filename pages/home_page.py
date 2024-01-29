
import time
import allure
from pages.base_page import BasePage
from pages.locators import home_page_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://goldapple.by/')
            time.sleep(3)
            self.accept_cookies()

    def check_stories_visible(self):
        with allure.step("Проверка отображения стторисов"):
            self.find_element(home_page_locators.stock_stories_button).is_displayed()
            self.find_element(home_page_locators.for_me_stories_button).is_displayed()
            self.find_element(home_page_locators.life_stories_button).is_displayed()
            self.find_element(home_page_locators.hits_stories_button).is_displayed()
            self.find_element(home_page_locators.rad_stories_button).is_displayed()
            self.find_element(home_page_locators.darling_stories_button).is_displayed()
            self.find_element(home_page_locators.news_stories_button).is_displayed()
            time.sleep(2)

    def click_stories(self):
        with allure.step("Нажатие на сторис Акции"):
            self.find_element(home_page_locators.stock_stories_button).click()
            time.sleep(1)
        with allure.step("Проверка отображаения контента"):
            self.find_element(home_page_locators.stock_stories_content).is_displayed()
            self.find_element(home_page_locators.stock_stories_content).click()
            self.find_element(home_page_locators.stock_stories_content).click()
        with allure.step("Проверка отображаения контента For me"):
            self.find_element(home_page_locators.for_me_stories_content).is_displayed()
            self.find_element(home_page_locators.stock_stories_content).click()
            self.find_element(home_page_locators.close_stories_button).click()

    def accept_cookies(self):
        pass
