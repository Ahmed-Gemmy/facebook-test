from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL = 'https://www.facebook.com'
username = 'USER_NAME'
password = 'MY_PASSWORD'

driver = webdriver.Firefox()
driver.get(URL)
email_elm = driver.find_element_by_id('email')
email_elm.send_keys(username)
password_elm = driver.find_element_by_id('pass')
password_elm.send_keys(password)
driver.find_element_by_id('u_0_n').click()
WebDriverWait(driver, 3).until(
    expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '//*[@id="u_0_g"]/a'),
        'Home'
    )
)
driver.find_element_by_id('pageLoginAnchor').click()
driver.find_element_by_css_selector('input.uiLinkButtonInput').click()
driver.close()