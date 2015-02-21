from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """
    Selenium locators for the Home page.
    """

    LOGIN_BUTTON = (By.ID, 'u_0_n')
    PASSWORD = (By.ID, 'pass')
    USER_NAME = (By.ID, 'email')


class HeaderLocators(object):
    """
    Selenium locators found in the header after login.
    """
    HOME_LINK = (By.XPATH, '//*[@id="u_0_g"]/a')
    LOGIN_ANCHOR = (By.ID, 'pageLoginAnchor')
    LOGOUT = (By.CSS_SELECTOR, 'input.uiLinkButtonInput')


class SettingPageLocators(object):
    """
    Selenium locators for the settings page including edit profile page.
    """
    ADD_PROFILE_BTN = (By.CSS_SELECTOR, 'input.add-profile.blue')
    ADDED_PROFILES = (By.XPATH, "//li[@data-type='social']")
    ADDED_PROFILES_REMOVE = (By.XPATH, "//li[@data-type='social']/span[@class='close']")
    EDIT_PROFILE_LINK = (By.CLASS_NAME, 'edit-avatar')
    IMAGE_BUTTON = (By.ID, 'edit-picture-upload-button')
    IMAGE_FILE_SELECTOR = (By.ID, 'edit-picture-upload')
    LOCATION = (By.XPATH, "//div[@id='edit-field-country-und_child']/ul/li/span[contains(text(), '%s')]")
    LOCATION_DISPLAY = (By.XPATH, "//span[@id='edit-field-country-und_title']/span")
    LOCATION_DROP = (By.ID, 'edit-field-country-und_title')
    PROFILE_ELEMENT = (By.XPATH, "//div[@id='profile-type_child']/ul/li/span[contains(text(), '%s')]")
    PROFILE_NAME_TEXT = (By.ID, 'edit-field-profiles')
    PROFILE_SELECT = (By.ID, 'profile-type_title')
    SAVE_CHANGES_BUTTON = (By.ID, 'edit-submit')
    WEBSITE = (By.ID, 'edit-field-website-und-0-value')

