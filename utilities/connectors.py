import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.constants import *

import base64
import json

from utilities.utilites import *


def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    return chrome_browser


def get_token():
    def esia_login_administrator(browser):
        browser.get(HOST)
        browser.find_element(By.XPATH, "//button[contains(text(), 'Отправить обращение (ЕСИА)')]").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//input[@id='login']").send_keys(LOGIN_ADMINISTARTOR)
        browser.find_element(By.XPATH, "//input[@id='password']").send_keys(PASSWORD_ADMINISTARTOR)
        time.sleep(3)
        browser.find_element(By.CLASS_NAME, "plain-button_wide").click()
        time.sleep(3)

    def get_token_from_local_storage(browser):
        token_script = """
            return window.localStorage.getItem('token');
        """
        saved_token = browser.execute_script(token_script)
        return saved_token

    chrome_browser = webdriver.Chrome()
    esia_login_administrator(chrome_browser)
    new_token = get_token_from_local_storage(chrome_browser)
    chrome_browser.quit()

    return new_token


token = get_token()


def get_reception_user_id(current_token):
    def parse_jwt(token):
        # Разбиваем токен по точкам и выбираем вторую часть
        _, payload, _ = token.split('.')

        # Декодируем base64 и десериализуем JSON
        json_payload = base64.urlsafe_b64decode(payload + '==').decode('utf-8')
        return json.loads(json_payload)

    jwt_token = current_token
    parsed_token = parse_jwt(jwt_token)
    id_value = parsed_token.get('id')  # Получаем значение ключа 'id'
    return id_value


def get_department_id():
    response = requests.get(f'{API_HOST}{API_DEPARTMENTS}')
    return response.json()[0]["id"]


new_department_id = get_department_id()


def create_topic_id():
    payload = {'hidden_payload'}
    response = requests.post(
        f'{API_HOST}{API_TOPICS}create',
        headers={'Authorization': f'Bearer {token}'},
        json=payload
    )
    response_json = response.json()
    return response_json["id"]


new_topic_id = create_topic_id()


def get_guest_petition_id():
    payload = {'hidden_payload'}
    response = requests.post(f'{API_HOST}{API_GUEST}create', json=payload)
    response_json = response.json()
    return response_json["id"]


new_guest_petition_id = get_guest_petition_id()
