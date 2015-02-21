from selenium import webdriver
from page import HomePage

driver = webdriver.Firefox()
driver.get('https://www.facebook.com')

home_page = HomePage(driver)
home_page.login(username='USER_NAME', password='PASSWORD')
home_page.log_out()

driver.close()