
import time
import allure
from pages.base_page import BasePage
from pages.locators import home_page_locators, header_locators


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_catalog(self):
        with allure.step("Проверка отображения кнопки каталог"):
            self.find_element(header_locators.catalog_button).is_displayed()
        with allure.step("Нажатие на кнопку каталог"):
            self.find_element(header_locators.catalog_button).click()
            time.sleep(2)

    def check_brands(self):
        with allure.step("Проверка отображения кнопки брэнды"):
            self.find_element(header_locators.brands_button).is_displayed()
        with allure.step("Нажатие на кнопку брэнды"):
            self.find_element(header_locators.brands_button).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста найти брэнд"):
            self.find_element(header_locators.find_brand_text).is_displayed()

    def check_novelties(self):
        with allure.step("Проверка отображения кнопки новинки"):
            self.find_element(header_locators.novelty_button).is_displayed()
        with allure.step("Нажатие на кнопку новинки"):
            self.find_element(header_locators.novelty_button).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста новинки"):
            self.find_element(header_locators.novelty_text).is_displayed()

    def check_stocks(self):
        with allure.step("Проверка отображения кнопки акции"):
            self.find_element(header_locators.stocks_button).is_displayed()
        with allure.step("Нажатие на кнопку акции"):
            self.find_element(header_locators.stocks_button).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста акции"):
            self.find_element(header_locators.stocks_text).is_displayed()

    def check_clients_days(self):
        with allure.step("Проверка отображения кнопки клиентские дни"):
            self.find_element(header_locators.clients_days_button).is_displayed()
        with allure.step("Нажатие на кнопку клиентские дни"):
            self.find_element(header_locators.clients_days_button).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста клиентсике дни"):
            self.find_element(header_locators.clients_days_text).is_displayed()

    def check_stores(self):
        with allure.step("Проверка отображения кнопки магазины"):
            self.find_element(header_locators.stores_button).is_displayed()
        with allure.step("Нажатие на кнопку магазины"):
            self.find_element(header_locators.stores_button).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста магазины"):
            self.find_element(header_locators.stores_text).is_displayed()

    def check_gift_cards(self):
        with allure.step("Проверка отображения кнопки подарочные карты"):
            self.find_element(header_locators.gift_cards_button).is_displayed()
        with allure.step("Нажатие на кнопку подарочные карты"):
            self.find_element(header_locators.gift_cards_button).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста подарочные карты"):
            time.sleep(3)
            self.find_element(header_locators.gift_card_text).is_displayed()
        with allure.step("Вернуться на главную страницу"):
            self.find_element(home_page_locators.logo_button).click()
            time.sleep(1)

    def check_sales(self):
        with allure.step("Проверка отображения кнопки скидки до 40%"):
            self.find_element(header_locators.sales_under_40).is_displayed()
        with allure.step("Нажатие на кнопку скидки до 40%"):
            self.find_element(header_locators.sales_under_40).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста скидки до 40%"):
            self.find_element(header_locators.sales_under_40_text).is_displayed()

    def check_liked(self):
        with allure.step("Проверка отображения кнопки избранное"):
            self.find_element(header_locators.liked_text).is_displayed()
        with allure.step("Нажатие на кнопку избранное"):
            self.find_element(header_locators.liked_text).click()
            time.sleep(2)
        with allure.step("Проверка отображения текста избранное"):
            self.find_element(header_locators.liked_text).is_displayed()

    def check_basket(self):
        with allure.step("Проверка отображения кнопки корзина"):
            self.find_element(header_locators.basket_button).is_displayed()
        with allure.step("Нажатие на кнопку корзина"):
            self.find_element(header_locators.basket_button).click()
            time.sleep(5)
        with allure.step("Проверка отображения текста корзина"):
            self.find_element(header_locators.basket_text).is_displayed()
        with allure.step("Закрыть корзину"):
            self.find_element(header_locators.close_basket_button).click()
