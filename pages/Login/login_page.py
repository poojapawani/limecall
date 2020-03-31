from selenium.webdriver.common.by import By
from limecallautomation.base.selenium_driver import SeleniumDriver
import limecallautomation.utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
        wd = SeleniumDriver(driver)

    #Locators
    _username_field = 'login-username'
    _password_field = 'login-password'
    _submit_button = '//button[@class="btn btn-rounded btn-hero-success btn-block custom-btn-color"]'
    _dashboard_label ='pageTitle'
    _username_field_error='login-username-error'
    _password_field_error = 'login-password-error'


    def enterUsername (self, username):
        self.sendKeys(locator=self._username_field,data=username,locatorType='id')

    def enterPassword (self,password):
        self.sendKeys(locator=self._password_field,data=password,locatorType='id')

    def clickSubmitButton (self):
        self.ElementClick(locator=self._submit_button, locatorType='xpath')

    def login (self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickSubmitButton()
        self.driver.implicitly_wait(5)

    def login_verification(self):
        result = self.isElementPresent(locator=self._dashboard_label)
        return result

    def login_verification_negative(self):
        result = self.isElementPresent(locator = "//*[text()='Invalid Email or Password']",locatorType='xpath')
        return result

    def login_emailfield_verification(self):
        result = self.getElement(locator=self._username_field_error).text
        return result

    def login_passwordfield_verification(self):
        result = self.getElement(locator=self._password_field_error).text
        return result
