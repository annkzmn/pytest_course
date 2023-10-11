from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_log_out():
    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url
    # print(url_before)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(1)

    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()
    # time.sleep(5)

    url_after = driver.current_url
    # print(url_after)
    # assert url_after == "https://www.saucedemo.com/"

    assert url_after == url_before