from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

PHONE_NUMBER = 'your ohone number'
PASSWORD = 'your password'
PORTAL_URL = 'https://efelerbelediyesi.yonettwifi.com.tr/'
CHECK_URL = 'https://1.1.1.1'


def login():
    driver = webdriver.Edge()
    driver.get(PORTAL_URL)
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        driver.find_element(By.XPATH, '//a[text()="Giriş Yap"]').click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'phone').send_keys(PHONE_NUMBER)
        driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        driver.find_element(By.ID, 'login').click()
    except Exception as e:
        print({e})

def check_connection(ip):
    try:
        requests.get(ip)
        return True
    except requests.exceptions.ConnectionError:
        return False

if __name__ == '__main__':
    if check_connection(CHECK_URL) == False:
        login()
        if check_connection(CHECK_URL) == True:
            print('Connected to the internet')
        else:
            print('Could not connect to the internet')
    else:
        print('Already connected to the internet')

