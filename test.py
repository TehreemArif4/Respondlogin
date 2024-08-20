import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By

#from Login import success_element

# Configuration variables for the login page
URL = "https://app.respond.io/user/login"
VALID_EMAIL = "tehreema9@gmail.com"
VALID_PASSWORD = "Admin1258."
INVALID_EMAIL = "test@example.com"
INVALID_PASSWORD = "Admin284e2749"

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "input-7")  # Adjust selectors as per your app
        self.password_input = (By.ID, "input-9")
        self.signin_button = (By.XPATH, "//button[@type='submit']")
        self.failure_alert = (By.ID, "alert")
        self.success_element = ((By.XPATH, "/html/body/div[3]/div/div/div/main/div/div[2]/div/div[1]/header/div/div[1]/div/div/div/div"))
        self.sso = ((By.XPATH, "//*[@id='authContainer']/div[1]/div[2]/div/div/form/div[1]/a"))
        self.google = (By.ID, "identifierId")

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_signin(self):
        self.driver.find_element(*self.signin_button).click()

    def click_sso(self):
        self.driver.find_element(*self.sso).click()

    def get_error_message(self):
        return self.driver.find_element(*self.failure_alert).text

    def get_success(self):
        return self.driver.find_element(*self.success_element).text

    def google(self):
        return self.driver.find_element(*self.google)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_sso(driver):
    driver.get(URL)
    login_page = Login(driver)

    # Test sso button
    login_page.click_sso()
    driver.implicitly_wait(20)
    # Assert successful login
    #assert driver.current_url != URL
    assert login_page.google

def test_successful_login(driver):
    driver.get(URL)
    login_page = Login(driver)

    # Test valid login
    login_page.enter_email(VALID_EMAIL)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_signin()
    driver.implicitly_wait(30)
    # Assert successful login
    #assert driver.current_url != URL
    assert login_page.success_element


def test_invalid_email_login(driver):
    driver.get(URL)
    login_page = Login(driver)

    # Test login with an invalid email
    login_page.enter_email(INVALID_EMAIL)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_signin()
    # Assert error message for invalid email
    driver.implicitly_wait(10)
    assert login_page.failure_alert

def test_invalid_password_login(driver):
    driver.get(URL)
    login_page = Login(driver)

    # Test login with an invalid password
    login_page.enter_email(VALID_EMAIL)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_signin()

    # Assert error message for invalid password
    driver.implicitly_wait(10)
    assert login_page.failure_alert



