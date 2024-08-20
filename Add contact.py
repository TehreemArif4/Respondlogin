from logging import lastResort

import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By

#from Login import success_element

# Configuration variables
URL = "https://app.respond.io/user/login"
VALID_EMAIL = "tehreema9@gmail.com"
VALID_PASSWORD = "Admin1258."
FIRST_NAME = "USERX"
LAST_NAME = "TEST"
EMAIL = "tehreema9+userx@gmail.com"

class Contact:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "input-7")  # Adjust selectors as per your app
        self.password_input = (By.ID, "input-9")
        self.signin_button = (By.XPATH, "//button[@type='submit']")
        self.first_name = (By.ID, "input-381")
        self.last_name = (By.ID, "input-1123")
        self.last_name = (By.ID, "input-1125")
        self.contact_panel = (By.XPATH, "//*[@id='root'']/div/div/div/nav/div/div[1]/a[3]/div[2]/div[1]/div[2]")
        self.add_contact = (By.XPATH, "/html/body/div[3]/div/div/div/main/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/header/div/div[2]/div[3]/div/button[1]/button")
        self.create_contact = (By.XPATH, "/html/body/div[13]/footer/div/button[2]")

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_signin(self):
        self.driver.find_element(*self.signin_button).click()

    def click_contact_panel(self):
        self.driver.find_element(*self.contact_panel).click()

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.email_input).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.email_input).send_keys(lastname)

    def enter_contactemail(self, email):
            self.driver.find_element(*self.email_input).send_keys(email)

    def click_addcontact(self):
        self.driver.find_element(*self.add_contact).click()

    def click_createcontact(self):
        self.driver.find_element(*self.add_contact).click()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_contact_creation_with_first_name (driver):
    driver.get(URL)
    contact = Contact(driver)

    # Test CONTACT CREATION with first name
    contact.enter_email(VALID_EMAIL)
    contact.enter_password(VALID_PASSWORD)
    contact.click_signin()
    driver.implicitly_wait(30)
    contact.click_contact_panel()
    contact.click_addcontact()
    contact.enter_firstname(FIRST_NAME)
    contact.click_createcontact()


def test_successful_contact_creation_with_all_values (driver):
    driver.get(URL)
    contact = Contact(driver)

    # Test CONTACT CREATION with all values
    contact.enter_email(VALID_EMAIL)
    contact.enter_password(VALID_PASSWORD)
    contact.click_signin()
    driver.implicitly_wait(30)
    contact.click_contact_panel()
    contact.click_addcontact()
    contact.enter_firstname(FIRST_NAME)
    contact.enter_lastname(LAST_NAME)
    contact.enter_contactemail(EMAIL)
    contact.click_createcontact()




