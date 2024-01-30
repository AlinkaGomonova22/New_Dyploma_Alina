from selenium.webdriver.common.by import By

catalog_button = (By.XPATH, '//li[@class="ogg-menu__item ogg-menu__item_parent"]')

brands_button = (By.XPATH, '(//li[@class="ogg-menu__item ogg-menu__item_parent   "])[2]')

novelty_button = (By.XPATH, '(//li[@class="ogg-menu__item ogg-menu__item_parent   "])[3]')

stocks_button = (By.XPATH, '(//li[@class="ogg-menu__item ogg-menu__item_parent   "])[4]')

clients_days_button = (By.XPATH, '(//li[@class="ogg-menu__item ogg-menu__item_parent   "])[5]')

stores_button = (By.XPATH, '//li[@class="ogg-menu__item ogg-menu__item_parent  _mobile-excluded "]')

gift_cards_button = (By.XPATH, '(//li[@class="ogg-menu__item ogg-menu__item_parent   "])[6]')

sales_under_40 = (By.XPATH, '//li[@class="ogg-menu__item ogg-menu__item_parent   _custom-color"]')

search_button = (By.XPATH, '//button[@class="header-tab-button header-tab-button_search"]')

liked_button = (By.XPATH, '//div[@data-role="header-tab-wishlist"]')

profile_button = (By.XPATH, '//button[@class="header-tab-button header-tab-button_customer"]')

basket_button = (By.XPATH, '//button[@class="header-tab-button header-tab-button_minicart"]')

logo_button = (By.XPATH, '//span[@class="header-tab-button header-tab-button_logo"]')

liked_text = (By.XPATH, '//h1[@class="E+FsI"]')

basket_text = (By.XPATH, '//span[@class="ehlvF"]')

find_brand_text = (By.XPATH, '//input[@placeholder="найти бренд"]')

novelty_text = (By.XPATH, '//div[@class="LCdDN"]')

stocks_text = (By.XPATH, '//h1[@class="m-h2 t-h1"]')

clients_days_text = (By.XPATH, '//h1[@class="m-h2 t-h1"]')

stores_text = (By.XPATH, '//h1[@class="I5iUR"]')

gift_card_text = (By.XPATH,'//nav[@class="A-ue7"]')

sales_under_40_text = (By.XPATH, '//span[@class="jH3N7"]')

close_basket_button = (By.XPATH, '//button[@class="h8lFg _4kl7v oL8O0 KNpCU ONl5c"]')
