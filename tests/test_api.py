import requests
import allure
import pytest_check as check
import time
import json


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода GET")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "alina gomonova")
@allure.link("https://goldapple.by/", name="Gold Apple")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_1():

    url = "https://goldapple.by/front/api/user/info/full"

    payload = {}
    headers = {
        'authority': 'goldapple.by',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'store=by; _userGUID=0:lplg9m3b:g7toFOrFPk~fUlCuKKdxEEUMo4v28uSM; is-accepted-cookies=true; mindboxDeviceUUID=872fbc6f-caa0-41da-8c2f-7595b4abe4bb; directCrm-session=%7B%22deviceGuid%22%3A%22872fbc6f-caa0-41da-8c2f-7595b4abe4bb%22%7D; tmr_lvid=5b43564671e43cd29a2b7f1bf2f13610; tmr_lvidTS=1701367627349; _ym_uid=1701367628616240021; _ym_d=1701367628; _fbp=fb.1.1701367627781.1555915512; adrcid=AKjmRG1d3W8rCbuioYrT4vQ; ga-lang=ru; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9bc0acbe-950a-43df-a2f4-0ca18905e26a; opened_cart_route=https%253A%252F%252Fgoldapple.by%252Fclientday; form_key=qto3iiEHu3zdzxsk; userId=7373591; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IkE4QTdDRDBFNjE0REQxNzE1OTU0ODZCNjA5MjNDMTBCRDYyMDZGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InFLZk5EbUZOMFhGWlZJYTJDU1BCQzlZZ2J4USJ9.eyJuYmYiOjE3MDU1OTU4OTYsImV4cCI6MTczNzEzMTg5NiwiaXNzIjoiaHR0cHM6Ly9wbGFpZC5nb2xkYXBwbGUuYnkiLCJhdWQiOiJJbnRlcm5hbEFQSSIsImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJzdWIiOiIzNzU0NDU5MjQyNzYiLCJhdXRoX3RpbWUiOjE3MDU1OTU4OTYsImlkcCI6InBob25lX2NhbGxfdG9rZW4iLCJtYWdlbnRvX2lkIjoiNzM3MzU5MSIsImN1c3RvbWVyX2lkIjoiMGEzOWU3M2EtNmI2Mi00NWM5LTg3MTctOTc0YjA3ZDYzZDBlIiwiY3VzdG9tZXJfcGhvbmUiOiIzNzU0NDU5MjQyNzYiLCJjdXN0b21lcl9pc19yZWdpc3RlcmVkIjoiMSIsImN1c3RvbWVyX2dyb3VwX2lkIjoiNiIsImp0aSI6IjFFNjRERDIyRTMyOTVCM0EyMjFBMTA1MkI0QkJFOEI1IiwiaWF0IjoxNzA1NTk1ODk2LCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiV2ViQVBJIiwib2ZmbGluZV9hY2Nlc3MiXX0.s-xhD1j5ZENT45TkAmlek4SV4dGCzL11j4pBO5AL-eh5LhBaY7KWUodvdiDA-dMUThXFZ94AkvScs6eq0r-HuR_3pm3Ss4lI43R29SI5rY2wCYQJ0vUQaVvSYN4n7X6pwHvpomJAS3BSYWAbvrBMFfdrlazc03oHI4VLfhodqjSYknHS93jzvVGOYRksi2YZM6I1Vzbe_hHZwr-AMRz03TEz1Rajiu66DvIloaaol7Gpt-mvoeQc47gGTnVMWs0vsUCexCa3p1JWGfMbSMX8cXENrhdUn0E9Y3-VpKUYDvQFxq5H--iirN0S3etsh1N-R9p9PZO_BrnQbCKEBw6dnupBh61-RwIHYWn8H-lkI5HBFceZvDhsoSTfHSYISsQTEY0vlqsTwjN7Gh23tSLEtOAflD1R-GvB6Sw37xgKvuKkmbTJoCE7YEzOuTtC6M1QVNSGgRxbzoHs2rJ-8ARqOkcRQFmPFx1yWZjVCbCGwufv4Mo8JJtnRsMrpPyjf5m3tLYBo2it3GspvcYoxKPGuajeYg6SIzCAKm1WLFXc3NDb7_OmK7gXiK48eFoIOtDqSoJpNih9JvtgGZkjEW7lKQOQSAGQ0L1vdtQSdRu8MeIWGb6xaOHiC5gtYf6SXG8KGYM-brW3v16g9fpqZoLUArXcR7Sv9Etf7QgqEhwVotw; has_access_token=true; refresh_token=4ECCD8BBBE2C2685726FEFBE3B8760BE000588443D66C992050E296D7081DCC8; has_refresh_token=true; X-Magento-Vary=5a01dc66ae84d635861677306cce28738ee73de0; PHPSESSID=be86a350e06e32e356afbc98244c0f7b; mage-messages=; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; client-store-code=by; mage-cache-sessid=true; private_content_version=need_version; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gid=GA1.2.972053435.1705997252; _ym_isad=2; ga-location-city-id=relation%3A59195; DIGI_CARTID=49542864; digi-analytics-sessionId=-Ua8uloquVfIAXKfo03TB; _gat_UA-31209334-1=1; dSesn=8a1f1551-a7c8-d3a8-3d53-72ed6c2fa45e; _dvs=0:lrq4kiym:4VY5ggXnw1ywtpWrFjPROf9NGgK1VXfi; cto_bundle=C2w2OV8ybkd6V2FpNWM5OGJFbEVVM3g0T3o1M25PaFA4V2djS0xzdExiSlYzcXlIOE9pcWxKSTNOVGdLeHNjbm1JRTZvZFNYTEglMkJyN0dyNSUyQmlwT1o0dUxXZHl2TUNLUWVUZHVuMzFTTVZnRDhpYXJld2N1MkdMdjBMOE9pdUhUbHM0WUdraUpkdGtXWFh2Z0NmMXJrQjJXYVVNOTVYZzJ2ZXgyNUlHa09LUjV2OW1LTXJqVEZvNlRnS3FuaG5zWTJDQWNLT1JSd3BPNUdwRllKZnZOJTJCNWFwZE13JTNEJTNE; _spx=eyJpZCI6ImFjOGFhYWY1LThhNGUtNDYyNi05YjI1LWYyMzBkNDczY2IxZSIsImZpeGVkIjp7InN0YWNrIjpbMCwtOTIyMjk3ODM3LDAsMCwwXX19; _ga=GA1.2.837300893.1701367627; tmr_detect=0%7C1706000374009; _ga_QE5MQ8XJJK=GS1.1.1706000341.10.1.1706000379.0.0.0; section_data_ids=%7B%22cart%22%3A1706000324%2C%22geolocation%22%3A1706000359%2C%22customer%22%3A1705997232%2C%22compare-products%22%3A1705997232%2C%22last-ordered-items%22%3A1705997232%2C%22directory-data%22%3A1705997233%2C%22captcha%22%3A1705997232%2C%22wishlist%22%3A1705997232%2C%22multiplewishlist%22%3A1705997232%2C%22goldcards%22%3A1705997232%2C%22adult_goods%22%3A1706000324%2C%22recently_viewed_product%22%3A1705997232%2C%22recently_compared_product%22%3A1705997232%2C%22product_data_storage%22%3A1705997232%7D',
        'referer': 'https://goldapple.by/customer/account/orders',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-1946d031d6e08bc5196f2bc66fa1b6c5-b59ae4d3ee5453ce-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)
    print(response.request.method)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200)

    with allure.step('Проверка метода'):
        check.equal(response.request.method, 'GET')

    with allure.step('Проверка значений Firstname и phone'):
        response_phone = response.json()
        for phone in response_phone:
            if 'phone' in [phone] == 375445924276:
                pass
            else:
                print("не тот номер")

    with allure.step('Проверка значений Firstname и phone'):
        response_firstName = response.json()
        for firstName in response_firstName:
            if 'Name' in firstName == "Alina":
                pass
            else:
                print("не то Name")


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода Post")
@allure.tag("API", "Post")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "alina gomonova")
@allure.link("https://goldapple.by/", name="Gold Apple")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_2():
    import requests
    import json

    url = "https://goldapple.by/front/api/cart/items"

    payload = json.dumps({
        "sku": "19760313784",
        "analyticsDetails": {
            "itemListName": "брендзона/3INA"
        }
    })
    headers = {
        'authority': 'goldapple.by',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'store=by; _userGUID=0:lplg9m3b:g7toFOrFPk~fUlCuKKdxEEUMo4v28uSM; is-accepted-cookies=true; mindboxDeviceUUID=872fbc6f-caa0-41da-8c2f-7595b4abe4bb; directCrm-session=%7B%22deviceGuid%22%3A%22872fbc6f-caa0-41da-8c2f-7595b4abe4bb%22%7D; tmr_lvid=5b43564671e43cd29a2b7f1bf2f13610; tmr_lvidTS=1701367627349; _ym_uid=1701367628616240021; _ym_d=1701367628; _fbp=fb.1.1701367627781.1555915512; adrcid=AKjmRG1d3W8rCbuioYrT4vQ; ga-lang=ru; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9bc0acbe-950a-43df-a2f4-0ca18905e26a; opened_cart_route=https%253A%252F%252Fgoldapple.by%252Fclientday; form_key=qto3iiEHu3zdzxsk; userId=7373591; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IkE4QTdDRDBFNjE0REQxNzE1OTU0ODZCNjA5MjNDMTBCRDYyMDZGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InFLZk5EbUZOMFhGWlZJYTJDU1BCQzlZZ2J4USJ9.eyJuYmYiOjE3MDU1OTU4OTYsImV4cCI6MTczNzEzMTg5NiwiaXNzIjoiaHR0cHM6Ly9wbGFpZC5nb2xkYXBwbGUuYnkiLCJhdWQiOiJJbnRlcm5hbEFQSSIsImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJzdWIiOiIzNzU0NDU5MjQyNzYiLCJhdXRoX3RpbWUiOjE3MDU1OTU4OTYsImlkcCI6InBob25lX2NhbGxfdG9rZW4iLCJtYWdlbnRvX2lkIjoiNzM3MzU5MSIsImN1c3RvbWVyX2lkIjoiMGEzOWU3M2EtNmI2Mi00NWM5LTg3MTctOTc0YjA3ZDYzZDBlIiwiY3VzdG9tZXJfcGhvbmUiOiIzNzU0NDU5MjQyNzYiLCJjdXN0b21lcl9pc19yZWdpc3RlcmVkIjoiMSIsImN1c3RvbWVyX2dyb3VwX2lkIjoiNiIsImp0aSI6IjFFNjRERDIyRTMyOTVCM0EyMjFBMTA1MkI0QkJFOEI1IiwiaWF0IjoxNzA1NTk1ODk2LCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiV2ViQVBJIiwib2ZmbGluZV9hY2Nlc3MiXX0.s-xhD1j5ZENT45TkAmlek4SV4dGCzL11j4pBO5AL-eh5LhBaY7KWUodvdiDA-dMUThXFZ94AkvScs6eq0r-HuR_3pm3Ss4lI43R29SI5rY2wCYQJ0vUQaVvSYN4n7X6pwHvpomJAS3BSYWAbvrBMFfdrlazc03oHI4VLfhodqjSYknHS93jzvVGOYRksi2YZM6I1Vzbe_hHZwr-AMRz03TEz1Rajiu66DvIloaaol7Gpt-mvoeQc47gGTnVMWs0vsUCexCa3p1JWGfMbSMX8cXENrhdUn0E9Y3-VpKUYDvQFxq5H--iirN0S3etsh1N-R9p9PZO_BrnQbCKEBw6dnupBh61-RwIHYWn8H-lkI5HBFceZvDhsoSTfHSYISsQTEY0vlqsTwjN7Gh23tSLEtOAflD1R-GvB6Sw37xgKvuKkmbTJoCE7YEzOuTtC6M1QVNSGgRxbzoHs2rJ-8ARqOkcRQFmPFx1yWZjVCbCGwufv4Mo8JJtnRsMrpPyjf5m3tLYBo2it3GspvcYoxKPGuajeYg6SIzCAKm1WLFXc3NDb7_OmK7gXiK48eFoIOtDqSoJpNih9JvtgGZkjEW7lKQOQSAGQ0L1vdtQSdRu8MeIWGb6xaOHiC5gtYf6SXG8KGYM-brW3v16g9fpqZoLUArXcR7Sv9Etf7QgqEhwVotw; has_access_token=true; refresh_token=4ECCD8BBBE2C2685726FEFBE3B8760BE000588443D66C992050E296D7081DCC8; has_refresh_token=true; X-Magento-Vary=5a01dc66ae84d635861677306cce28738ee73de0; PHPSESSID=be86a350e06e32e356afbc98244c0f7b; mage-messages=; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; client-store-code=by; mage-cache-sessid=true; private_content_version=need_version; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gid=GA1.2.972053435.1705997252; _ym_isad=2; ga-location-city-id=relation%3A59195; DIGI_CARTID=49542864; cto_bundle=C2w2OV8ybkd6V2FpNWM5OGJFbEVVM3g0T3o1M25PaFA4V2djS0xzdExiSlYzcXlIOE9pcWxKSTNOVGdLeHNjbm1JRTZvZFNYTEglMkJyN0dyNSUyQmlwT1o0dUxXZHl2TUNLUWVUZHVuMzFTTVZnRDhpYXJld2N1MkdMdjBMOE9pdUhUbHM0WUdraUpkdGtXWFh2Z0NmMXJrQjJXYVVNOTVYZzJ2ZXgyNUlHa09LUjV2OW1LTXJqVEZvNlRnS3FuaG5zWTJDQWNLT1JSd3BPNUdwRllKZnZOJTJCNWFwZE13JTNEJTNE; dSesn=8a945ef2-83b0-04e3-2610-3280f8f40150; _dvs=0:lrq6ink4:nAOKaNYSvLQ_jPrbU5bH6Nf_I65NL5eM; digi-analytics-sessionId=scn92kHRQYb2o5x5AmO0Z; _spx=eyJpZCI6ImFjOGFhYWY1LThhNGUtNDYyNi05YjI1LWYyMzBkNDczY2IxZSIsImZpeGVkIjp7InN0YWNrIjpbMCwwLC05MjIyOTc4MzcsMCwwXX19; _ga=GA1.2.837300893.1701367627; _ga_QE5MQ8XJJK=GS1.1.1706003636.11.1.1706003749.0.0.0; section_data_ids=%7B%22cart%22%3A1706003730%2C%22geolocation%22%3A1706003727%2C%22customer%22%3A1705997232%2C%22compare-products%22%3A1705997232%2C%22last-ordered-items%22%3A1705997232%2C%22directory-data%22%3A1705997233%2C%22captcha%22%3A1705997232%2C%22wishlist%22%3A1706003619%2C%22multiplewishlist%22%3A1705997232%2C%22goldcards%22%3A1705997232%2C%22adult_goods%22%3A1706003729%2C%22recently_viewed_product%22%3A1705997232%2C%22recently_compared_product%22%3A1705997232%2C%22product_data_storage%22%3A1705997232%7D; tmr_detect=0%7C1706003757050',
        'origin': 'https://goldapple.by',
        'referer': 'https://goldapple.by/brands/3ina',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-5115a79dd1f605ddfb842733af2c176f-a911e73e9854a876-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)
    print(response.request.method)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200)

    with allure.step('Проверка метода'):
        check.equal(response.request.method, 'POST')

    with allure.step('Проверка что значение параметра data не пустое'):
        response_data = response.json()
        if 'data' in response_data:
            print(response_data['data'])
            check.is_not_none(response_data['data'])
        else:
            print('Ошибка')

@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Пишем тесты для метода Put")
@allure.tag("API", "PUT")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "alina gomonova")
@allure.link("https://goldapple.by/", name="Gold Apple")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_3():
    import requests
    import json

    url = "https://goldapple.by/front/api/user/favorites/products"

    payload = json.dumps({
        "products": [
            "19000052772"
        ]
    })
    headers = {
        'authority': 'goldapple.by',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'store=by; _userGUID=0:lplg9m3b:g7toFOrFPk~fUlCuKKdxEEUMo4v28uSM; is-accepted-cookies=true; mindboxDeviceUUID=872fbc6f-caa0-41da-8c2f-7595b4abe4bb; directCrm-session=%7B%22deviceGuid%22%3A%22872fbc6f-caa0-41da-8c2f-7595b4abe4bb%22%7D; tmr_lvid=5b43564671e43cd29a2b7f1bf2f13610; tmr_lvidTS=1701367627349; _ym_uid=1701367628616240021; _ym_d=1701367628; _fbp=fb.1.1701367627781.1555915512; adrcid=AKjmRG1d3W8rCbuioYrT4vQ; ga-lang=ru; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=9bc0acbe-950a-43df-a2f4-0ca18905e26a; opened_cart_route=https%253A%252F%252Fgoldapple.by%252Fclientday; form_key=qto3iiEHu3zdzxsk; userId=7373591; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IkE4QTdDRDBFNjE0REQxNzE1OTU0ODZCNjA5MjNDMTBCRDYyMDZGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InFLZk5EbUZOMFhGWlZJYTJDU1BCQzlZZ2J4USJ9.eyJuYmYiOjE3MDU1OTU4OTYsImV4cCI6MTczNzEzMTg5NiwiaXNzIjoiaHR0cHM6Ly9wbGFpZC5nb2xkYXBwbGUuYnkiLCJhdWQiOiJJbnRlcm5hbEFQSSIsImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJzdWIiOiIzNzU0NDU5MjQyNzYiLCJhdXRoX3RpbWUiOjE3MDU1OTU4OTYsImlkcCI6InBob25lX2NhbGxfdG9rZW4iLCJtYWdlbnRvX2lkIjoiNzM3MzU5MSIsImN1c3RvbWVyX2lkIjoiMGEzOWU3M2EtNmI2Mi00NWM5LTg3MTctOTc0YjA3ZDYzZDBlIiwiY3VzdG9tZXJfcGhvbmUiOiIzNzU0NDU5MjQyNzYiLCJjdXN0b21lcl9pc19yZWdpc3RlcmVkIjoiMSIsImN1c3RvbWVyX2dyb3VwX2lkIjoiNiIsImp0aSI6IjFFNjRERDIyRTMyOTVCM0EyMjFBMTA1MkI0QkJFOEI1IiwiaWF0IjoxNzA1NTk1ODk2LCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiV2ViQVBJIiwib2ZmbGluZV9hY2Nlc3MiXX0.s-xhD1j5ZENT45TkAmlek4SV4dGCzL11j4pBO5AL-eh5LhBaY7KWUodvdiDA-dMUThXFZ94AkvScs6eq0r-HuR_3pm3Ss4lI43R29SI5rY2wCYQJ0vUQaVvSYN4n7X6pwHvpomJAS3BSYWAbvrBMFfdrlazc03oHI4VLfhodqjSYknHS93jzvVGOYRksi2YZM6I1Vzbe_hHZwr-AMRz03TEz1Rajiu66DvIloaaol7Gpt-mvoeQc47gGTnVMWs0vsUCexCa3p1JWGfMbSMX8cXENrhdUn0E9Y3-VpKUYDvQFxq5H--iirN0S3etsh1N-R9p9PZO_BrnQbCKEBw6dnupBh61-RwIHYWn8H-lkI5HBFceZvDhsoSTfHSYISsQTEY0vlqsTwjN7Gh23tSLEtOAflD1R-GvB6Sw37xgKvuKkmbTJoCE7YEzOuTtC6M1QVNSGgRxbzoHs2rJ-8ARqOkcRQFmPFx1yWZjVCbCGwufv4Mo8JJtnRsMrpPyjf5m3tLYBo2it3GspvcYoxKPGuajeYg6SIzCAKm1WLFXc3NDb7_OmK7gXiK48eFoIOtDqSoJpNih9JvtgGZkjEW7lKQOQSAGQ0L1vdtQSdRu8MeIWGb6xaOHiC5gtYf6SXG8KGYM-brW3v16g9fpqZoLUArXcR7Sv9Etf7QgqEhwVotw; has_access_token=true; refresh_token=4ECCD8BBBE2C2685726FEFBE3B8760BE000588443D66C992050E296D7081DCC8; has_refresh_token=true; X-Magento-Vary=5a01dc66ae84d635861677306cce28738ee73de0; PHPSESSID=be86a350e06e32e356afbc98244c0f7b; mage-messages=; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; client-store-code=by; mage-cache-sessid=true; private_content_version=need_version; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gid=GA1.2.972053435.1705997252; _ym_isad=2; ga-location-city-id=relation%3A59195; DIGI_CARTID=49542864; cto_bundle=C2w2OV8ybkd6V2FpNWM5OGJFbEVVM3g0T3o1M25PaFA4V2djS0xzdExiSlYzcXlIOE9pcWxKSTNOVGdLeHNjbm1JRTZvZFNYTEglMkJyN0dyNSUyQmlwT1o0dUxXZHl2TUNLUWVUZHVuMzFTTVZnRDhpYXJld2N1MkdMdjBMOE9pdUhUbHM0WUdraUpkdGtXWFh2Z0NmMXJrQjJXYVVNOTVYZzJ2ZXgyNUlHa09LUjV2OW1LTXJqVEZvNlRnS3FuaG5zWTJDQWNLT1JSd3BPNUdwRllKZnZOJTJCNWFwZE13JTNEJTNE; dSesn=8a945ef2-83b0-04e3-2610-3280f8f40150; _dvs=0:lrq6ink4:nAOKaNYSvLQ_jPrbU5bH6Nf_I65NL5eM; digi-analytics-sessionId=scn92kHRQYb2o5x5AmO0Z; _spx=eyJpZCI6ImFjOGFhYWY1LThhNGUtNDYyNi05YjI1LWYyMzBkNDczY2IxZSIsImZpeGVkIjp7InN0YWNrIjpbMCwwLC05MjIyOTc4MzcsMCwwXX19; _ga=GA1.2.837300893.1701367627; tmr_detect=0%7C1706003757050; section_data_ids=%7B%22cart%22%3A1706003800%2C%22geolocation%22%3A1706003727%2C%22customer%22%3A1705997232%2C%22compare-products%22%3A1705997232%2C%22last-ordered-items%22%3A1705997232%2C%22directory-data%22%3A1705997233%2C%22captcha%22%3A1705997232%2C%22wishlist%22%3A1706003619%2C%22multiplewishlist%22%3A1705997232%2C%22goldcards%22%3A1705997232%2C%22adult_goods%22%3A1706003729%2C%22recently_viewed_product%22%3A1705997232%2C%22recently_compared_product%22%3A1705997232%2C%22product_data_storage%22%3A1705997232%7D; _ga_QE5MQ8XJJK=GS1.1.1706003636.11.1.1706004799.0.0.0',
        'origin': 'https://goldapple.by',
        'referer': 'https://goldapple.by/catalogsearch/result?q=kiki',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-b73568cfaab9e96818257d2bdeff74c2-fb0d46576d0eda1f-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200)

    with allure.step('Проверка метода'):
        check.equal(response.request.method, 'PUT')

    with allure.step('Проверка что значение параметра data не пустое'):
        response_data = response.json()
        if 'data' in response_data:
            print(response_data['data'])
            check.is_not_none(response_data['data'])
        else:
            print('Ошибка')

