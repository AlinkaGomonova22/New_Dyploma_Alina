from selenium.webdriver.common.by import By

confirm_city_minsk_button = (
    By.XPATH, '//button[@class="button-primary modal-city-informer__btn modal-city-informer__btn_primary"]')

choose_city_button = (
    By.XPATH, 'class="header-tab-button header-tab-button_city"')

find_city_input = (By.XPATH, '//input[@class="city-selector__input"]')

gomel_displayed = (By.XPATH, '//li[@class="city-selector__item link _select"]')

dysplayed_on_header_chosen_city = (By.XPATH, '(//div[@class="header-city__city"])[1]')

brest_button = (By.XPATH, '(//span[@class="city-selector__city"])[3]')

select_country_field = (By.XPATH, '//input[@class="select-field__view-button"]')

russia_country = (By.XPATH, '(//span[@class="select-field__option-main"])[2]')

kazahstan_country = (By.XPATH, '(//span[@class="select-field__option-main"])[3]')

geolocation_button = (By.XPATH, '(//div[@class="city-selector__geo-arrow"])[2]')

text_confirm_in_minsk = (By.XPATH, '//p[@class="paragraph-1 city-by-geo__description"]')

yes_button = (By.XPATH, '//button[@class="button-primary city-by-geo__btn city-by-geo__btn_primary"]')

text_minsk = (By.XPATH, '(//div[@class="header-city__city"])[1]')
