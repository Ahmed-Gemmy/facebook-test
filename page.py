from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import HomePageLocators, HeaderLocators, SettingPageLocators


class BasePage(object):
    """
    BasePage class extends object, it only initiates a new driver.
    """

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """
    Extends BasePage class.
    It is a holder for all the functionalities for the homepage http://visual.ly/
    """

    def login(self, username, password):
        """
        Locates the username, password input fields.
        Then, inserts the given username and password to these fields and after that clicking on the login button.

        :param username: The username to the system.
        :param password: The password associated with the given username
        :return: True; if logged in successfully.
                 False; if there was a problem in log in.
        """
        self.driver.find_element(*HomePageLocators.USER_NAME).send_keys(username)
        self.driver.find_element(*HomePageLocators.PASSWORD).send_keys(password)

        btn = self.driver.find_element(*HomePageLocators.LOGIN_BUTTON)
        while not btn.is_enabled():
            continue
        btn.click()

        try:
            WebDriverWait(self.driver, 3).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, '//*[@id="u_0_g"]/a'),
                    'Home'
                )
            )
            return True
        except:
            return False

    def log_out(self):
        """
        Locates and clicks the logout button
        :return: None
        """
        self.driver.find_element(*HeaderLocators.LOGIN_ANCHOR).click()
        self.driver.find_element(*HeaderLocators.LOGOUT).click()
